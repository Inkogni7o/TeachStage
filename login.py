# -*- coding: UTF-8 -*-
from PyQt5.QtWidgets import QWidget
from forms.login1UI import Ui_login_wndw


class LogWindow(QWidget, Ui_login_wndw):
    def __init__(self):
        super(LogWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Вход в учетную запись')
