# -*- coding: UTF-8 -*-
import sqlite3
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMenu, QAction, QAbstractItemView

from forms.one_groupUI import Ui_MainWindow
from new_pupil import NewPupilWindow
from new_lesson import NewLessonWindow


# класс, созданный для уцентрирования ячеек
class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


class EditGroupWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, id_group: int):
        super(EditGroupWindow, self).__init__()
        self.setupUi(self)
        self.id_group = id_group
        self.update_table(self.id_group)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        # TODO: сделать окно статистики ученика
        self.add_pupil_action = QAction('Добавить ученика', self)
        self.statistic_action = QAction('Статистика ученика', self)
        self.delete_pupil_action = QAction('Удалить ученика', self)

        self.separator = QAction(self)
        self.separator.setSeparator(True)

        self.add_date_action = QAction('Добавить занятие', self)
        self.redact_date_action = QAction('Перенести занятие', self)
        self.delete_date_action = QAction('Удалить занятие', self)

        self.add_pupil_action.triggered.connect(self.new_pupil)
        # self.statistic_action.triggered.connect()
        # self.delete_pupil.triggered.connect()
        self.add_date_action.triggered.connect(lambda: self.configure_date('n'))
        # self.redact_date.triggered.connect()
        self.delete_date_action.triggered.connect(lambda: self.configure_date('d'))

        contextMenu.addAction(self.add_pupil_action)
        contextMenu.addAction(self.statistic_action)
        contextMenu.addAction(self.delete_pupil_action)
        contextMenu.addAction(self.separator)
        contextMenu.addAction(self.add_date_action)
        contextMenu.addAction(self.redact_date_action)
        contextMenu.addAction(self.delete_date_action)

        self.action = contextMenu.exec_(self.mapToGlobal(event.pos()))

    def update_table(self, id_group: int):
        with sqlite3.connect('main_db.db') as con:
            cur = con.cursor()
            self.pupils = sorted(cur.execute("""SELECT id,name,second_name,attendance FROM pupils 
                WHERE id_group = ?""", (id_group,)).fetchall(), key=lambda x: x[1])
            self.timetable = cur.execute("""SELECT days_work,title FROM groups WHERE id = ?""", (id_group,)).fetchone()

        self.setWindowTitle(self.timetable[1])
        self.tableWidget.setRowCount(len(self.pupils))
        self.tableWidget.setColumnCount(len(self.timetable[0].split(',')))
        self.tableWidget.setHorizontalHeaderLabels(['.'.join(i.split('.')[:2]) for i in self.timetable[0].split(',')])
        self.tableWidget.setVerticalHeaderLabels([str(i[1]) + ' ' + str(i[2]) for i in self.pupils])

        for i, pupil in enumerate(self.pupils):
            for j, day in enumerate(pupil[-1].split(',')):
                delegate = AlignDelegate(self.tableWidget)
                self.tableWidget.setItemDelegateForColumn(j, delegate)
                if day == '2':
                    self.tableWidget.setItem(i, j, QTableWidgetItem('✔'))
                    self.tableWidget.item(i, j).setBackground(QColor(0, 255, 0))
                elif day == '1':
                    self.tableWidget.setItem(i, j, QTableWidgetItem(' '))
                    self.tableWidget.item(i, j).setBackground(QColor(255, 255, 51))
                elif day == '0':
                    self.tableWidget.setItem(i, j, QTableWidgetItem('❌'))
                    self.tableWidget.item(i, j).setBackground(QColor(255, 0, 0))
                # отсутствовал на тех занятиях, когда не занесли в базу (серый фон)
                elif day == 'X':
                    self.tableWidget.setItem(i, j, QTableWidgetItem(' '))
                    self.tableWidget.item(i, j).setBackground(QColor(160, 160, 160))
                else:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(' '))

        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()

    def new_pupil(self):
        wndw = NewPupilWindow(self.windowTitle())
        wndw.show()
        wndw.buttonBox.accepted.connect(lambda: self.update_table(self.id_group))

    def configure_date(self, mode: str):
        if mode == 'n':
            self.wndw = NewLessonWindow(self.id_group)
            self.wndw.show()
            self.wndw.buttonBox.accepted.connect(lambda: self.update_table(self.id_group))
        if mode == 'd':
            current_index = self.tableWidget.currentColumn()
            with sqlite3.connect('main_db.db') as con:
                cur = con.cursor()
                old_days_work = cur.execute("""SELECT days_work FROM groups WHERE id=?""",
                                            (self.id_group,)).fetchone()[0].split(',')
                old_days_work.pop(current_index)
                new_days_work = ','.join(old_days_work)
                cur.execute("""UPDATE groups SET days_work=? WHERE id=?""", (new_days_work, self.id_group,))

                pupils = cur.execute("""SELECT id,attendance FROM pupils WHERE id_group=?""", (self.id_group,))
                for pupil in pupils:
                    new_attendance = pupil[1].split(',')
                    new_attendance.pop(current_index)
                    cur.execute("""UPDATE pupils SET attendance=? WHERE id=?""",
                                (','.join(new_attendance), pupil[0]))
                con.commit()
                self.tableWidget.removeColumn(current_index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = EditGroupWindow(7)
    main_app.show()
    sys.exit(app.exec_())
