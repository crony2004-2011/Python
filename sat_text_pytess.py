import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image, ImageEnhance
import cv2
import pytesseract as tess
import PIL
from PIL import Image as I
import wand
from wand.image import Image

#MAKE IMAGE CLEARER
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('download.png',0)
_, th1 = cv2.threshold(img,150,255,cv2.THRESH_TOZERO)
#blur = cv2.GaussianBlur(th1,(5,5),0)
#_,th4 = cv2.threshold(blur,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('SAT',th1)

#EXTRACT TEXT
text = tess.image_to_string(th1)
