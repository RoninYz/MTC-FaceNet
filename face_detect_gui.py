# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_detect_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(837, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_vedio = QtWidgets.QLabel(self.centralwidget)
        self.label_vedio.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.label_vedio.setStyleSheet("border: 1px solid black;")
        self.label_vedio.setText("")
        self.label_vedio.setObjectName("label_vedio")
        self.label_total = QtWidgets.QLabel(self.centralwidget)
        self.label_total.setGeometry(QtCore.QRect(660, 200, 171, 51))
        self.label_total.setStyleSheet("border: 1px solid black;\n"
"font: 17pt \"华文行楷\";")
        self.label_total.setObjectName("label_total")
        # MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 837, 23))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_total.setText(_translate("MainWindow", "总人数："))