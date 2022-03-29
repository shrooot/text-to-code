import cv2 as cv
import pytesseract as tess
import numpy as np

img_path = "./data/testdata.jpeg"
img = cv.imread(img_path)
# cv.imshow("stock image",img)


def resizeImage(img):
    scale_percent = 60

    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    # cv.imshow("resized image",resized_img)
    return resized_img


def getThresholdImg(grayscale_img):
    th = cv.adaptiveThreshold(
        grayscale_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 35, 13)
    return th


def removeNoice(th):
    noice_removed = cv.fastNlMeansDenoising(
        th, h=20, templateWindowSize=11, searchWindowSize=33)
    return noice_removed


def preprocessImg(img):
    resized_img = resizeImage(img)
    grayscale_img = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
    # cv.imshow("grayscale image", grayscale_img)

    th = getThresholdImg(grayscale_img)
    # cv.imshow("adaptive threshold image", th)

    noice_removed = removeNoice(th)
    # cv.imshow("noise removed image", noice_removed)

    # cv.imwrite("modelreadyimage2.png",noice_removed)
    return noice_removed

    # cv.waitKey(0)
    # cv.destroyAllWindows()
