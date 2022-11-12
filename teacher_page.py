# -*- coding: UTF-8 -*-
import sqlite3

from PyQt5.QtWidgets import QWidget
from forms.teacher_pageUI import Ui_Form


class TeacherWindow(QWidget, Ui_Form):
    def __init__(self, login):
        super(TeacherWindow, self).__init__()
        self.setupUi(self)
        self.login = login
        with sqlite3.connect("""main_db.db""") as con:
            cur = con.cursor()
            self.groups = cur.execute("""SELECT id,title FROM groups WHERE teacher_login=?""", (login,)).fetchall()
            self.comboBox_2.addItems([i[1] for i in self.groups])


