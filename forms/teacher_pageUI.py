# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(497, 220)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 140, 151, 16))
        self.label.setObjectName("label")

        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(30, 90, 151, 20))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 150, 131, 20))
        self.radioButton_2.setObjectName("radioButton_2")

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(30, 120, 121, 22))
        self.comboBox.setObjectName("comboBox")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 201, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(350, 140, 113, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(180, 90, 171, 16))
        self.label_3.setObjectName("label_3")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 90, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 50, 431, 22))
        self.comboBox_2.setObjectName("comboBox_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Максимальный доход:"))
        self.radioButton.setText(_translate("Form", "За один месяц:"))
        self.radioButton_2.setText(_translate("Form", "За весь курс:"))
        self.label_2.setText(_translate("Form", "Запланированные занятия:"))
        self.label_3.setText(_translate("Form", "Гарантированный доход:"))
