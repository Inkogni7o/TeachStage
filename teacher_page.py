# -*- coding: UTF-8 -*-
import sqlite3
import sys

from PyQt5.QtWidgets import QWidget, QApplication
from forms.teacher_pageUI import Ui_Form


class TeacherWindow(QWidget, Ui_Form):
    def __init__(self, login: str):
        super(TeacherWindow, self).__init__()
        self.setupUi(self)
        self.login = login
        self.radioButton.clicked.connect(self.update_data)
        self.comboBox_2.currentTextChanged.connect(self.update_data)

        with sqlite3.connect("""main_db.db""") as con:
            cur = con.cursor()
            self.groups = cur.execute("""SELECT title,cost,percent,days_work FROM groups
             WHERE teacher_login=?""", (login,)).fetchall()
            self.comboBox_2.addItems([i[0] for i in self.groups])

    def update_data(self):
        if self.radioButton_2.isChecked():
            self.lineEdit.setText(str(
                len(self.groups[self.comboBox_2.currentIndex()][-1].split(',')
                    * int(self.groups[self.comboBox_2.currentIndex()][1]
                          * int(self.groups[self.comboBox_2.currentIndex()][2])))
            ))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TeacherWindow('Логин')
    ex.show()
    sys.exit(app.exec())


