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
        self.imageCapture = QtWidgets.QPushButton(self.horizontalFrame, clicked = lambda: self.TakeImage()) # type: ignore
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
        self.downloadButton = QtWidgets.QPushButton(self.horizontalFrame, clicked=lambda: self.DownloadImage()) # type: ignore
        self.downloadButton.setMinimumSize(QtCore.QSize(100, 30))
        self.downloadButton.setObjectName("downloadButton")
        self.horizontalLayout.addWidget(self.downloadButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.imageCrop = QtWidgets.QPushButton(self.horizontalFrame, clicked = lambda: self.open_crop_window(MainWindow)) # type: ignore
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
        self.begin = QtWidgets.QPushButton(self.horizontalFrame, clicked = lambda: self.open_convert_window()) # type: ignore
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
        # Hiển thị hộp thoại để nhập URL của hình ảnh cần tải
        url, ok = QtWidgets.QInputDialog.getText(self.mainWindow, "Download Image", "Nhập đường dẫn hình ảnh:")
        if ok:
            try:
                # Thử tải hình ảnh từ URL
                response = requests.get(url)
                response.raise_for_status()  # Nếu có lỗi, ném ra ngoại lệ
            except requests.RequestException as e:
                # Hiển thị thông báo lỗi nếu không tải được hình
                QtWidgets.QMessageBox.warning(self.mainWindow, "Error", f"Tải hình ảnh thất bại: {str(e)}")
                return
            
            # Kiểm tra nếu mã trạng thái HTTP là 200 (thành công)
            if response.status_code == 200:
                # Lấy kiểu nội dung của phản hồi, kiểm tra nếu là hình ảnh
                content_type = response.headers.get('Content-Type')
                if 'image' in content_type: # type: ignore
                    img_data = response.content
                    filename = 'temp/temp.jpg'
                    with open(filename, 'wb') as f:
                        f.write(img_data)
                        # Tạo QPixmap từ file vừa tải
                        self.pixmap = QPixmap(filename)
                        # Đọc hình ảnh sử dụng OpenCV
                        self.cv2_image = cv2.imread(filename)
                        self.cv2_image_tmp = self.cv2_image
                        # Cập nhật hình ảnh lên giao diện
                        self.setImage()
                        self.filename = filename
                        # Kích hoạt các thanh trượt và nút nhấn
                        self.brightnessSlider.setEnabled(True)
                        self.sharpnessSlider.setEnabled(True)
                        self.contrastSlider.setEnabled(True)
                        self.begin.setEnabled(True)
                        self.imageCrop.setEnabled(True)
                        # Đặt giá trị ban đầu cho các thanh trượt
                        self.brightnessSlider.setValue(0)
                        self.sharpnessSlider.setValue(0)
                        self.contrastSlider.setValue(0)

    def setImage(self):
        # Kiểm tra chiều rộng của pixmap để xác định cách hiển thị
        if self.pixmap.width() <= 460:
            # Nếu chiều rộng nhỏ hơn hoặc bằng 445, hiển thị pixmap gốc
            if self.pixmap.width() <= 445:
                self.imageContainer.setPixmap(self.pixmap)
            # Nếu chiều rộng lớn hơn 445 nhưng nhỏ hơn 460, thu nhỏ theo chiều cao 445
            else: 
                self.imageContainer.setPixmap(self.pixmap.scaled(self.pixmap.width(), 445))
        # Nếu chiều rộng lớn hơn 460
        else:
            # Nếu chiều cao nhỏ hơn hoặc bằng 445, thu nhỏ theo chiều rộng 460
            if self.pixmap.height() <= 445:
                self.imageContainer.setPixmap(self.pixmap.scaled(460, self.pixmap.height()))
            # Nếu cả chiều rộng và chiều cao lớn hơn 445, thu nhỏ về 460x445
            else:
                self.imageContainer.setPixmap(self.pixmap.scaled(460, 445))

    def openFileDialog(self):
        # Mở hộp thoại chọn file và lấy đường dẫn của file hình ảnh được chọn
        filename, _ = QFileDialog.getOpenFileName(self.imageChoose, "Chọn hình ảnh", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if filename:
            # Tạo QPixmap từ file được chọn
            self.pixmap = QPixmap(filename)
            # Đọc hình ảnh sử dụng OpenCV
            self.cv2_image = cv2.imread(filename)
            self.cv2_image_tmp = self.cv2_image
            # Cập nhật hình ảnh lên giao diện
            self.setImage()
            self.filename = filename
            # Kích hoạt các thanh trượt và nút nhấn
            self.brightnessSlider.setEnabled(True)
            self.sharpnessSlider.setEnabled(True)
            self.contrastSlider.setEnabled(True)
            self.begin.setEnabled(True)
            self.imageCrop.setEnabled(True)
            # Đặt giá trị ban đầu cho các thanh trượt
            self.brightnessSlider.setValue(0)
            self.sharpnessSlider.setValue(0)
            self.contrastSlider.setValue(0)

    def TakeImage(self):
        # Khởi tạo camera
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Unable to access camera")
            return

        width = 600
        height = 600
        
        while True:
            ret, frame = cap.read()
            
            # Điều chỉnh kích thước khung hình
            frame = cv2.resize(frame, (width, height))
            
            # Hiển thị khung hình trên cửa sổ
            cv2.imshow("Camera", frame)
            
            # Thoát khi nhấn phím Esc
            if cv2.waitKey(1) == ord('\x1b'): #Esc button
                cv2.destroyAllWindows()
                return
            
            # Chụp ảnh khi nhấn phím Space
            if cv2.waitKey(1) == ord(' '):
                break
            # Đóng cửa sổ khi cửa sổ không còn hiển thị
            if cv2.getWindowProperty("Camera", cv2.WND_PROP_VISIBLE) < 1:
                cv2.destroyAllWindows()
                return
        
        cap.release()
        cv2.destroyAllWindows()
        # Lưu hình ảnh đã chụp
        self.cv2_image = frame
        self.cv2_image_tmp = frame
        now = datetime.datetime.now()
        filename = 'Images/Capture'+ now.strftime("%Y%m%d%H%M%S") + ".jpg"
        cv2.imwrite(filename, frame)
        self.pixmap = QPixmap(filename)
        # Cập nhật hình ảnh lên giao diện
        self.setImage()
        self.filename = filename
        # Kích hoạt các thanh trượt và nút nhấn
        self.brightnessSlider.setEnabled(True)
        self.sharpnessSlider.setEnabled(True)
        self.contrastSlider.setEnabled(True)
        self.begin.setEnabled(True)
        self.imageCrop.setEnabled(True)
        # Đặt giá trị ban đầu cho các thanh trượt
        self.brightnessSlider.setValue(0)
        self.sharpnessSlider.setValue(0)
        self.contrastSlider.setValue(0)
    
    def customize_image(self):
        # Chuyển đổi hình ảnh từ OpenCV sang Pillow để thực hiện tăng giảm độ sáng
        pillow_image = Image.fromarray(self.cv2_image_tmp)

        # Lấy giá trị từ thanh trượt độ sáng và điều chỉnh độ sáng của hình ảnh
        brightness_value_normalized = self.brightnessSlider.value()
        brightened_image = ImageEnhance.Brightness(pillow_image).enhance((brightness_value_normalized + 100) / 100)

        # Lấy giá trị từ thanh trượt độ nét và điều chỉnh độ nét của hình ảnh
        sharpness_value_normalized = self.sharpnessSlider.value()
        image = np.array(brightened_image)
        sharpened_image = cv2.convertScaleAbs(image, alpha=1 + sharpness_value_normalized/100, beta=0)
        
        # Lấy giá trị từ thanh trượt độ tương phản và điều chỉnh độ tương phản của hình ảnh
        contrast_value_normalized = self.contrastSlider.value()
        sharpened_image = Image.fromarray(sharpened_image)
        contrastened_image = ImageEnhance.Contrast(sharpened_image).enhance((contrast_value_normalized + 100) / 100)

        # Chuyển đổi hình ảnh cuối cùng trở lại dạng mảng numpy để xử lý tiếp
        image = np.array(contrastened_image)

        return image
        
    def update_image_brightness(self):
        # Tạo hình ảnh đã tùy chỉnh từ các thanh trượt
        image = self.customize_image()
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        # Chuyển đổi hình ảnh từ RGB sang BGR để hiển thị đúng màu
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image = np.array(image)
        # Tạo QImage từ dữ liệu hình ảnh
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)

        # Hiển thị QImage sử dụng QPixmap
        q_pixmap = QPixmap.fromImage(q_image)
        self.cv2_image = image
        self.pixmap = q_pixmap
        # Cập nhật hình ảnh trên giao diện người dùng
        self.setImage()
            
    def update_image_contrast(self):
        # Tạo hình ảnh đã tùy chỉnh dựa trên các giá trị từ thanh trượt
        image = self.customize_image()
        # Lấy kích thước và số kênh màu của hình ảnh
        height, width, channel = image.shape
        # Tính số byte trên mỗi dòng
        bytes_per_line = 3 * width
        # Chuyển đổi hình ảnh từ RGB sang BGR để hiển thị đúng màu sắc
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # Chuyển đổi mảng numpy thành QImage
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)

        # Tạo QPixmap từ QImage để hiển thị trên GUI
        q_pixmap = QPixmap.fromImage(q_image)
        # Cập nhật hình ảnh hiện tại và pixmap để hiển thị
        self.cv2_image = image
        self.pixmap = q_pixmap
        # Cập nhật hình ảnh trên giao diện người dùng
        self.setImage()
    
    def update_image_sharpness(self):
        # Tạo hình ảnh đã tùy chỉnh từ các thanh trượt
        image = self.customize_image()
        # Lấy kích thước và số kênh màu của hình ảnh
        height, width, channel = image.shape
        # Tính số byte trên mỗi dòng
        bytes_per_line = 3 * width
        # Chuyển đổi hình ảnh từ RGB sang BGR để hiển thị đúng màu
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # Chuyển đổi mảng numpy thành QImage
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)

        # Tạo QPixmap từ QImage để hiển thị trên GUI
        q_pixmap = QPixmap.fromImage(q_image)
        # Cập nhật hình ảnh hiện tại và pixmap để hiển thị
        self.cv2_image = image
        self.pixmap = q_pixmap
        # Cập nhật hình ảnh trên giao diện người dùng
        self.setImage()
    
    def resetParams(self):
        # Load lại hình ảnh gốc từ đường dẫn lưu trữ
        self.pixmap = QPixmap(self.filename)
        # Đọc lại hình ảnh gốc sử dụng OpenCV
        self.cv2_image = cv2.imread(self.filename)
        # Đặt lại giá trị của các thanh trượt về 0
        self.brightnessSlider.setValue(0)
        self.sharpnessSlider.setValue(0)
        self.contrastSlider.setValue(0)
        # Cập nhật lại hình ảnh trên giao diện người dùng
        self.setImage()
    
    def open_convert_window(self):
        # Tạo một cửa sổ mới cho việc chuyển đổi hình ảnh
        self.window = QtWidgets.QWidget()
        
        # Khởi tạo giao diện người dùng cho cửa sổ chuyển đổi
        self.convertWindow = convertGUI.Ui_Form()
        self.convertWindow.setupUi(self.window)
        
        # Chuyển ngôn ngữ hiện tại được chọn sang cửa sổ chuyển đổi
        self.convertWindow.language = self.language.currentIndex()
        
        # Hiển thị cửa sổ chuyển đổi
        self.window.show()
        
        # Gửi hình ảnh hiện tại đến cửa sổ chuyển đổi để xử lý
        self.convertWindow.Image(self.cv2_image)
        
    def open_crop_window(self, MainWindow):
        # Tạo một widget mới để hiển thị cửa sổ cắt ảnh
        self.window = QtWidgets.QWidget()
        
        # Khởi tạo giao diện người dùng cho cửa sổ cắt ảnh từ module cropGUI
        self.convertWindow = cropGUI.Ui_Form()
        self.convertWindow.setupUi(self.window)
        
        # Gửi hình ảnh hiện tại và tên file đến cửa sổ cắt để xử lý
        self.convertWindow.Image(self.cv2_image, self.filename)
        
        # Hiển thị cửa sổ cắt ảnh
        self.window.show()
        
        # Đóng cửa sổ chính hiện tại
        MainWindow.close()
        
    def receiveImg(self):
        # Đặt tên file mặc định cho hình ảnh nhận được
        self.filename = 'temp/temp.jpg'
        
        # Tạo QPixmap từ file hình ảnh
        self.pixmap = QPixmap(self.filename)
        
        # Đọc hình ảnh sử dụng OpenCV
        self.cv2_image = cv2.imread(self.filename)
        self.cv2_image_tmp = self.cv2_image  # Lưu trữ hình ảnh tạm thời để xử lý
        
        # Cập nhật hình ảnh lên giao diện người dùng
        self.setImage()
        
        # Kích hoạt các thanh trượt và nút nhấn
        self.brightnessSlider.setEnabled(True)
        self.sharpnessSlider.setEnabled(True)
        self.contrastSlider.setEnabled(True)
        self.begin.setEnabled(True)
        self.imageCrop.setEnabled(True)
        
        # Đặt giá trị ban đầu cho các thanh trượt về 0
        self.brightnessSlider.setValue(0)
        self.sharpnessSlider.setValue(0)
        self.contrastSlider.setValue(0)
        
    def reOpenMain(self, filename):
        # Cập nhật tên file hiện tại
        self.filename = filename
        
        # Tạo QPixmap từ file hình ảnh
        self.pixmap = QPixmap(filename)
        
        # Đọc hình ảnh sử dụng OpenCV
        self.cv2_image = cv2.imread(filename)
        
        # Cập nhật hình ảnh lên giao diện người dùng
        self.setImage()
        
        # Kích hoạt các thanh trượt và nút nhấn
        self.brightnessSlider.setEnabled(True)
        self.sharpnessSlider.setEnabled(True)
        self.contrastSlider.setEnabled(True)
        self.begin.setEnabled(True)
        self.imageCrop.setEnabled(True)
        
        # Đặt giá trị ban đầu cho các thanh trượt về 0
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
