# -*- coding: UTF-8 -*-
import sqlite3
import sys

from PyQt5.QtWidgets import QWidget, QApplication
from forms.add_pupilUI import Ui_Form


class NewPupilWindow(QWidget, Ui_Form):
    def __init__(self):
        super(NewPupilWindow, self).__init__()
        self.setupUi(self)
        self.buttonBox.rejected.connect(lambda: self.close())
        self.buttonBox.accepted.connect(self.add_new_pupil)
        with sqlite3.connect('main_db.db') as con:
            cur = con.cursor()
            self.result = cur.execute("""SELECT title,id,days_work FROM groups""").fetchall()
        for group in self.result:
            self.choose_group.addItem(group[0])

    def add_new_pupil(self):
        attendance = 'asdasda'
        with sqlite3.connect('main_db.db') as con:
            cur = con.cursor()
            cur.execute("""INSERT INTO pupils(id_group, name, second_name, attendance) VALUES(?,?,?,?)""",
                        (self.result[[i[0] for i in self.result].index(self.choose_group.currentText())][1],
                         self.lineEdit.text().split()[0],
                         self.lineEdit.text().split()[1], attendance))
            con.commit()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = NewPupilWindow()
    main_app.show()
    sys.exit(app.exec_())