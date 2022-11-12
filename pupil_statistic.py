# -*- coding: UTF-8 -*-
import sqlite3

from PyQt5.QtWidgets import QWidget
from forms.statisticUI import Ui_Form


class StatisticWindow(QWidget, Ui_Form):
    def __init__(self, name: str, second_name: str, id_group: int):
        super(StatisticWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f'{second_name} {name}')
        self.all_months, self.all_attendance = list(), dict()
        with sqlite3.connect('main_db.db') as con:
            cur = con.cursor()
            days = cur.execute("""SELECT days_work FROM groups WHERE id=?""", (id_group,)).fetchone()[0]
            attendance = cur.execute("""SELECT attendance FROM pupils WHERE name=? AND second_name=?""",
                                     (name, second_name)).fetchone()[0]

            for i, day in enumerate(days.split(',')):
                self.all_months.append('.'.join([day.split('.')[1], day.split('.')[2]]))
            self.all_months = sorted(list(set(self.all_months)), key=lambda x: (x.split('.')[1], x.split('.')[0]))
            for i, day in enumerate(days.split(',')):
                current_day = '.'.join([day.split('.')[1], day.split('.')[2]])
                self.all_attendance[current_day] = self.all_attendance.get(current_day, '') + attendance.split(',')[i]

            sums = list()
            for month in self.all_attendance.keys():
                summa = 0
                for day in self.all_attendance[month]:
                    if day == '2':
                        summa += 2
                        self.label_5.setText(str(int(self.label_5.text() if self.label_5.text() else 0) + 1))
                    elif day == '1':
                        summa += 1
                        self.label_9.setText(str(int(self.label_9.text() if self.label_9.text() else 0) + 1))
                    elif day == '0':
                        self.label_7.setText(str(int(self.label_7.text() if self.label_7.text() else 0) + 1))
                sums.append(summa)

            ax = self.figure.add_subplot(111)
            ax.plot([*range(len(self.all_months))], sums)
            ax.set_xticks([*range(len(self.all_months))])
            ax.set_xticklabels(self.all_months)
            self.graphicsView.draw()


