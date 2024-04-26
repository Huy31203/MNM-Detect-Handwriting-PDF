from tkinter import messagebox
import cv2
import sys
import datetime
import numpy as np
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap, QImage
from PyQt6 import QtCore, QtWidgets
import requests
import convertGUI, cropGUI
from PIL import Image, ImageEnhance
import imghdr

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.mainWindow = MainWindow
        MainWindow.setFixedSize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(700, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.imageChoose = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageChoose.sizePolicy().hasHeightForWidth())
        self.imageChoose.setSizePolicy(sizePolicy)
        self.imageChoose.setMinimumSize(QtCore.QSize(100, 30))
        self.imageChoose.setObjectName("imageChoose")
        self.horizontalLayout.addWidget(self.imageChoose)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.imageCapture = QtWidgets.QPushButton(self.horizontalFrame, clicked = lambda: self.TakeImage())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageCapture.sizePolicy().hasHeightForWidth())
        self.imageCapture.setSizePolicy(sizePolicy)
        self.imageCapture.setMinimumSize(QtCore.QSize(100, 30))
        self.imageCapture.setObjectName("imageCapture")
        self.horizontalLayout.addWidget(self.imageCapture)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.downloadButton = QtWidgets.QPushButton(self.horizontalFrame, clicked=lambda: self.DownloadImage())
        self.downloadButton.setMinimumSize(QtCore.QSize(100, 30))
        self.downloadButton.setObjectName("downloadButton")
        self.horizontalLayout.addWidget(self.downloadButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.imageCrop = QtWidgets.QPushButton(self.horizontalFrame, clicked = lambda: self.open_crop_window(MainWindow))
        self.imageCrop.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy( QtWidgets.QSizePolicy.Policy.Preferred,  QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageCrop.sizePolicy().hasHeightForWidth())
        self.imageCrop.setSizePolicy(sizePolicy)
        self.imageCrop.setMinimumSize(QtCore.QSize(100, 30))
        self.imageCrop.setObjectName("imageCrop")
        self.horizontalLayout.addWidget(self.imageCrop)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.reset = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy( QtWidgets.QSizePolicy.Policy.Preferred,  QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset.sizePolicy().hasHeightForWidth())
        self.reset.setSizePolicy(sizePolicy)
        self.reset.setMinimumSize(QtCore.QSize(100, 30))
        self.reset.setObjectName("reset")
        self.horizontalLayout.addWidget(self.reset)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.language = QtWidgets.QComboBox(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy( QtWidgets.QSizePolicy.Policy.Preferred,  QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.language.sizePolicy().hasHeightForWidth())
        self.language.setSizePolicy(sizePolicy)
        self.language.setMinimumSize(QtCore.QSize(100, 30))
        self.language.setObjectName("language")
        self.language.addItem("")
        self.language.addItem("")
        self.language.addItem("")
        self.language.addItem("")
        self.language.addItem("")
        self.horizontalLayout.addWidget(self.language)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.begin = QtWidgets.QPushButton(self.horizontalFrame, clicked = lambda: self.open_convert_window())
        self.begin.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy( QtWidgets.QSizePolicy.Policy.Preferred,  QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.begin.sizePolicy().hasHeightForWidth())
        self.begin.setSizePolicy(sizePolicy)
        self.begin.setMinimumSize(QtCore.QSize(100, 30))
        self.begin.setObjectName("begin")
        self.horizontalLayout.addWidget(self.begin)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout.addWidget(self.horizontalFrame, 1, 0, 1, 1)
        self.horizontalFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalFrame = QtWidgets.QFrame(self.horizontalFrame_2)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.imageLabel = QtWidgets.QLabel(self.verticalFrame)
        self.imageLabel.setIndent(10)
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout_2.addWidget(self.imageLabel)
        self.imageContainer = QtWidgets.QLabel(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageContainer.sizePolicy().hasHeightForWidth())
        self.imageContainer.setSizePolicy(sizePolicy)
        self.imageContainer.setMinimumSize(QtCore.QSize(200, 200))
        self.imageContainer.setFrameStyle(2)
        self.imageContainer.setLineWidth(1)
        self.imageContainer.setMidLineWidth(1)
        self.imageContainer.setText("")
        self.imageContainer.setObjectName("imageContainer")
        self.verticalLayout_2.addWidget(self.imageContainer)
        self.horizontalLayout_3.addWidget(self.verticalFrame)
        self.verticalFrame_2 = QtWidgets.QFrame(self.horizontalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy( QtWidgets.QSizePolicy.Policy.Preferred,  QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame_2.sizePolicy().hasHeightForWidth())
        self.verticalFrame_2.setSizePolicy(sizePolicy)
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.brightnessSlider = QtWidgets.QSlider(self.verticalFrame_2)
        self.brightnessSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.brightnessSlider.setObjectName("brightnessSlider")
        self.brightnessSlider.setRange(-100, 100)
        self.brightnessSlider.setValue(0)
        self.brightnessSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.brightnessSlider.setTickInterval(10)
        self.brightnessSlider.setEnabled(False)
        self.horizontalLayout_7.addWidget(self.brightnessSlider)
        self.brightnessLabel = QtWidgets.QLabel(self.verticalFrame_2)
        self.brightnessLabel.setObjectName("brightnessLabel")
        self.horizontalLayout_7.addWidget(self.brightnessLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sharpnessSlider = QtWidgets.QSlider(self.verticalFrame_2)
        self.sharpnessSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sharpnessSlider.setObjectName("sharpnessSlider")
        self.sharpnessSlider.setRange(-100, 100)
        self.sharpnessSlider.setValue(0)
        self.sharpnessSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.sharpnessSlider.setTickInterval(10)
        self.sharpnessSlider.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.sharpnessSlider)
        self.sharpnessLabel = QtWidgets.QLabel(self.verticalFrame_2)
        self.sharpnessLabel.setObjectName("sharpnessLabel")
        self.horizontalLayout_5.addWidget(self.sharpnessLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.contrastSlider = QtWidgets.QSlider(self.verticalFrame_2)
        self.contrastSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.contrastSlider.setObjectName("contrastSlider")
        self.contrastSlider.setRange(-100, 100)
        self.contrastSlider.setValue(0)
        self.contrastSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.contrastSlider.setTickInterval(10)
        self.contrastSlider.setEnabled(False)
        self.horizontalLayout_6.addWidget(self.contrastSlider)
        self.contrastLabel = QtWidgets.QLabel(self.verticalFrame_2)
        self.contrastLabel.setObjectName("contrastLabel")
        self.horizontalLayout_6.addWidget(self.contrastLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addWidget(self.verticalFrame_2)
        self.gridLayout.addWidget(self.horizontalFrame_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.brightnessLabel.setBuddy(self.brightnessSlider)
        self.sharpnessLabel.setBuddy(self.sharpnessSlider)
        self.contrastLabel.setBuddy(self.contrastSlider)
        self.filename = ''
        self.imageSize = []
        self.preBright = 0
        self.preSharp = 0
        self.preContrast = 0

        self.imageChoose.clicked.connect(self.openFileDialog)
        self.reset.clicked.connect(self.resetParams)
        # self.begin.clicked.connect(self.open_convert_window)
        self.brightnessSlider.valueChanged.connect(self.update_image_brightness)
        self.contrastSlider.valueChanged.connect(self.update_image_contrast)
        self.sharpnessSlider.valueChanged.connect(self.update_image_sharpness)

        self.retranslateUi(self.mainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def DownloadImage(self):
        url, ok = QtWidgets.QInputDialog.getText(self.mainWindow, "Download Image", "Enter the image URL:")
        if ok:
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an HTTPError for bad responses
            except requests.RequestException as e:
                QtWidgets.QMessageBox.warning(self.mainWindow, "Error", f"Tải hình ảnh thất bại: {str(e)}")
                return
            
            if response.status_code == 200:
                content_type = response.headers.get('Content-Type')
                if 'image' in content_type:
                    img_data = response.content
                    filename = 'temp/temp.jpg'
                    with open(filename, 'wb') as f:
                        f.write(img_data)
                        self.pixmap = QPixmap(filename)
                        self.cv2_image = cv2.imread(filename)
                        self.cv2_image_tmp = self.cv2_image
                        self.setImage()
                        self.filename = filename
                        self.brightnessSlider.setEnabled(True)
                        self.sharpnessSlider.setEnabled(True)
                        self.contrastSlider.setEnabled(True)
                        self.begin.setEnabled(True)
                        self.imageCrop.setEnabled(True)
                        self.preBright = 0
                        self.preSharp = 0
                        self.preContrast = 0
                        self.brightnessSlider.setValue(0)
                        self.sharpnessSlider.setValue(0)
                        self.contrastSlider.setValue(0)
                        
    def setImage(self):
        if self.pixmap.width() <= 460:
            if self.pixmap.width() <= 445:
                self.imageContainer.setPixmap(self.pixmap)
            else: 
                self.imageContainer.setPixmap(self.pixmap.scaled(self.pixmap.width(), 445))
        else:
            if self.pixmap.height() <= 445:
                self.imageContainer.setPixmap(self.pixmap.scaled(460, self.pixmap.height()))
            else:
                self.imageContainer.setPixmap(self.pixmap.scaled(460, 445))

    def openFileDialog(self):
        filename, _ = QFileDialog.getOpenFileName(self.imageChoose, "Chọn hình ảnh", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if filename:
            self.pixmap = QPixmap(filename)
            self.cv2_image = cv2.imread(filename)
            self.cv2_image_tmp = self.cv2_image
            self.setImage()
            self.filename = filename
            self.brightnessSlider.setEnabled(True)
            self.sharpnessSlider.setEnabled(True)
            self.contrastSlider.setEnabled(True)
            self.begin.setEnabled(True)
            self.imageCrop.setEnabled(True)
            self.preBright = 0
            self.preSharp = 0
            self.preContrast = 0
            self.brightnessSlider.setValue(0)
            self.sharpnessSlider.setValue(0)
            self.contrastSlider.setValue(0)
        
    def TakeImage(self):
        # Access the camera
        cap = cv2.VideoCapture(0)

        # Check if the camera is opened successfully
        if not cap.isOpened():
            print("Unable to access camera")
            return

        width = 600
        height = 600
        
        # Read a frame from the camera
        while True:
            ret, frame = cap.read()
            
            frame = cv2.resize(frame, (width, height))
            
            # Display the captured frame
            cv2.imshow("Camera", frame)
            
            if cv2.waitKey(1) == ord('\x1b'): #Esc button
                cv2.destroyAllWindows()
                return
            
            if cv2.waitKey(1) == ord(' '):
                break
        cap.release()
        cv2.destroyAllWindows()
        self.cv2_image = frame
        self.cv2_image_tmp = frame
        now = datetime.datetime.now()
        filename = 'Images/Capture'+ now.strftime("%Y%m%d%H%M%S") + ".jpg"
        cv2.imwrite(filename, frame)
        self.pixmap = QPixmap(filename)
        self.setImage()
        self.filename = filename
        self.brightnessSlider.setEnabled(True)
        self.sharpnessSlider.setEnabled(True)
        self.contrastSlider.setEnabled(True)
        self.begin.setEnabled(True)
        self.imageCrop.setEnabled(True)
        self.preBright = 0
        self.preSharp = 0
        self.preContrast = 0
        self.brightnessSlider.setValue(0)
        self.sharpnessSlider.setValue(0)
        self.contrastSlider.setValue(0)
    
    def customize_image(self):
        pillow_image = Image.fromarray(self.cv2_image_tmp)

        # Thực hiện tăng độ sáng
        brightness_value_normalized = self.brightnessSlider.value()
        brightened_image = ImageEnhance.Brightness(pillow_image).enhance((brightness_value_normalized + 100) / 100)

        # Thực hiện tăng độ sắc nét
        sharpness_value_normalized = self.sharpnessSlider.value()
        image = np.array(brightened_image)
        sharpened_image = cv2.convertScaleAbs(image, alpha=1 + sharpness_value_normalized/100, beta=0)
        
        # Thực hiện tăng độ tương phản
        contrast_value_normalized = self.contrastSlider.value()
        sharpened_image = Image.fromarray(sharpened_image)
        contrastened_image = ImageEnhance.Contrast(sharpened_image).enhance((contrast_value_normalized + 100) / 100)

        image = np.array(contrastened_image)

        return image
        
    def update_image_brightness(self):
        image = self.customize_image()
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image = np.array(image)
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)

        # Display the QImage using QPixmap
        q_pixmap = QPixmap.fromImage(q_image)
        self.cv2_image = image
        self.pixmap = q_pixmap
        self.setImage()
            
    def update_image_contrast(self):
        image = self.customize_image()
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image = np.array(image)
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)

        # Display the QImage using QPixmap
        q_pixmap = QPixmap.fromImage(q_image)
        self.cv2_image = image
        self.pixmap = q_pixmap
        self.setImage()
    
    def update_image_sharpness(self):
        image = self.customize_image()
        
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image = np.array(image)
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)

        # Display the QImage using QPixmap
        q_pixmap = QPixmap.fromImage(q_image)
        self.cv2_image = image
        self.pixmap = q_pixmap
        self.setImage()
    
    def resetParams(self):
        self.pixmap = QPixmap(self.filename)
        self.cv2_image = cv2.imread(self.filename)
        self.preSharp = 0
        self.preContrast = 0
        self.brightnessSlider.setValue(0)
        self.sharpnessSlider.setValue(0)
        self.contrastSlider.setValue(0)
        self.setImage()
    
    def open_convert_window(self):
        self.window = QtWidgets.QWidget()
        self.convertWindow = convertGUI.Ui_Form()
        self.convertWindow.setupUi(self.window)
        self.convertWindow.language = self.language.currentIndex()
        self.window.show()
        self.convertWindow.Image(self.cv2_image)
        
    def open_crop_window(self, MainWindow):
        self.window = QtWidgets.QWidget()
        self.convertWindow = cropGUI.Ui_Form()
        self.convertWindow.setupUi(self.window)
        self.convertWindow.Image(self.cv2_image, self.filename)
        self.window.show()
        MainWindow.close()
        
    def receiveImg(self):
        self.filename = 'temp/temp.jpg'
        self.pixmap = QPixmap(self.filename)
        self.cv2_image = cv2.imread(self.filename)
        self.cv2_image_tmp = self.cv2_image
        self.setImage()
        self.brightnessSlider.setEnabled(True)
        self.sharpnessSlider.setEnabled(True)
        self.contrastSlider.setEnabled(True)
        self.begin.setEnabled(True)
        self.imageCrop.setEnabled(True)
        self.preBright = 0
        self.preSharp = 0
        self.preContrast = 0
        self.brightnessSlider.setValue(0)
        self.sharpnessSlider.setValue(0)
        self.contrastSlider.setValue(0)
        
    def reOpenMain(self, filename):
        self.filename = filename
        self.pixmap = QPixmap(filename)
        self.cv2_image = cv2.imread(filename)
        self.setImage()
        self.brightnessSlider.setEnabled(True)
        self.sharpnessSlider.setEnabled(True)
        self.contrastSlider.setEnabled(True)
        self.begin.setEnabled(True)
        self.imageCrop.setEnabled(True)
        self.preBright = 0
        self.preSharp = 0
        self.preContrast = 0
        self.brightnessSlider.setValue(0)
        self.sharpnessSlider.setValue(0)
        self.contrastSlider.setValue(0)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image to PDF"))
        self.imageChoose.setText(_translate("MainWindow", "Chọn ảnh"))
        self.downloadButton.setText(_translate("MainWindow", "URL"))
        self.imageCapture.setText(_translate("MainWindow", "Chụp ảnh"))
        self.imageCrop.setText(_translate("MainWindow", "Cắt ảnh"))
        self.reset.setText(_translate("MainWindow", "Reset"))
        self.language.setItemText(0, _translate("MainWindow", "Tiếng Việt"))
        self.language.setItemText(1, _translate("MainWindow", "Tiếng Anh"))
        self.language.setItemText(2, _translate("MainWindow", "Tiếng Pháp"))
        self.language.setItemText(3, _translate("MainWindow", "Tiếng Ý"))
        self.language.setItemText(4, _translate("MainWindow", "Tiếng Tây Ban Nha"))
        self.begin.setText(_translate("MainWindow", "Bắt đầu"))
        self.imageLabel.setText(_translate("MainWindow", "Image"))
        self.brightnessLabel.setText(_translate("MainWindow", "Brightness"))
        self.sharpnessLabel.setText(_translate("MainWindow", "Sharpness"))
        self.contrastLabel.setText(_translate("MainWindow", "Contrast"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
