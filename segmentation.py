# Import necessary libraries
import cv2
import numpy as np
import pytesseract
import re

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'.\Tesseract-OCR\tesseract.exe'

# Define a regex pattern to match Vietnamese characters and numbers
PATTERN = "[aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789]"

# Function to check if an image contains text
def ImgHasText(image):
    # Apply Gaussian blur to the image
    image = cv2.GaussianBlur(image, (5, 5), 0)
    # Detect edges in the image
    edged = cv2.Canny(image, 30, 100)
    found = False
    regex = re.compile(PATTERN)
    # Use Tesseract to convert image to string
    text = pytesseract.image_to_string(edged, lang='eng', config='--psm 7')
    # Search for the pattern in the text
    if regex.search(text):
        found = True
    return found

# Function to display an image
def showImg(img):    
    cv2.imshow("img", img)
    cv2.waitKey(0)

# Function to apply thresholding to an image
def thresholding(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply binary inverse thresholding
    ret, thresh = cv2.threshold(img_gray, 100, 300, cv2.THRESH_BINARY_INV)
    return thresh   

# Function to segment lines in an image
def line_segmentation(img):
    # Convert image to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
    h, w, c = img.shape

    # Resize image if width is greater than 1000
    if w > 1000:
        new_w = 1000
        ar = w/h
        new_h = int(new_w/ar)
        
        img = cv2.resize(img, (new_w, new_h), interpolation = cv2.INTER_AREA) 

    # Apply thresholding
    thresh_img = thresholding(img)

    # Define a kernel for dilation
    kernel = np.ones((20, 150), np.uint8)
    # Dilate the image
    dilated = cv2.dilate(thresh_img, kernel, iterations = 1)
    
    # Find contours in the dilated image
    (contours, heirachy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)

    # Sort contours based on y-coordinate
    sorted_contours_lines = sorted(contours, key = lambda ctr : cv2.boundingRect(ctr)[1])
    img2 = img.copy()

    segments = []
    # Iterate through each contour
    for ctr in sorted_contours_lines:
        x, y, w, h = cv2.boundingRect(ctr)
        segment = img2[y:y+h, x:x+w]
        segment_gray = cv2.cvtColor(segment, cv2.COLOR_BGR2GRAY)
        # Check if the height of the contour is greater than 50 and contains text
        if h > 50:
            if ImgHasText(segment_gray):
                # Draw a rectangle around the text
                cv2.rectangle(img, (x, y), (x+w, y+h), (40, 100, 250), 2)
                segments.append(segment_gray)
    
# Insert the original image at the beginning of the segments list
    segments.insert(0, img)
    return segments