# -*- coding: UTF-8 -*-
import sqlite3

from PyQt5.QtWidgets import QWidget
from forms.regUI import Ui_Form


class RegWindow(QWidget, Ui_Form):
    def __init__(self):
        super(RegWindow, self).__init__()
        self.setupUi(self)
        self.lets_begin_btn.clicked.connect(self.new_user)

    def new_user(self):
        if self.password.text() == self.password2.text():
            with sqlite3.connect('main_db.db') as con:
                cur = con.cursor()
                cur.execute("""INSERT INTO users(login,password,name,second_name) VALUES(?,?,?,?)""",
                            (self.login_input.text(), self.password.text(), self.name_input.text(),
                             self.name2_input.text()))
                con.commit()
