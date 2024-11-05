#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :config_event.py
# @Time      :2024/11/3 下午3:36
# @Author    :Ronin
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import cv2

from face_detect import face_detect
class EventHandler:
    def __init__(self, main_window,config_dict):
        self.main_window = main_window
        self.img_path = config_dict["input"]

    def init_events(self):
        img, num = face_detect(self.img_path)
        cv2.imwrite(f"total_face_{num}.jpg", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        self.display_image(img)
        self.main_window.label_total.setText(f'总人数：{num}')

    def display_image(self, img):
        # 将图像转换为 QImage
        height, width, channel = img.shape
        bytes_per_line = 3 * width
        q_image = QtGui.QImage(img.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)

        # 将 QImage 设置为 QPixmap
        pixmap = QtGui.QPixmap.fromImage(q_image)

        # 设置 QLabel 的 pixmap
        self.main_window.label_vedio.setPixmap(pixmap)
        self.main_window.label_vedio.setScaledContents(True)  # 使图片自适应标签
