# -*- coding: UTF-8 -*-
import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from forms.one_groupUI import Ui_MainWindow


class EditGroupWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, id_group: int):
        super(EditGroupWindow, self).__init__()
        self.setupUi(self)
        self.update_table(id_group)

    def update_table(self, id_group: int):
        with sqlite3.connect('main_db.db') as con:
            cur = con.cursor()
            self.result = cur.execute("""SELECT id,name,second_name,attendance FROM pupils 
            WHERE id_group = ?""", (id_group,)).fetchall()
            self.tableWidget.setRowCount(len(self.result))
            self.tableWidget.setColumnCount(len(self.result[0][-1].split(',')) + 1)
            self.tableWidget.setHorizontalHeaderLabels(['Имя', '22.10', '23.10', '24.10'])
            for i, pupil in enumerate(self.result):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(pupil[1] + ' ' + pupil[2]))
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = EditGroupWindow(8)
    main_app.show()
    sys.exit(app.exec_())

