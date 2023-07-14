# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
#import QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
import time
#pytorch
import numpy as np
import cv2
import torch

#trt
import tensorrt as trt
import pycuda.driver as cuda

#onnx
import onnx
import onnxruntime
from mhn_2.model import MHN, simplified_model

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.start_b.setEnabled(False)

        #ui variables
        self.check_state = {"Source": False, "Device": False, "Confidence": True, "Labels": False, "Weights": False}
        self.timer = QTimer(self)
        self.vid_src_state = False
        self.cuda = False
        self.width, self.height = 400, 225

        #connect buttons
        self.ui.scr_set.clicked.connect(self.select_and_cap)
        self.ui.start_b.clicked.connect(self.start_clicked)
        self.ui.stop_b.clicked.connect(self.timer.stop)
        self.ui.browse_labels.clicked.connect(self.set_labels)
        self.ui.browse_weights.clicked.connect(self.initialize_model)

    def check_ready(self):
        if all(self.check_state.values()):
            self.ui.start_b.setEnabled(True)

    def start_clicked(self):
        self.ui.start_b.setEnabled(False)
        self.timer.timeout.connect(lambda: self.update_frame())
        self.timer.start(30)

    def update_frame(self):
        self.ret, frame = self.vid_cap.read()
        if self.ret == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (self.width, self.height))

            draw_boxes, draw_segmentation, draw_all = self.infer(frame)

            draw_box = QImage(draw_boxes.data, draw_boxes.shape[1], draw_boxes.shape[0], QImage.Format_RGB888)
            draw_box_pixmap = QPixmap.fromImage(draw_box)

            draw_seg = QImage(draw_segmentation.data, draw_segmentation.shape[1], draw_segmentation.shape[0], QImage.Format_RGB888)
            draw_seg_pixmap = QPixmap.fromImage(draw_seg)

            draw_all = QImage(draw_all.data, draw_all.shape[1], draw_all.shape[0], QImage.Format_RGB888)
            draw_all = QPixmap.fromImage(draw_all)

            self.ui.det_show.setPixmap(draw_box_pixmap)
            self.ui.seg_show.setPixmap(draw_seg_pixmap)
            self.ui.joint_show.setPixmap(draw_all)

    def select_and_cap(self):
        self.vid_src_state = self.ui.video_src.isChecked()
        if self.vid_src_state:
            filename = QFileDialog.getOpenFileName(self, 'Open File', '.', 'Video Files(*.mp4 *.avi *.mov)')[0]
        else:
            filename = 0

        self.vid_cap = cv2.VideoCapture(filename)
        self.ui.input_g.setEnabled(False)
        self.check_state["Source"] = True
        self.check_ready()
    
    def set_labels(self):
        label_path = QFileDialog.getOpenFileName(self, 'Select Label File', '.', 'Text Files(*.txt)')[0]
        with open(label_path, 'r') as f:
            self.labels = f.read().splitlines()
            labels_to_show = ' '.join(self.labels)
        self.ui.labelFile_browser.setText(labels_to_show)
        self.ui.labelmap_g.setEnabled(False)
        self.check_state["Labels"] = True
        self.check_ready()

    def initialize_model(self):
        if self.ui.with_cuda.isChecked():
            self.cuda = True
        self.check_state["Device"] = True

        if self.ui.with_torch.isChecked():
            model_path = QFileDialog.getOpenFileName(self, 'Select Weight File', '.', 'Video Files(*.pt)')[0]
            pass
        elif self.ui.with_onnx.isChecked():
            model_path = QFileDialog.getOpenFileName(self, 'Select Weight File', '.', 'Video Files(*.onnx)')[0]
            anchor_path = model_path.replace(model_path.split(".")[1], 'npy')
            self.roadEstimator = MHN(model_path, anchor_path, conf_thres=0.25, iou_thres=0.5, labelmap=self.labels, cuda=self.cuda)
        elif self.ui.with_trt.isChecked():
            model_path = QFileDialog.getOpenFileName(self, 'Select Weight File', '.', 'Video Files(*.trt *.engine)')[0]
            anchor_path = model_path.replace(model_path.split(".")[1], 'npy')
            pass

        self.ui.weightFile_browser.setText(model_path.split("/")[-1])
        self.ui.weight_g.setEnabled(False) 
        self.check_state["Weights"] = True
        self.check_ready()

    def infer(self, frame):
        if self.ui.with_torch.isChecked():
            pass
        elif self.ui.with_onnx.isChecked():
            t1 = time.time()
            self.roadEstimator(frame)
            self.ui.label_11.setText(f"{round(1 / (time.time() - t1), 2)} fps")
            self.ui.label_12.setText(f"{round((time.time() - t1)*1000, 3)} ms")
            draw_box = frame.copy()
            draw_box = self.roadEstimator.draw_boxes(draw_box)
            draw_seg = frame.copy()
            draw_seg = self.roadEstimator.draw_segmentation(draw_seg)
            draw_all = frame.copy()
            draw_all = self.roadEstimator.draw_2D(draw_all)
        elif self.ui.with_trt.isChecked():
            pass
        else:
            draw_box = np.zeros((225, 400, 3), dtype=np.float16)
            draw_seg = np.zeros((225, 400, 3), dtype=np.float16)
            draw_all = np.zeros((225, 400, 3), dtype=np.float16)

        return draw_box, draw_seg, draw_all

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
