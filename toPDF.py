from fpdf import FPDF
from PyQt6.QtWidgets import QFileDialog
import cv2, os
import segmentation as sg

def convertToPdf(text, image):
    # Tạo tệp PDF và ghi nội dung văn bản đã chuyển đổi vào tệp đó
    pdf = FPDF()
    pdf.encoding = 'utf-8'
    pdf.add_page()
    pdf.add_font('ArialUni', '', r'ArialUni.ttf', uni=True)
    pdf.set_font('ArialUni', '', 15)
    pdf.multi_cell(0, 5, text)
    # lưu ảnh vào file tạm thời
    cv2.imwrite('PDFtemp.jpg', image)
    pdf.add_page()
    pdf.cell(200, 10, "Chữ đã được nhận dạng:", ln=1, align="L")
    pdf.image('PDFtemp.jpg', x=10, y=30, w=100)
    # xóa file tạm thời
    os.remove('PDFtemp.jpg')

    
    #Lưu tệp PDF
    save_path, _ = QFileDialog.getSaveFileName(None, "Lưu văn bản vào tệp PDF", "", "PDF Files (*.pdf)")
    if save_path:
        pdf.output(save_path)
        return True