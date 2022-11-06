# -*- coding: UTF-8 -*-
import sys

from PyQt5.QtWidgets import QWidget, QApplication
from forms.add_pupilUI import Ui_Form


class NewPupilWindow(QWidget, Ui_Form):
    def __init__(self):
        super(NewPupilWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = NewPupilWindow()
    main_app.show()
    sys.exit(app.exec_())