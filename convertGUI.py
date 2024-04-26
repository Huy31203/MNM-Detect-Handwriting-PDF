import cv2
import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QMessageBox, QSizePolicy, QFrame, QMessageBox
from PyQt6.QtGui import QPixmap, QColor, QImage
from PyQt6 import QtCore, QtGui, QtWidgets
import segmentation as sg
import HandleDetect as detect
import toPDF

class Ui_Form(object):
    def setupUi(self, Form):
        self.language = 0
        Form.setObjectName("Form")
        Form.setFixedSize(818, 524)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalFrame = QtWidgets.QFrame(Form)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(800, 400))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_2 = QtWidgets.QFrame(self.horizontalFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.imageContainer = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageContainer.sizePolicy().hasHeightForWidth())
        self.imageContainer.setSizePolicy(sizePolicy)
        self.imageContainer.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.imageContainer.setText("")
        self.imageContainer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.imageContainer.setIndent(0)
        self.imageContainer.setObjectName("imageContainer")
        self.horizontalLayout_18.addWidget(self.imageContainer)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.textPreview = QtWidgets.QTextEdit(self.frame_2)
        self.textPreview.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.textPreview.setFont(font)
        self.textPreview.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textPreview.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textPreview.setObjectName("textPreview")
        self.gridLayout_7.addWidget(self.textPreview, 0, 2, 1, 1)
        self.horizontalLayout_18.addLayout(self.gridLayout_7)
        self.horizontalLayout_14.addWidget(self.frame_2)
        self.gridLayout_2.addWidget(self.horizontalFrame, 0, 0, 1, 1)
        self.verticalFrame = QtWidgets.QFrame(Form)
        self.verticalFrame.setMinimumSize(QtCore.QSize(0, 100))
        self.verticalFrame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.processBar = QtWidgets.QProgressBar(self.verticalFrame);
        self.processBar.setProperty("value", 0)
        self.processBar.setObjectName("processBar")
        self.verticalLayout_9.addWidget(self.processBar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem2)
        self.cancel = QtWidgets.QPushButton(self.verticalFrame)
        self.cancel.setMinimumSize(QtCore.QSize(100, 30))
        self.cancel.setObjectName("cancel")
        self.cancel.clicked.connect(lambda: self.cancelConvert(Form))
        self.horizontalLayout_21.addWidget(self.cancel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem3)
        self.covert = QtWidgets.QPushButton(self.verticalFrame)
        self.covert.setMinimumSize(QtCore.QSize(100, 30))
        self.covert.setObjectName("covert")
        self.covert.clicked.connect(self.createPDF)  # Connect the clicked signal here
        self.horizontalLayout_21.addWidget(self.covert)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_21)
        self.gridLayout_2.addWidget(self.verticalFrame, 2, 0, 1, 1)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def setImage(self):
        if self.pixmap.width() <= 372:
            if self.pixmap.width() <= 360:
                self.imageContainer.setPixmap(self.pixmap)
            else: 
                self.imageContainer.setPixmap(self.pixmap.scaled(self.pixmap.width(), 360))
        else:
            if self.pixmap.height() <= 360:
                self.imageContainer.setPixmap(self.pixmap.scaled(372, self.pixmap.height()))
            else:
                self.imageContainer.setPixmap(self.pixmap.scaled(372, 360))

    def Image(self, image):
        self.image = image
        image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        height, width, channel = image_rgb.shape
        bytesPerLine = channel * width
        qImg = QImage(image_rgb.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        self.pixmap = QPixmap.fromImage(qImg)
        self.setImage()
        msg = QMessageBox()
        msg.setWindowTitle("Thông báo")
        msg.setText("Bắt đầu chuyển đổi?")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
        self.processBar.setProperty("value", 20)
        self.Convert()
        
    def Convert(self):
        segments = sg.line_segmentation(self.image)
        self.processBar.setProperty("value", 50)
        self.reg_image = segments[0]
        segments.pop(0)
        
        height, width, channel = self.reg_image.shape
        bytesPerLine = channel * width
        qImg = QImage(self.reg_image.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        self.pixmap = QPixmap.fromImage(qImg)
        self.setImage()
        
        self.processBar.setProperty("value", 60)
        text = ""
        match self.language:
            case 0:
                text = detect.convertToString(segments)
            case 1:
                text = detect.convertToString(segments, "en_US")
            case 2:
                text = detect.convertToString(segments, "fr_FR")
            case 3:
                text = detect.convertToString(segments, "it_IT")
            case 4:
                text = detect.convertToString(segments, "es_ES")
        self.processBar.setProperty("value", 100)
        
        self.textPreview.setText(str(text))
        self.textPreview.setEnabled(True)
    
    def createPDF(self):
        self.text = self.textPreview.toPlainText()
        toPDF.convertToPdf(self.text, cv2.cvtColor(self.reg_image, cv2.COLOR_BGR2RGB))
        
    
    def cancelConvert(self, Form):
        Form.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PDF Converter"))
        self.cancel.setText(_translate("Form", "Huỷ"))
        self.covert.setText(_translate("Form", "Chuyển đổi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())