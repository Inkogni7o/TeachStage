# -*- coding: UTF-8 -*-
from PyQt5.QtWidgets import QWidget
from forms.statisticUI import Ui_Form


class StatisticWindow(QWidget, Ui_Form):
    def __init__(self):
        super(StatisticWindow, self).__init__()
        self.setupUi(self)