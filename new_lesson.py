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
            cur = con.cursor()
            old_dates = cur.execute("""SELECT days_work FROM groups WHERE id=?""", (id_group,)).fetchone()[0]
            new_dates = sorted(old_dates.split(',') + [f'{str(self.calendar.selectedDate().day()).rjust(2, "0")}.'
                                                       f'{str(self.calendar.selectedDate().month()).rjust(2, "0")}.'
                                                       f'{self.calendar.selectedDate().year()}.'
                                                       f'{self.timeEdit.text()}'],
                               key=lambda x: (int(x.split('.')[2]), int(x.split('.')[1]), int(x.split('.')[0])))
            new_day_index = new_dates.index(f'{str(self.calendar.selectedDate().day()).rjust(2, "0")}.'
                                            f'{str(self.calendar.selectedDate().month()).rjust(2, "0")}.'
                                            f'{self.calendar.selectedDate().year()}.'
                                            f'{self.timeEdit.text()}')
            cur.execute("""UPDATE groups SET days_work=? WHERE id=?""",
                        (','.join(new_dates), id_group))

            pupils = cur.execute("""SELECT id,attendance FROM pupils WHERE id_group=?""", (id_group,)).fetchall()
            for pupil in pupils:
                print(pupil[1], new_day_index)
                new_attendance = pupil[1].split(',')
                new_attendance.insert(new_day_index, '.')
                new_attendance = ','.join(new_attendance)
                print(new_attendance)
                cur.execute("""UPDATE pupils SET attendance=? WHERE id=?""", (new_attendance, pupil[0]))
            con.commit()
            self.close()
