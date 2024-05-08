import cv2
import numpy as np
import pytesseract
import re

# Cấu hình đường dẫn của Tesseract
pytesseract.pytesseract.tesseract_cmd = r'.\Tesseract-OCR\tesseract.exe'

PATTERN = "[aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789]"

def ImgHasText(image):
    # Làm mờ ảnh bằng Gaussian Blur
    image = cv2.GaussianBlur(image, (5, 5), 0)
    # Sử dụng phát hiện biên Canny để tạo ra hình ảnh biên
    edged = cv2.Canny(image, 30, 100)
    found = False
    # Sử dụng Tesseract để trích xuất văn bản từ hình ảnh biên
    text = pytesseract.image_to_string(edged, lang='eng', config='--psm 7')
    # So khớp với biểu thức chính quy để xác định xem văn bản được trích xuất có chứa các ký tự từ PATTERN hay không
    regex = re.compile(PATTERN)
    if regex.search(text):
        found = True
    return found

def showImg(img):    
    cv2.imshow("img", img)
    cv2.waitKey(0)

def thresholding(image):
    # Chuyển đổi ảnh màu sang thang độ xám
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Áp dụng ngưỡng nhị phân để chuyển đổi ảnh thành ảnh nhị phân
    ret, thresh = cv2.threshold(img_gray, 100, 300, cv2.THRESH_BINARY_INV)
    return thresh   

def line_segmentation(img):
    # Chuyển đổi ảnh sang không gian màu RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
    h, w, c = img.shape

    # Thực hiện việc resize ảnh nếu cần thiết để giảm kích thước
    if w > 1000:
        new_w = 1000
        ar = w/h
        new_h = int(new_w/ar)
        img = cv2.resize(img, (new_w, new_h), interpolation = cv2.INTER_AREA) 

    thresh_img = thresholding(img)

    # Tăng độ dày để của chữ dựa trên màu trắng đen để dễ dàng khoanh vùng
    kernel = np.ones((20, 150), np.uint8)
    dilated = cv2.dilate(thresh_img, kernel, iterations = 1)
    
    # Tìm các đoạn đã khoanh vùng
    (contours, heirachy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)

    # Sắp xếp các đoạn theo chiều dọc
    sorted_contours_lines = sorted(contours, key = lambda ctr : cv2.boundingRect(ctr)[1])
    img2 = img.copy()

    segments = []
    # Duyệt qua các đoạn đã sắp xếp
    for ctr in sorted_contours_lines:
        x, y, w, h = cv2.boundingRect(ctr)
        segment = img2[y:y+h, x:x+w]
        segment_gray = cv2.cvtColor(segment, cv2.COLOR_BGR2GRAY)
        # Kiểm tra xem đoạn văn bản có chứa văn bản hay không
        if h > 50:
            if ImgHasText(segment_gray):
                # Đánh dấu đoạn văn bản được phát hiện bằng hình chữ nhật màu xanh lá cây
                cv2.rectangle(img, (x, y), (x+w, y+h), (40, 100, 250), 2)
                segments.append(segment_gray)
    
    segments.insert(0, img)
    return segments

if __name__ == "__main__":
    pass