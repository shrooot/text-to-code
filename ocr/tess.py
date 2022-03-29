import pytesseract as tess
import cv2

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def getCodeFromImg(img):
    img2 = cv2.imread('./modelreadyimage.png')
    test = tess.image_to_string(img2)
    print(test)
    return test

# getCodeFromImg("absc")