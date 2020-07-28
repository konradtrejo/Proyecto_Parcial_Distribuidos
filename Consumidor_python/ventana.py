# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_conexion(object):
    def setupUi(self, conexion):
        conexion.setObjectName("conexion")
        conexion.resize(420, 403)
        conexion.setStyleSheet("background-color: rgb(198, 255, 203);")
        self.centralwidget = QtWidgets.QWidget(conexion)
        self.centralwidget.setObjectName("centralwidget")
        self.Bconectar = QtWidgets.QPushButton(self.centralwidget)
        self.Bconectar.setGeometry(QtCore.QRect(290, 10, 111, 31))
        self.Bconectar.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Bconectar.setObjectName("Bconectar")
        self.Bdesconectar = QtWidgets.QPushButton(self.centralwidget)
        self.Bdesconectar.setGeometry(QtCore.QRect(290, 60, 111, 31))
        self.Bdesconectar.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Bdesconectar.setObjectName("Bdesconectar")
        self.Lhost = QtWidgets.QLabel(self.centralwidget)
        self.Lhost.setGeometry(QtCore.QRect(20, 20, 51, 21))
        self.Lhost.setObjectName("Lhost")
        self.Lport = QtWidgets.QLabel(self.centralwidget)
        self.Lport.setGeometry(QtCore.QRect(20, 70, 51, 21))
        self.Lport.setObjectName("Lport")
        self.Thost = QtWidgets.QTextEdit(self.centralwidget)
        self.Thost.setGeometry(QtCore.QRect(80, 10, 171, 31))
        self.Thost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Thost.setObjectName("Thost")
        self.Tport = QtWidgets.QTextEdit(self.centralwidget)
        self.Tport.setGeometry(QtCore.QRect(80, 60, 171, 31))
        self.Tport.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tport.setObjectName("Tport")
        self.Tlogs = QtWidgets.QTextEdit(self.centralwidget)
        self.Tlogs.setGeometry(QtCore.QRect(20, 190, 371, 161))
        self.Tlogs.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tlogs.setObjectName("Tlogs")
        self.Bconsumir = QtWidgets.QPushButton(self.centralwidget)
        self.Bconsumir.setGeometry(QtCore.QRect(120, 140, 111, 31))
        self.Bconsumir.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Bconsumir.setObjectName("Bconsumir")
        self.Llogs = QtWidgets.QLabel(self.centralwidget)
        self.Llogs.setGeometry(QtCore.QRect(40, 150, 51, 21))
        self.Llogs.setObjectName("Llogs")
        self.Bproducir = QtWidgets.QPushButton(self.centralwidget)
        self.Bproducir.setGeometry(QtCore.QRect(250, 140, 111, 31))
        self.Bproducir.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.Bproducir.setObjectName("Bproducir")
        conexion.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(conexion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        conexion.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(conexion)
        self.statusbar.setObjectName("statusbar")
        conexion.setStatusBar(self.statusbar)

        self.retranslateUi(conexion)
        QtCore.QMetaObject.connectSlotsByName(conexion)

    def retranslateUi(self, conexion):
        _translate = QtCore.QCoreApplication.translate
        conexion.setWindowTitle(_translate("conexion", "Conexión con Python"))
        self.Bconectar.setText(_translate("conexion", "Conectar"))
        self.Bdesconectar.setText(_translate("conexion", "Desconectar"))
        self.Lhost.setText(_translate("conexion", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Host</span></p></body></html>"))
        self.Lport.setText(_translate("conexion", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Port</span></p></body></html>"))
        self.Bconsumir.setText(_translate("conexion", "Consumir"))
        self.Llogs.setText(_translate("conexion", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Logs</span></p></body></html>"))
        self.Bproducir.setText(_translate("conexion", "Producir"))

