import sys
import cv2
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QImage, QPainter, QColor, QPen, QCursor
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QGraphicsRectItem
from PyQt6.QtCore import Qt, QPoint, QRect, QSize
import mainGUI

# Lớp ImageLabel được sử dụng để tạo ra một nhãn hình ảnh có thể vẽ hình chữ nhật bằng cách kéo chuột.
class ImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.drag_start = None  # Điểm bắt đầu kéo
        self.drag_end = None  # Điểm kết thúc kéo
        self.rect = None  # type: ignore
        self.draw_rect_pen = QPen(QColor("red"))  # Bút vẽ hình chữ nhật
        self.draw_rect_pen.setWidth(1)  # Độ rộng của bút vẽ

    def mousePressEvent(self, event):
        # Khi nhấn chuột trái
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start = event.pos()  # Lưu vị trí bắt đầu kéo
            self.rect = QRect(self.drag_start, QSize())  # type: ignore
            self.setCursor(QCursor(Qt.CursorShape.CrossCursor))  # Thay đổi con trỏ chuột
        self.update()  # Cập nhật giao diện

    def mouseMoveEvent(self, event):
        # Khi di chuyển chuột
        if self.drag_start is not None:
            self.drag_end = event.pos()  # Lưu vị trí kết thúc kéo
        self.update()  # Cập nhật giao diện

    def mouseReleaseEvent(self, event):
        # Khi thả chuột trái
        if event.button() == Qt.MouseButton.LeftButton:
            self.rect = QRect(self.drag_start, event.pos()).normalized()  # type: ignore
            self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))  # Thay đổi con trỏ chuột
        self.update()  # Cập nhật giao diện

    def paintEvent(self, event):
        # Khi vẽ giao diện
        super().paintEvent(event)
        painter = QPainter(self)  # Tạo đối tượng vẽ
        painter.setPen(QPen(QColor(255, 0, 0), 1, Qt.PenStyle.SolidLine))  # Thiết lập bút vẽ
        if self.drag_start and self.drag_end:
            # Vẽ hình chữ nhật nếu có điểm bắt đầu và kết thúc kéo
            painter.drawRect(QRect(self.drag_start, self.drag_end).normalized())

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(818, 626)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        
        self.imageLabel = ImageLabel(Form)
        self.gridLayout.addWidget(self.imageLabel, 0, 0, 1, 1)
        
        self.horizontalFrame = QtWidgets.QFrame(Form)
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel = QtWidgets.QPushButton(self.horizontalFrame, clicked = lambda: self.cancelCrop(Form)) # type: ignore
        self.cancel.setMinimumSize(QtCore.QSize(100, 40))
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.crop = QtWidgets.QPushButton(self.horizontalFrame, clicked = lambda: self.cropImage(Form)) # type: ignore
        self.crop.setMinimumSize(QtCore.QSize(100, 40))
        self.crop.setObjectName("crop")
        self.horizontalLayout.addWidget(self.crop)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addWidget(self.horizontalFrame, 1, 0, 1, 1)
        self.image = QPixmap("Images/Sample7.jpg")
        self.imageLabel.setPixmap(self.image.scaled(790, 540))
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def cropImage(self, Form):
        # Nếu đã kéo chuột để chọn vùng
        if self.imageLabel.drag_start is not None:
            # Lấy tọa độ x, y nhỏ nhất và lớn nhất từ vùng đã chọn
            x1 = min(self.imageLabel.drag_start.x(), self.imageLabel.drag_end.x()) # type: ignore
            y1 = min(self.imageLabel.drag_start.y(), self.imageLabel.drag_end.y()) # type: ignore
            x2 = max(self.imageLabel.drag_start.x(), self.imageLabel.drag_end.x()) # type: ignore
            y2 = max(self.imageLabel.drag_start.y(), self.imageLabel.drag_end.y()) # type: ignore

            # Thay đổi kích thước hình ảnh gốc để phù hợp với kích thước hiển thị
            img = cv2.resize(self.image, (790, 540), interpolation = cv2.INTER_AREA) # type: ignore

            # Cắt hình ảnh theo vùng đã chọn
            self.cropped_image = img[y1:y2, x1:x2]

            # Lưu hình ảnh đã cắt vào thư mục temp
            cv2.imwrite("temp/temp.jpg", self.cropped_image)

            # Tạo cửa sổ mới
            MainWindow = QtWidgets.QMainWindow()

            # Tạo giao diện cho cửa sổ mới
            self.mainWindow = mainGUI.Ui_MainWindow()
            self.mainWindow.setupUi(MainWindow)

            # Nhận hình ảnh đã cắt
            self.mainWindow.receiveImg()

            # Hiển thị cửa sổ mới
            MainWindow.show()

            # Đóng cửa sổ hiện tại
            Form.close()            
            
    def Image(self, image, filename):
        self.image = image  # Lưu hình ảnh vào thuộc tính self.image
        self.filename = filename  # Lưu tên file vào thuộc tính self.filename

        # Chuyển hình ảnh từ không gian màu RGB sang BGR
        image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Lấy kích thước và số kênh màu của hình ảnh
        height, width, channel = image_rgb.shape

        # Tính số byte trên mỗi dòng của hình ảnh
        bytesPerLine = channel * width

        # Tạo một đối tượng QImage từ dữ liệu hình ảnh
        qImg = QImage(image_rgb.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)

        # Tạo một đối tượng QPixmap từ đối tượng QImage
        self.pixmap = QPixmap.fromImage(qImg)

        # Đặt hình ảnh cho nhãn và thay đổi kích thước hình ảnh để phù hợp với kích thước nhãn
        self.imageLabel.setPixmap(self.pixmap.scaled(790, 540))
        
    def cancelCrop(self, Form):
        # Tạo cửa sổ mới
        MainWindow = QtWidgets.QMainWindow()

        # Tạo giao diện cho cửa sổ mới
        self.mainWindow = mainGUI.Ui_MainWindow()
        self.mainWindow.setupUi(MainWindow)

        # Mở lại cửa sổ chính với tên file hình ảnh gốc
        self.mainWindow.reOpenMain(self.filename)

        # Hiển thị cửa sổ mới
        MainWindow.show()

        # Đóng cửa sổ hiện tại
        Form.close()
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cancel.setText(_translate("Form", "Cancel"))
        self.crop.setText(_translate("Form", "Crop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())