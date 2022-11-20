# -*- coding: UTF-8 -*-
import sqlite3
import sys

from PyQt5.QtWidgets import QWidget, QApplication
from forms.teacher_pageUI import Ui_Form


class TeacherWindow(QWidget, Ui_Form):
    def __init__(self, login: str):
        super(TeacherWindow, self).__init__()
        self.setWindowTitle('Подсчёт заработка')
        self.setupUi(self)
        self.login = login
        self.radioButton.clicked.connect(self.update_data)
        self.radioButton_2.clicked.connect(self.update_data)
        self.comboBox_2.currentTextChanged.connect(self.update_data)

        with sqlite3.connect("""main_db.db""") as con:
            cur = con.cursor()
            self.groups = cur.execute("""SELECT id,title,cost,percent,days_work FROM groups
             WHERE teacher_login=?""", (login,)).fetchall()
            self.comboBox_2.addItems([i[1] for i in self.groups])

    def update_data(self):
        with sqlite3.connect('main_db.db') as con:
            cur = con.cursor()
            self.pupils = cur.execute("""SELECT attendance FROM pupils WHERE id_group=?""",
                                      (self.groups[self.comboBox_2.currentIndex()][0],)).fetchall()
        if self.radioButton_2.isChecked():
            irreplaceable_lessons, attended_lessons = 0, 0
            for pupil in self.pupils:
                pupil_attendance = pupil[0].split(',')
                irreplaceable_lessons += pupil_attendance.count('X')
                attended_lessons += pupil_attendance.count('2') * 2 + pupil_attendance.count('1')
            self.lineEdit.setText(str(
                attended_lessons * int(self.groups[self.comboBox_2.currentIndex()][2])
                * float(self.groups[self.comboBox_2.currentIndex()][3])
            ))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TeacherWindow('Логин')
    ex.show()
    sys.exit(app.exec())


