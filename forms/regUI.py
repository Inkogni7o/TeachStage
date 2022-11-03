# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(393, 256)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 20, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 55, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 55, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 55, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 121, 16))
        self.label_6.setObjectName("label_6")

        self.lets_begin_btn = QtWidgets.QPushButton(Form)
        self.lets_begin_btn.setGeometry(QtCore.QRect(240, 210, 131, 28))
        self.lets_begin_btn.setObjectName("lets_begin_btn")

        self.password2 = QtWidgets.QLineEdit(Form)
        self.password2.setGeometry(QtCore.QRect(150, 170, 171, 22))
        self.password2.setObjectName("password2")

        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(150, 140, 171, 22))
        self.password.setObjectName("password")

        self.name_input = QtWidgets.QLineEdit(Form)
        self.name_input.setGeometry(QtCore.QRect(150, 110, 171, 22))
        self.name_input.setObjectName("name_input")

        self.name2_input = QtWidgets.QLineEdit(Form)
        self.name2_input.setGeometry(QtCore.QRect(150, 80, 171, 22))
        self.name2_input.setObjectName("name2_input")

        self.login_input = QtWidgets.QLineEdit(Form)
        self.login_input.setGeometry(QtCore.QRect(150, 50, 171, 22))
        self.login_input.setObjectName("login_input")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Регистрация"))
        self.label_2.setText(_translate("Form", "Логин:"))
        self.label_3.setText(_translate("Form", "Фамилия:"))
        self.label_4.setText(_translate("Form", "Имя:"))
        self.label_5.setText(_translate("Form", "Пароль:"))
        self.label_6.setText(_translate("Form", "Повторите пароль:"))
        self.lets_begin_btn.setText(_translate("Form", "Начнем работать!"))
