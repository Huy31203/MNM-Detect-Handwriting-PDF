import cv2
import numpy as np
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'D:\Code\VS Code\MNM\Python-Detect-HandWriting-PDF-main\Tesseract-OCR\tesseract.exe'
PATTERN = "[aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789]"#delete 'cause it's too long, cannot capture, it a-z

def ImgHasText(image):
    image = cv2.GaussianBlur(image, (5, 5), 0)
    edged = cv2.Canny(image, 30, 100)
    found = False
    regex = re.compile(PATTERN)
    text = pytesseract.image_to_string(edged, lang='eng', config='--psm 7')
    if regex.search(text):
        found = True
    return found


def showImg(img):    
    cv2.imshow("img", img)
    cv2.waitKey(0)

def thresholding(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 100, 300, cv2.THRESH_BINARY_INV)
    return thresh   

def line_segmentation(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
    h, w, c = img.shape

    if w > 1000:
        new_w = 1000
        ar = w/h
        new_h = int(new_w/ar)
        
        img = cv2.resize(img, (new_w, new_h), interpolation = cv2.INTER_AREA) 

    thresh_img = thresholding(img)

    kernel = np.ones((20, 150), np.uint8)
    dilated = cv2.dilate(thresh_img, kernel, iterations = 1)
    
    (contours, heirachy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)

    sorted_contours_lines = sorted(contours, key = lambda ctr : cv2.boundingRect(ctr)[1])
    img2 = img.copy()

    segments = []
    for ctr in sorted_contours_lines:
        x, y, w, h = cv2.boundingRect(ctr)
        segment = img2[y:y+h, x:x+w]
        segment_gray = cv2.cvtColor(segment, cv2.COLOR_BGR2GRAY)
        if h > 50:
            if ImgHasText(segment_gray):
                cv2.rectangle(img, (x, y), (x+w, y+h), (40, 100, 250), 2)
                segments.append(segment_gray)
    
    segments.insert(0, img)
    return segments