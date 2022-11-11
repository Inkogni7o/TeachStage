# -*- coding: UTF-8 -*-
import datetime as dt
import sqlite3

from PyQt5.QtWidgets import QWidget
from forms.add_pupilUI import Ui_Form


class NewPupilWindow(QWidget, Ui_Form):
    def __init__(self, current_group: str):
        super(NewPupilWindow, self).__init__()
        self.setupUi(self)
        self.buttonBox.rejected.connect(lambda: self.close())
        self.buttonBox.accepted.connect(self.add_new_pupil)

        with sqlite3.connect('main_db.db') as con:
            cur = con.cursor()
            self.result = cur.execute("""SELECT title,id,days_work FROM groups""").fetchall()
        first_group = self.result[[i[0] for i in self.result].index(current_group)]
        self.result.pop([i[0] for i in self.result].index(current_group))
        self.result = [first_group] + self.result
        for group in self.result:
            self.choose_group.addItem(group[0])

    def add_new_pupil(self):
        days, attendance = [i[2] for i in self.result if i[0] == self.choose_group.currentText()][0], ''
        for day in days.split(','):
            if dt.datetime.now() > dt.datetime(year=int(day.split('.')[2]),
                                               month=int(day.split('.')[1]),
                                               day=int(day.split('.')[0]) + 1):
                attendance += 'X,'
            else:
                attendance += '.,'
        with sqlite3.connect('main_db.db') as con:
            cur = con.cursor()
            cur.execute("""INSERT INTO pupils(id_group, name, second_name, attendance) VALUES(?,?,?,?)""",
                        (self.result[[i[0] for i in self.result].index(self.choose_group.currentText())][1],
                         self.lineEdit.text().split()[0],
                         self.lineEdit.text().split()[1], attendance))
            con.commit()
        self.close()