import sys
import cv2
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QImage, QPainter, QColor, QPen, QCursor
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QGraphicsRectItem
from PyQt6.QtCore import Qt, QPoint, QRect, QSize
import mainGUI

class ImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.drag_start = None
        self.drag_end = None
        self.rect = None
        self.draw_rect_pen = QPen(QColor("red"))
        self.draw_rect_pen.setWidth(1)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start = event.pos()
            self.rect = QRect(self.drag_start, QSize())
            self.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.update()

    def mouseMoveEvent(self, event):
        if self.drag_start is not None:
            self.drag_end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.rect = QRect(self.drag_start, event.pos()).normalized()
            self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.update()
        
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(255, 0, 0), 1, Qt.PenStyle.SolidLine))
        if self.drag_start and self.drag_end:
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
        self.cancel = QtWidgets.QPushButton(self.horizontalFrame, clicked = lambda: self.cancelCrop(Form))
        self.cancel.setMinimumSize(QtCore.QSize(100, 40))
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.crop = QtWidgets.QPushButton(self.horizontalFrame, clicked = lambda: self.cropImage(Form))
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
        if self.imageLabel.drag_start is not None:
            x1 = min(self.imageLabel.drag_start.x(), self.imageLabel.drag_end.x())
            y1 = min(self.imageLabel.drag_start.y(), self.imageLabel.drag_end.y())
            x2 = max(self.imageLabel.drag_start.x(), self.imageLabel.drag_end.x())
            y2 = max(self.imageLabel.drag_start.y(), self.imageLabel.drag_end.y())
            
            img = cv2.resize(self.image, (790, 540), interpolation = cv2.INTER_AREA)
            self.cropped_image = img[y1:y2, x1:x2]
            cv2.imwrite("temp/temp.jpg", self.cropped_image)
            MainWindow = QtWidgets.QMainWindow()
            self.mainWindow = mainGUI.Ui_MainWindow()
            self.mainWindow.setupUi(MainWindow)
            self.mainWindow.receiveImg()
            MainWindow.show()
            Form.close()            
            
    def Image(self, image, filename):
        self.image = image
        self.filename = filename
        image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        height, width, channel = image_rgb.shape
        bytesPerLine = channel * width
        qImg = QImage(image_rgb.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        self.pixmap = QPixmap.fromImage(qImg)
        self.imageLabel.setPixmap(self.pixmap.scaled(790, 540))
        
    def cancelCrop(self, Form):
        MainWindow = QtWidgets.QMainWindow()
        self.mainWindow = mainGUI.Ui_MainWindow()
        self.mainWindow.setupUi(MainWindow)
        self.mainWindow.reOpenMain(self.filename)
        MainWindow.show()
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