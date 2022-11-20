# -*- coding: UTF-8 -*-
import datetime as dt
import sqlite3

import holidays
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView, QAction

from consts import DECODE_DAYS
from edit_group import EditGroupWindow
from forms.today_formUI import Ui_MainWindow
from new_group import NewGroupWindow
from new_pupil import NewPupilWindow
from teacher_page import TeacherWindow


class TodayWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, login: str):
        self.login, self.today = login, (dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day)
        self.setWindowTitle('TeachStage')
        super(TodayWindow, self).__init__()
        self.setupUi(self)
        self.add_group.triggered.connect(self.add_new_group)
        self.teacher = QAction('Открыть вкладку педагога', self)
        self.teacher_menu.addAction(self.teacher)
        self.teacher.triggered.connect(lambda: self.open_teacher(login))
        self.calendar.setSelectedDate(QDate(*self.today))
        self.display_groups()
        self.calendar.clicked.connect(self.display_groups)
        self.today_groups.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def display_groups(self):
        for day in holidays.RU(years=dt.datetime.now().year).items():
            if (day[0].day == self.calendar.selectedDate().day() and
                    day[0].month == self.calendar.selectedDate().month()):
                self.today_groups.setRowCount(1)
                self.today_groups.setItem(0, 0, QTableWidgetItem('Сегодня праздник!'))
                self.today_groups.setItem(0, 1, QTableWidgetItem(day[-1]))
                break
        else:
            day_of_the_week = DECODE_DAYS[self.calendar.selectedDate().dayOfWeek()]
            current_date = self.calendar.selectedDate()
            with sqlite3.connect('main_db.db') as con:
                cur = con.cursor()
                self.result = cur.execute("""SELECT title, days_of_the_week, starts, ends, id, days_work FROM groups 
                    WHERE days_work LIKE ? AND teacher_login=?""",
                                          (f'%{str(current_date.day()).rjust(2, "0")}.'
                                           f'{str(current_date.month()).rjust(2, "0")}.'
                                           f'{current_date.year()}%', self.login)).fetchall()

            if self.result:
                today = (f'{str(current_date.day()).rjust(2, "0")}.'
                         f'{str(current_date.month()).rjust(2, "0")}.'
                         f'{current_date.year()}')
                for i, group in enumerate(self.result):
                    index = -1
                    self.today_groups.setRowCount(len(self.result))
                    self.today_groups.setItem(i, 0, QTableWidgetItem(group[0]))

                    for dates in group[5].split():
                        if today in dates:
                            for j, date in enumerate(dates.split(',')):
                                if today in date and today != date:
                                    index = j
                                    break
                            if index == -1:
                                time = QTableWidgetItem(
                                    group[2].split()[group[1].split().index(day_of_the_week)] + ' - '
                                    + group[3].split()[group[1].split().index(day_of_the_week)])
                                self.today_groups.setItem(i, 1, time)
                            else:
                                time = QTableWidgetItem(dates.split(',')[index].split('.')[3])
                                self.today_groups.setItem(i, 1, time)
                    self.today_groups.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                    self.today_groups.scrollToItem(time)
                self.today_groups.viewport().installEventFilter(self)
            else:
                self.today_groups.setRowCount(0)
        self.today_groups.setSortingEnabled(True)

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseButtonDblClick and
                event.buttons() == QtCore.Qt.LeftButton and
                source is self.today_groups.viewport()):
            self.item = self.today_groups.itemAt(event.pos())
            self.edit_group = EditGroupWindow(self.result[[i[0] for i in self.result].index(self.item.text())][4])
            self.edit_group.show()
        return super(TodayWindow, self).eventFilter(source, event)

    def add_new_group(self):
        self.wndw = NewGroupWindow(self.login)
        self.wndw.show()
        self.wndw.buttonBox.accepted.connect(self.display_groups)

    def open_teacher(self, login):
        self.wndw = TeacherWindow(login)
        self.wndw.show()
