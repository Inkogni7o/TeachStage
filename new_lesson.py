import sqlite3

from PyQt5.QtWidgets import QWidget
from forms.new_lessonUI import Ui_Form


class NewLessonWindow(QWidget, Ui_Form):
    def __init__(self, id_group):
        super(NewLessonWindow, self).__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(lambda: self.new_lesson(id_group))
        self.buttonBox.rejected.connect(lambda: self.close)

    def new_lesson(self, id_group: int):
        with sqlite3.connect('main_db.db') as con:
            print(id_group)
            cur = con.cursor()
            old_dates = cur.execute("""SELECT additional_work_days FROM groups WHERE id=?""",
                                    (id_group,)).fetchone()[0]
            cur.execute("""UPDATE groups SET additional_work_days=? WHERE id=?""",
                        (old_dates + f'{str(self.calendar.selectedDate().day()).rjust(2, "0")}.'
                                     f'{str(self.calendar.selectedDate().month()).rjust(2, "0")}.'
                                     f'{self.calendar.selectedDate().year()}'
                                     f' - {self.timeEdit.text()}/!\\', id_group))
            con.commit()
            self.close()

