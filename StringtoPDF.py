from fpdf import FPDF
from PyQt5.QtWidgets import QFileDialog

def convertToPdf(self):
    # Tạo tệp PDF và ghi nội dung văn bản đã chuyển đổi vào tệp đó
    pdf = FPDF()
    pdf.encoding = 'utf-8'
    pdf.add_page()
    pdf.add_font('ArialUni', '', r'ArialUni.ttf', uni=True)
    pdf.set_font('ArialUni', '', 12)
    pdf.multi_cell(0, 5, self.text)

    #Lưu tệp PDF
    save_path, _ = QFileDialog.getSaveFileName(self, "Lưu văn bản vào tệp PDF", "", "PDF Files (*.pdf)")
    if save_path:
        pdf.output(save_path)
        return True
