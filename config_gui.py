# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(354, 327)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 321, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setStyleSheet("font: 12pt \"华文行楷\";")
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.btn_sel_db = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.btn_sel_db.setObjectName("btn_sel_db")
        self.horizontalLayout.addWidget(self.btn_sel_db)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 60, 321, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(11)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_3.setStyleSheet("font: 12pt \"华文行楷\";")
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.cbb_input = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.cbb_input.setObjectName("cbb_input")
        self.cbb_input.addItem("")
        self.cbb_input.addItem("")
        self.horizontalLayout_2.addWidget(self.cbb_input)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_2.addWidget(self.textBrowser_2)
        self.btn_sel_input = QtWidgets.QToolButton(self.horizontalLayoutWidget_2)
        self.btn_sel_input.setObjectName("btn_sel_input")
        self.horizontalLayout_2.addWidget(self.btn_sel_input)
        self.horizontalLayout_2.setStretch(2, 5)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 100, 151, 22))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setStyleSheet("font: 12pt \"华文行楷\";")
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.cbb_func = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.cbb_func.setObjectName("cbb_func")
        self.cbb_func.addItem("")
        self.cbb_func.addItem("")
        self.horizontalLayout_3.addWidget(self.cbb_func)
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(210, 90, 71, 51))
        self.btn_start.setStyleSheet("font: 12pt \"华文行楷\";")
        self.btn_start.setObjectName("btn_start")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(30, 150, 301, 121))
        self.listView.setObjectName("listView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 354, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "数据库："))
        self.btn_sel_db.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "输入源："))
        self.cbb_input.setItemText(0, _translate("MainWindow", "图片"))
        self.cbb_input.setItemText(1, _translate("MainWindow", "摄像头"))
        self.btn_sel_input.setText(_translate("MainWindow", "..."))
        self.label_4.setText(_translate("MainWindow", "功能："))
        self.cbb_func.setItemText(0, _translate("MainWindow", "人脸检测"))
        self.cbb_func.setItemText(1, _translate("MainWindow", "人脸识别"))
        self.btn_start.setText(_translate("MainWindow", "启动"))
        self.menu.setTitle(_translate("MainWindow", "人脸识别系统"))
        self.menu_2.setTitle(_translate("MainWindow", "【作者】杨焯"))
        self.menu_3.setTitle(_translate("MainWindow", "李昌益"))
