# -*- coding: UTF-8 -*-
import sqlite3
import sys
import holidays
from datetime import datetime, timedelta, date

from PyQt5.QtCore import QTime, QDate
from PyQt5.QtWidgets import QApplication, QWidget
from forms.add_groupUI import Ui_Form


class NewGroupWindow(QWidget, Ui_Form):
    def __init__(self, login):
        super(NewGroupWindow, self).__init__()
        self.login = login
        self.days = list()
        self.setupUi(self)
        self.setWindowTitle('Добавление новой группы')
        self.dateEdit.setDate(QDate(datetime.now().year, datetime.now().month, datetime.now().day))
        self.dateEdit_2.setDate(QDate(datetime.now().year, datetime.now().month, datetime.now().day))
        self.buttonBox.rejected.connect(lambda: self.close())
        self.buttonBox.accepted.connect(self.new_group)

        lst = [self.monday, self.tuesday, self.wendsday, self.thursday,
               self.friday, self.saturday, self.sunday]
        for word in lst:
            word.clicked.connect(self.open_time)

        self.main_dict = {
            'Понедельник': (self.time_edit_1, self.end_edit_1),
            'Вторник': (self.time_edit_2, self.end_edit_2),
            'Среда': (self.time_edit_3, self.end_edit_3),
            'Четверг': (self.time_edit_4, self.end_edit_4),
            'Пятница': (self.time_edit_5, self.end_edit_5),
            'Суббота': (self.time_edit_6, self.end_edit_6),
            'Воскресенье': (self.time_edit_7, self.end_edit_7),
            0: 'Понедельник', 1: 'Вторник', 2: 'Среда',
            3: 'Четверг', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'
        }

    def open_time(self):
        if self.main_dict[self.sender().text()][0].isEnabled() == 0:
            self.main_dict[self.sender().text()][0].setEnabled(True)
            self.main_dict[self.sender().text()][1].setEnabled(True)
            self.days.append(self.sender().text())
        else:
            self.main_dict[self.sender().text()][0].setEnabled(False)
            self.main_dict[self.sender().text()][0].setTime(QTime(0, 0))
            self.main_dict[self.sender().text()][1].setEnabled(False)
            self.main_dict[self.sender().text()][1].setTime(QTime(0, 0))
            self.days.pop(self.days.index(self.sender().text()))

    def new_group(self):
        all_work_days, end = (list(),
                              date(year=self.dateEdit_2.date().year(), month=self.dateEdit_2.date().month(),
                                   day=self.dateEdit_2.date().day()))
        day = date(year=self.dateEdit.date().year(), month=self.dateEdit.date().month(),
                   day=self.dateEdit.date().day())
        while day.month != end.month or day.day != end.day:
            for holiday in [i[0] for i in holidays.RU(years=datetime.now().year).items()]:
                if holiday.day == day.day and holiday.month == day.month:
                    day += timedelta(days=1)
                    continue
            if self.main_dict[day.weekday()] in self.days:
                all_work_days.append(str(day.day).rjust(2, '0') + '.' +
                                     str(day.month).rjust(2, '0') + '.' + str(day.year))
            day += timedelta(days=1)

        with sqlite3.connect('main_db.db') as con:
            cur = con.cursor()
            cur.execute("""INSERT INTO groups(title, teacher_login, max_count, days_of_the_week, starts,
             ends, day_start, day_end, days_work) VALUES(?,?,?,?,?,?,?,?,?)""",
                        (self.name_group_input.text(),
                         self.login,
                         int(self.count_pupils_input.text()),
                         ' '.join(self.days),
                         ' '.join([self.main_dict[i][0].text() for i in self.days]),
                         ' '.join([self.main_dict[i][1].text() for i in self.days]),
                         str(self.dateEdit.date().day()) + '.' + str(self.dateEdit.date().month()),
                         str(self.dateEdit_2.date().day()) + '.' + str(self.dateEdit_2.date().month()),
                         ','.join(all_work_days)))
            con.commit()
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = NewGroupWindow('Логин')
    main_app.show()
    sys.exit(app.exec_())
