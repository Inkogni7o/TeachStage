# -*- coding: UTF-8 -*-
import datetime as dt
import sqlite3
import sys

import holidays
from PyQt5.QtCore import QDate
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView
from forms.today_formUI import Ui_MainWindow
from new_group import NewGroupWindow
from consts import DECODE_DAYS
from edit_group import EditGroupWindow
from new_pupil import NewPupilWindow


class TodayWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, login: str):
        self.login, self.today = login, (dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day)
        super(TodayWindow, self).__init__()
        self.setupUi(self)
        self.add_group.triggered.connect(self.add_new_group)
        self.calendar.setSelectedDate(QDate(*self.today))
        self.display_groups()
        self.calendar.clicked.connect(self.display_groups)

    def display_groups(self):
        for day in holidays.RU(years=dt.datetime.now().year).items():
            if (day[0].day == self.calendar.selectedDate().day() and
                    day[0].month == self.calendar.selectedDate().month()):
                self.today_groups.setRowCount(1)
                self.today_groups.setItem(0, 0, QTableWidgetItem('Сегодня праздник!'))
                self.today_groups.setItem(0, 1, QTableWidgetItem(day[-1]))
                break
        else:
            current_date = self.calendar.selectedDate()
            with sqlite3.connect('main_db.db') as con:
                cur = con.cursor()
                self.result = cur.execute("""SELECT title, days_of_the_week, starts, ends, id FROM groups 
                    WHERE days_work LIKE ?""",
                    (f'%{current_date.day()}.{current_date.month()}.{current_date.year()}%',)).fetchall()
            if self.result:
                for group in self.result:
                    day_of_the_week = DECODE_DAYS[self.calendar.selectedDate().dayOfWeek()]
                    if day_of_the_week in group[1].split():
                        print(day_of_the_week, group[1].split(), self.result)
                        self.today_groups.setRowCount(len(self.result))
                        self.today_groups.setItem(self.result.index(group), 0, QTableWidgetItem(group[0]))
                        time = QTableWidgetItem(group[2].split()[group[1].split().index(day_of_the_week)] + ' - '
                                                + group[3].split()[group[1].split().index(day_of_the_week)])
                        self.today_groups.setItem(self.result.index(group), 1, time)

                        self.today_groups.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                        self.today_groups.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                        self.today_groups.scrollToItem(time)
                self.today_groups.viewport().installEventFilter(self)
            else:
                self.today_groups.setRowCount(0)

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseButtonDblClick and
                event.buttons() == QtCore.Qt.LeftButton and
                source is self.today_groups.viewport()):
            self.item = self.today_groups.itemAt(event.pos())
            self.edit_group = EditGroupWindow(self.result[[i[0] for i in self.result].index(self.item.text())][-1])
            self.edit_group.show()
            self.edit_group.add_pupil.clicked.connect(self.add_new_pupil)
        return super(TodayWindow, self).eventFilter(source, event)

    def add_new_group(self):
        self.wndw = NewGroupWindow(self.login)
        self.wndw.show()
        self.wndw.buttonBox.accepted.connect(self.display_groups)

    def add_new_pupil(self):
        self.wndw_new = NewPupilWindow(self.item.text())
        self.wndw_new.show()
        self.wndw_new.buttonBox.accepted.connect(lambda: self.edit_group.update_table(self.result[[i[0]
            for i in self.result].index(self.item.text())][-1]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = TodayWindow('Логин')
    main_app.show()
    sys.exit(app.exec_())
