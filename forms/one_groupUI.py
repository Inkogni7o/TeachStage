# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'one_group.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.print_table_btn = QtWidgets.QPushButton('Распечатать', self.centralwidget)
        self.horizontalLayout.addWidget(self.print_table_btn)
        self.was_2 = QtWidgets.QPushButton(self.centralwidget)
        self.was_2.setObjectName("was_2")
        self.horizontalLayout.addWidget(self.was_2)
        self.was_1 = QtWidgets.QPushButton(self.centralwidget)
        self.was_1.setObjectName("was_1")
        self.horizontalLayout.addWidget(self.was_1)
        self.was_0 = QtWidgets.QPushButton(self.centralwidget)
        self.was_0.setObjectName("was_0")
        self.horizontalLayout.addWidget(self.was_0)
        self.add_pupil = QtWidgets.QPushButton(self.centralwidget)
        self.add_pupil.setObjectName("add_pupil")
        self.horizontalLayout.addWidget(self.add_pupil)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.was_2.setText(_translate("MainWindow", "Присутствовал на 2"))
        self.was_1.setText(_translate("MainWindow", "Присутвовал на 1"))
        self.was_0.setText(_translate("MainWindow", "Отсутствовал"))
        self.add_pupil.setText(_translate("MainWindow", "Добавить ученика"))
