# -*- coding: UTF-8 -*-
import sqlite3

from PyQt5.QtWidgets import QWidget
from forms.statisticUI import Ui_Form


class StatisticWindow(QWidget, Ui_Form):
    def __init__(self, name: str, second_name: str, id_group: int):
        super(StatisticWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f'{second_name} {name}')
        with sqlite3.connect('main_db.db') as con:
            cur = con.cursor()
            days = cur.execute("""SELECT days_work FROM groups WHERE id=?""", (id_group,)).fetchone()[0]
            attendance = cur.execute("""SELECT attendance FROM pupils WHERE name=? AND second_name=?""",
                                     (name, second_name)).fetchone()[0]
            for i, day in enumerate(days.split(',')):
                all_months.append(day.split('.')[1:])
