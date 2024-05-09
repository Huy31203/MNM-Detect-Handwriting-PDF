# Detect HandWriting and Convert to PDF
# Nhận dạng chữ viết tay (Detect Handwriting)

Đồ án nhận dạng chữ viết tay là một ứng dụng winform được viết dựa trên ngôn ngữ Python kết hợp với các thư viện như PyQt5, OpenCV, VietOCR, Tesseract, v.v....

## 📌 Các tính năng của ứng dụng

- Người dùng có thể upload ảnh và thực hiện các chuyển đổi từ một hình ảnh có nội dung chữ viết tay bên trong
- Người dùng có thể chụp ảnh từ camera máy tính và thực hiện các chuyển đổi từ một hình ảnh có nội dung chữ viết tay bên trong
- Người dùng có thể đưa đường dẫn hình ảnh và thực hiện chuyển đổi từ một hình ảnh có nội dung chữ viết tay bên trong
- Người dùng có thể chỉnh sửa hình ảnh để cho ứng dụng dễ dàng nhận diện hơn như cắt ảnh, tùy chỉnh độ sáng/tối, màu sắc
- Người dùng có thể chỉnh sửa lại nội dung sau khi ứng dụng hoàn tất quá trình nhận dạng chữ viết tay trong hình ảnh
- Người dùng có thể xuất nội dung sau khi ứng dụng hoàn tất quá trình nhận dạng ra file PDF

## 📌 Các thông tin thêm về thư viện được sử dụng trong ứng dụng

- [Python]: (v3.10) - Python là một ngôn ngữ lập trình thông dịch, được sử dụng phổ biến cho nhiều mục đích khác nhau từ phát triển web đến trí tuệ nhân tạo.
- [OpenCV]: (v4.8.1.78) - OpenCV là một thư viện mã nguồn mở về thị giác máy tính và xử lý hình ảnh, cung cấp các công cụ mạnh mẽ cho việc xử lý và phân tích ảnh số.
- [PyQt6] (v6.4.2) - PyQt6 là một bộ công cụ lập trình ứng dụng đồ họa người dùng (GUI) cho Python, được xây dựng trên cơ sở của Qt Framework.
- [Pillow] (v9.5.0) - Pillow là một fork của thư viện xử lý hình ảnh Python PIL (Python Imaging Library), cung cấp các chức năng mạnh mẽ cho việc xử lý hình ảnh.
- [Pytesseract] (v0.3.10) - Pytesseract là một giao diện Python cho Tesseract OCR Engine, cho phép nhận diện ký tự từ hình ảnh.
- [VietOCR] (v0.3.11) - VietOCR là một thư viện Python cho nhận diện ký tự tiếng Việt từ hình ảnh, dựa trên Tesseract OCR Engine.
- [Pyenchant] (v3.2.2) - Pyenchant là một giao diện Python cho Enchant, một thư viện kiểm tra chính tả mã nguồn mở, hỗ trợ nhiều ngôn ngữ và từ điển.

## 📌 Tập dữ liệu model cho việc train

- Với hơn 400,000 file ảnh và label cho việc train dữ liệu bằng Google Colab trong 3 tiếng với độ chính xác từ 60% đến 90% tùy thuộc vào ảnh đầu vào có chất lượng cao hay thấp

## 📌 Installation

- Cài đặt Python v3.10
- Cài đặt các thư viện theo file requirements (có thể xảy ra lỗi do một vài thư viện nâng cấp lên version mới có thể bị xung đột): `pip install -r requirements.txt`
- Chạy chương trình: `python mainGUI.py`

## 📌 Project structure

```text
Detect-Handwriting-PDF
├─ Images
├─ languages
├─ temp (chứa ảnh tạm phục vụ cho việc crop ảnh)
├─ Tesseract-OCR (chứa engine để thực hiện nhận diện ký tự từ hình ảnh)
├─ UI
├─ venv
│  ├─ Include
│  │  └─ Models (chứa model đã train từ Google Colab)
├─ convertGUI.py
├─ cropGUI.py
├─ HandleDetect.py
├─ mainGUI.py
├─ segmentation.py
├─ toPDF.py

```

[Python]: https://www.python.org/
[OpenCV]: https://opencv.org/
[PyQt6]: https://www.riverbankcomputing.com/software/pyqt/intro
[Pillow]: https://pillow.readthedocs.io/en/stable/
[Pytesseract]: https://github.com/tesseract-ocr/tesseract
[VietOCR]: https://github.com/pbcquoc/vietocr
[Pyenchant]: https://pyenchant.github.io/pyenchant/
