# -*- coding: UTF-8 -*-
import sqlite3

from PyQt5.QtWidgets import QMainWindow
from forms.one_groupUI import Ui_MainWindow


class EditGroupWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, id_group: int):
        super(EditGroupWindow, self).__init__()
        self.setupUi(self)
        with sqlite3.connect('main_db.db') as con:
            cur = con.cursor()
            self.result = cur.execute(""" """)
