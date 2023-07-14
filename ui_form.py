# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QTextBrowser, QVBoxLayout, QWidget)
import rc_resources

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 322, 701))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_label = QLabel(self.verticalLayoutWidget)
        self.title_label.setObjectName(u"title_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy1)
        self.title_label.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.input_g = QGroupBox(self.verticalLayoutWidget)
        self.input_g.setObjectName(u"input_g")
        sizePolicy1.setHeightForWidth(self.input_g.sizePolicy().hasHeightForWidth())
        self.input_g.setSizePolicy(sizePolicy1)
        self.input_g.setMinimumSize(QSize(0, 65))
        self.input_g.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayoutWidget_7 = QWidget(self.input_g)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(0, 20, 301, 41))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.video_src = QRadioButton(self.gridLayoutWidget_7)
        self.video_src.setObjectName(u"video_src")
        self.video_src.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.video_src.setChecked(True)

        self.gridLayout_7.addWidget(self.video_src, 0, 0, 1, 1)

        self.cam_src = QRadioButton(self.gridLayoutWidget_7)
        self.cam_src.setObjectName(u"cam_src")
        self.cam_src.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.cam_src, 0, 1, 1, 1)

        self.scr_set = QPushButton(self.gridLayoutWidget_7)
        self.scr_set.setObjectName(u"scr_set")
        sizePolicy.setHeightForWidth(self.scr_set.sizePolicy().hasHeightForWidth())
        self.scr_set.setSizePolicy(sizePolicy)
        self.scr_set.setMinimumSize(QSize(0, 0))
        self.scr_set.setMaximumSize(QSize(50, 16777215))
        self.scr_set.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")

        self.gridLayout_7.addWidget(self.scr_set, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.input_g)

        self.device_g = QGroupBox(self.verticalLayoutWidget)
        self.device_g.setObjectName(u"device_g")
        sizePolicy1.setHeightForWidth(self.device_g.sizePolicy().hasHeightForWidth())
        self.device_g.setSizePolicy(sizePolicy1)
        self.device_g.setMinimumSize(QSize(0, 65))
        self.device_g.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayoutWidget_3 = QWidget(self.device_g)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 20, 301, 41))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.with_cuda = QRadioButton(self.gridLayoutWidget_3)
        self.with_cuda.setObjectName(u"with_cuda")
        self.with_cuda.setChecked(True)

        self.gridLayout_3.addWidget(self.with_cuda, 0, 0, 1, 1)

        self.with_cpu = QRadioButton(self.gridLayoutWidget_3)
        self.with_cpu.setObjectName(u"with_cpu")

        self.gridLayout_3.addWidget(self.with_cpu, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.device_g)

        self.score_g = QGroupBox(self.verticalLayoutWidget)
        self.score_g.setObjectName(u"score_g")
        sizePolicy1.setHeightForWidth(self.score_g.sizePolicy().hasHeightForWidth())
        self.score_g.setSizePolicy(sizePolicy1)
        self.score_g.setMinimumSize(QSize(0, 70))
        self.score_g.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayoutWidget = QWidget(self.score_g)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 20, 301, 46))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)

        self.score_slider = QSlider(self.gridLayoutWidget)
        self.score_slider.setObjectName(u"score_slider")
        self.score_slider.setOrientation(Qt.Horizontal)
        self.score_slider.setTickInterval(5)

        self.gridLayout.addWidget(self.score_slider, 0, 0, 1, 2)


        self.verticalLayout.addWidget(self.score_g)

        self.framework_g = QGroupBox(self.verticalLayoutWidget)
        self.framework_g.setObjectName(u"framework_g")
        sizePolicy1.setHeightForWidth(self.framework_g.sizePolicy().hasHeightForWidth())
        self.framework_g.setSizePolicy(sizePolicy1)
        self.framework_g.setMinimumSize(QSize(0, 95))
        self.framework_g.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayoutWidget_4 = QWidget(self.framework_g)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 20, 301, 71))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.with_trt = QRadioButton(self.gridLayoutWidget_4)
        self.with_trt.setObjectName(u"with_trt")

        self.gridLayout_4.addWidget(self.with_trt, 1, 1, 1, 1)

        self.with_onnx = QRadioButton(self.gridLayoutWidget_4)
        self.with_onnx.setObjectName(u"with_onnx")
        self.with_onnx.setChecked(True)

        self.gridLayout_4.addWidget(self.with_onnx, 1, 0, 1, 1)

        self.with_torch = QRadioButton(self.gridLayoutWidget_4)
        self.with_torch.setObjectName(u"with_torch")
        self.with_torch.setChecked(False)

        self.gridLayout_4.addWidget(self.with_torch, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.framework_g)

        self.labelmap_g = QGroupBox(self.verticalLayoutWidget)
        self.labelmap_g.setObjectName(u"labelmap_g")
        sizePolicy1.setHeightForWidth(self.labelmap_g.sizePolicy().hasHeightForWidth())
        self.labelmap_g.setSizePolicy(sizePolicy1)
        self.labelmap_g.setMinimumSize(QSize(0, 70))
        self.labelmap_g.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayoutWidget_5 = QWidget(self.labelmap_g)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 20, 301, 51))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.browse_labels = QPushButton(self.gridLayoutWidget_5)
        self.browse_labels.setObjectName(u"browse_labels")
        self.browse_labels.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_5.addWidget(self.browse_labels, 0, 1, 1, 1)

        self.labelFile_browser = QTextBrowser(self.gridLayoutWidget_5)
        self.labelFile_browser.setObjectName(u"labelFile_browser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelFile_browser.sizePolicy().hasHeightForWidth())
        self.labelFile_browser.setSizePolicy(sizePolicy2)
        self.labelFile_browser.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_5.addWidget(self.labelFile_browser, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.labelmap_g)

        self.weight_g = QGroupBox(self.verticalLayoutWidget)
        self.weight_g.setObjectName(u"weight_g")
        sizePolicy1.setHeightForWidth(self.weight_g.sizePolicy().hasHeightForWidth())
        self.weight_g.setSizePolicy(sizePolicy1)
        self.weight_g.setMinimumSize(QSize(0, 95))
        self.weight_g.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gridLayoutWidget_6 = QWidget(self.weight_g)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(0, 20, 301, 71))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.weightFile_browser = QTextBrowser(self.gridLayoutWidget_6)
        self.weightFile_browser.setObjectName(u"weightFile_browser")
        sizePolicy2.setHeightForWidth(self.weightFile_browser.sizePolicy().hasHeightForWidth())
        self.weightFile_browser.setSizePolicy(sizePolicy2)
        self.weightFile_browser.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_6.addWidget(self.weightFile_browser, 0, 0, 1, 1)

        self.browse_weights = QPushButton(self.gridLayoutWidget_6)
        self.browse_weights.setObjectName(u"browse_weights")
        self.browse_weights.setStyleSheet(u"color: rgb(0,0,0);")

        self.gridLayout_6.addWidget(self.browse_weights, 0, 1, 1, 1)

        self.export_check = QCheckBox(self.gridLayoutWidget_6)
        self.export_check.setObjectName(u"export_check")
        self.export_check.setEnabled(False)
        self.export_check.setStyleSheet(u"color: rgb(153, 153, 153);")

        self.gridLayout_6.addWidget(self.export_check, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.weight_g)

        self.start_b = QPushButton(Widget)
        self.start_b.setObjectName(u"start_b")
        self.start_b.setGeometry(QRect(460, 610, 70, 70))
        sizePolicy.setHeightForWidth(self.start_b.sizePolicy().hasHeightForWidth())
        self.start_b.setSizePolicy(sizePolicy)
        self.start_b.setMinimumSize(QSize(70, 50))
        icon = QIcon()
        icon.addFile(u":/button_icons/src/play_b.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_b.setIcon(icon)
        self.start_b.setIconSize(QSize(65, 65))
        self.stop_b = QPushButton(Widget)
        self.stop_b.setObjectName(u"stop_b")
        self.stop_b.setGeometry(QRect(380, 610, 70, 70))
        sizePolicy.setHeightForWidth(self.stop_b.sizePolicy().hasHeightForWidth())
        self.stop_b.setSizePolicy(sizePolicy)
        self.stop_b.setMinimumSize(QSize(70, 50))
        icon1 = QIcon()
        icon1.addFile(u":/button_icons/src/stop_b.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_b.setIcon(icon1)
        self.stop_b.setIconSize(QSize(65, 65))
        self.label_8 = QLabel(Widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 1280, 720))
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(320, 180))
        self.label_8.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label_9 = QLabel(Widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(370, 20, 851, 671))
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(320, 180))
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.copyright_l = QLabel(Widget)
        self.copyright_l.setObjectName(u"copyright_l")
        self.copyright_l.setGeometry(QRect(420, 700, 711, 16))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.copyright_l.setFont(font1)
        self.copyright_l.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.copyright_l.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget_2 = QWidget(Widget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(380, 30, 831, 621))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.seg_show = QLabel(self.gridLayoutWidget_2)
        self.seg_show.setObjectName(u"seg_show")
        sizePolicy.setHeightForWidth(self.seg_show.sizePolicy().hasHeightForWidth())
        self.seg_show.setSizePolicy(sizePolicy)
        self.seg_show.setMinimumSize(QSize(400, 225))
        self.seg_show.setStyleSheet(u"background-color: rgb(85, 255, 0);")

        self.gridLayout_2.addWidget(self.seg_show, 0, 2, 1, 2)

        self.det_show = QLabel(self.gridLayoutWidget_2)
        self.det_show.setObjectName(u"det_show")
        sizePolicy.setHeightForWidth(self.det_show.sizePolicy().hasHeightForWidth())
        self.det_show.setSizePolicy(sizePolicy)
        self.det_show.setMinimumSize(QSize(400, 225))
        self.det_show.setStyleSheet(u"background-color: rgb(0, 0, 255);")

        self.gridLayout_2.addWidget(self.det_show, 0, 0, 1, 2)

        self.joint_show = QLabel(self.gridLayoutWidget_2)
        self.joint_show.setObjectName(u"joint_show")
        sizePolicy.setHeightForWidth(self.joint_show.sizePolicy().hasHeightForWidth())
        self.joint_show.setSizePolicy(sizePolicy)
        self.joint_show.setMinimumSize(QSize(400, 225))
        self.joint_show.setStyleSheet(u"background-color: rgb(170, 0, 255)")

        self.gridLayout_2.addWidget(self.joint_show, 1, 1, 1, 2)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_8.addWidget(self.label_11, 1, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_8.addWidget(self.label_12, 2, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout_8, 1, 3, 1, 1)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(640, 610, 301, 16))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(850, 320, 301, 31))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(430, 330, 301, 16))
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_8.raise_()
        self.label_9.raise_()
        self.verticalLayoutWidget.raise_()
        self.start_b.raise_()
        self.stop_b.raise_()
        self.copyright_l.raise_()
        self.gridLayoutWidget_2.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.title_label.setText(QCoreApplication.translate("Widget", u"MultiHeadNet", None))
        self.input_g.setTitle(QCoreApplication.translate("Widget", u"Input Source", None))
        self.video_src.setText(QCoreApplication.translate("Widget", u"VideoFile", None))
        self.cam_src.setText(QCoreApplication.translate("Widget", u"WebCamera", None))
        self.scr_set.setText(QCoreApplication.translate("Widget", u"set", None))
        self.device_g.setTitle(QCoreApplication.translate("Widget", u"Processing Device", None))
        self.with_cuda.setText(QCoreApplication.translate("Widget", u"CUDA", None))
        self.with_cpu.setText(QCoreApplication.translate("Widget", u"CPU", None))
        self.score_g.setTitle(QCoreApplication.translate("Widget", u"Confidence Score", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"0.05", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"0.95", None))
        self.framework_g.setTitle(QCoreApplication.translate("Widget", u"Framework", None))
        self.with_trt.setText(QCoreApplication.translate("Widget", u"TensorRT", None))
        self.with_onnx.setText(QCoreApplication.translate("Widget", u"ONNX", None))
        self.with_torch.setText(QCoreApplication.translate("Widget", u"PyTorch", None))
        self.labelmap_g.setTitle(QCoreApplication.translate("Widget", u"Labelmap (.txt)", None))
        self.browse_labels.setText(QCoreApplication.translate("Widget", u"browse...", None))
        self.weight_g.setTitle(QCoreApplication.translate("Widget", u"Weights file (.pt, .onnx, .trt)", None))
        self.browse_weights.setText(QCoreApplication.translate("Widget", u"browse...", None))
        self.export_check.setText(QCoreApplication.translate("Widget", u"convert to selected framework (upcoming)", None))
        self.start_b.setText("")
        self.stop_b.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.copyright_l.setText(QCoreApplication.translate("Widget", u"Copyright \u00a9 2023 CVLab. All Rights Reserved.", None))
        self.seg_show.setText("")
        self.det_show.setText("")
        self.joint_show.setText("")
        self.label_10.setText(QCoreApplication.translate("Widget", u"Processing Time : ", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Frames Per Second :", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"pending...", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"pending...", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Statistics", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Joint Prediction", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Segmentation Prediction", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Detection Prediction", None))
    # retranslateUi

