# -*- coding: UTF-8 -*-
import sqlite3
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from forms.one_groupUI import Ui_MainWindow


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


class EditGroupWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, id_group: int):
        super(EditGroupWindow, self).__init__()
        self.setupUi(self)
        self.update_table(id_group)

    def update_table(self, id_group: int):
        with sqlite3.connect('main_db.db') as con:
            cur = con.cursor()
            self.pupils = cur.execute("""SELECT id,name,second_name,attendance FROM pupils 
                WHERE id_group = ?""", (id_group,)).fetchall()
            self.timetable = cur.execute("""SELECT days_work,title FROM groups WHERE id = ?""", (id_group,)).fetchone()

            self.setWindowTitle(self.timetable[1])
            self.tableWidget.setRowCount(len(self.pupils))
            self.tableWidget.setColumnCount(len(self.timetable[0].split(',')) + 1)
            self.tableWidget.setHorizontalHeaderLabels(['.'.join(i.split('.')[:2]) for i in self.timetable[0].split(',')])
            self.tableWidget.setVerticalHeaderLabels([i[1] + ' '+ i[2] for i in self.pupils])

            for i, pupil in enumerate(self.pupils):
                for j, day in enumerate(pupil[-1].split(',')):
                    delegate = AlignDelegate(self.tableWidget)
                    self.tableWidget.setItemDelegateForColumn(j, delegate)

                    # TODO: заменить внутренности таблицы на другие символы
                    if day == '2':
                        self.tableWidget.setItem(i, j, QTableWidgetItem('2'))
                    elif day == '1':
                        self.tableWidget.setItem(i, j, QTableWidgetItem('1'))
                    # отсутствовал на тех занятиях, когда не занесли в базу (серый фон)
                    elif day == 'X':
                        self.tableWidget.setItem(i, j, QTableWidgetItem('X'))
                    else:
                        self.tableWidget.setItem(i, j, QTableWidgetItem(' '))

            self.tableWidget.resizeRowsToContents()
            self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = EditGroupWindow(8)
    main_app.show()
    sys.exit(app.exec_())

