#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :config_event.py
# @Time      :2024/11/3 下午3:36
# @Author    :Ronin
import sys

import numpy as np
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import cv2

from face_rec import FaceRecognitionApp
class EventHandler:
    def __init__(self, main_window,config_dict):
        self.main_window = main_window
        self.model = QtGui.QStandardItemModel()
        self.db_path = config_dict["db"]
        self.input_path = config_dict["input"]
        self.input_src = config_dict["input_src"]
    def init_events(self):
        self.main_window.listView.setModel(self.model)
        self.add_info("正在加载模型")
        self.face_rec = FaceRecognitionApp(self.db_path)
        self.add_info("加载模型成功")
        if self.input_src == "摄像头":
            self.video_capture = cv2.VideoCapture(0)
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(30)
        elif self.input_src == "图片":
            image = Image.open(self.input_path)
            image = np.array(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            frame = self.face_rec.process_frame(image)
            frame = np.array(frame)
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QtGui.QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
            # Set the QImage to the QLabel
            self.main_window.label_vedio.setPixmap(QtGui.QPixmap.fromImage(q_image))
    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            # Convert the frame to RGB format
            frame = self.face_rec.process_frame(frame)
            frame = np.array(frame)
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the frame to QImage
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QtGui.QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
            # Set the QImage to the QLabel
            self.main_window.label_vedio.setPixmap(QtGui.QPixmap.fromImage(q_image))

    def add_info(self, info):
        current_time = datetime.now().strftime("%H:%M:%S")
        formatted_info = f"{current_time} {info}"
        item = QtGui.QStandardItem(formatted_info)
        self.model.appendRow(item)