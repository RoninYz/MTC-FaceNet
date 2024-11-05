#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :config_event.py
# @Time      :2024/11/3 下午3:36
# @Author    :Ronin
import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import face_detect_gui as face_detect_gui
import face_detect_gui_event as face_detect_gui_event

import face_rec_gui as face_rec_gui
import face_rec_gui_event as face_rec_gui_event
class EventHandler:
    def __init__(self, main_window):
        self.main_window = main_window
        self.model = QtGui.QStandardItemModel()

    def init_events(self):
        self.main_window.btn_sel_db.clicked.connect(self.select_db_folder)
        self.main_window.cbb_input.currentIndexChanged.connect(self.on_cbb_input_changed)

        self.main_window.btn_sel_input.clicked.connect(self.select_input_file)

        self.main_window.cbb_func.currentIndexChanged.connect(self.on_cbb_func_changed)
        self.main_window.btn_start.clicked.connect(self.on_btn_start_clicked)
        self.main_window.listView.setModel(self.model)

    def add_info(self, info):
        item = QtGui.QStandardItem(info)
        self.model.appendRow(item)
    def select_db_folder(self):
        options = QtWidgets.QFileDialog.Options()
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            "选择文件夹",
            "",
            options=options
        )
        if folder_path:
            self.main_window.textBrowser.setText(folder_path)
            self.add_info("设置数据库：" + folder_path)

    def select_input_file(self):
        current_text = self.main_window.cbb_input.currentText()
        if(current_text == "图片"):
            options = QtWidgets.QFileDialog.Options()
            file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
                None,
                "选择文件",
                "",
                "所有文件 (*);;文本文件 (*.txt);;Python 文件 (*.py)",
                options=options
            )
            if file_path:
                self.main_window.textBrowser_2.setText(file_path)
                self.add_info("设置文件路径：" + file_path)

    def on_cbb_input_changed(self, index):
        current_text = self.main_window.cbb_input.currentText()
        self.add_info("输入源已更改为：" + current_text)

    def on_cbb_func_changed(self, index):
        current_text = self.main_window.cbb_func.currentText()
        self.add_info("功能设置为：" + current_text)

    def on_btn_start_clicked(self):
        current_db = self.main_window.textBrowser.toPlainText()
        current_input = self.main_window.textBrowser_2.toPlainText()
        current_input_src = self.main_window.cbb_input.currentText()
        current_func = self.main_window.cbb_func.currentText()
        config_dict = {"db": current_db, "input": current_input,
                       "input_src":current_input_src,"func": current_func}
        if(self.validate_config(config_dict) is False):
            return
        self.add_info("开始运行")

        if(current_func == "人脸检测"):
            new_window = face_detect_win(config_dict)
            new_window.show()
            new_window.exec_()

        elif(current_func == "人脸识别"):
            new_window = face_rec_win(config_dict)
            new_window.show()
            new_window.exec_()
    def validate_config(self, config_dict):
        if config_dict["input_src"]=="图片":
            current_input = config_dict["input"].strip()
            if not current_input:
                self.add_info("警告: 请输入文件路径")
                return False

            if not os.path.exists(current_input):
                self.add_info("警告: 路径不存在")
                return False

            if not os.path.isfile(current_input):
                self.add_info("警告: 路径不是文件")
                return False

            _, file_extension = os.path.splitext(current_input)
            valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif']

            if file_extension.lower() not in valid_extensions:
                self.add_info("警告: 请输入图片")
                return False

        if config_dict["func"]=="人脸识别":
            current_db = config_dict["db"].strip()
            if not current_db:
                self.add_info("警告: 请输入数据库路径")
                return False
            if not os.path.exists(current_db):
                self.add_info("警告: 数据库路径不存在")
                return False

        if config_dict["input_src"]=="摄像头" and config_dict["func"]=="人脸检测":
            self.add_info("警告: 摄像头暂不支持人脸检测功能")
            return False
        return True

class face_detect_win(QtWidgets.QDialog):
    def __init__(self, config_dict, parent=None):
        super(face_detect_win, self).__init__(parent)
        self.ui = face_detect_gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.event=face_detect_gui_event.EventHandler(self.ui,config_dict)
        self.event.init_events()

class face_rec_win(QtWidgets.QDialog):
    def __init__(self, config_dict, parent=None):
        super(face_rec_win, self).__init__(parent)
        self.ui = face_rec_gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.event=face_rec_gui_event.EventHandler(self.ui,config_dict)
        self.event.init_events()