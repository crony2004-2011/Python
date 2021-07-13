import cv2
from wand.image import Image
import os
import easyocr
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract as tess
os.chdir(r'C:\Users\Acer\Desktop')

image = cv2.imread('sharpkoala.jpeg')
image = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_,th1 = cv2.threshold(grayimg,70,255,cv2.THRESH_TOZERO)
_,th2 = cv2.threshold(th1,0,255,cv2.THRESH_BINARY_INV)
#blur = cv2.GaussianBlur(th2,(3,3),0)
_,th4 = cv2.threshold(th2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Mexican-Hat', th4)
cv2.waitKey(0)

#tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#text = tess.image_to_string(th1)
#print(text)
