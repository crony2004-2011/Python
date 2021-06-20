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
#PYTESSERACT PROGRAM
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = I.open('download5.png')
text = tess.image_to_string(image)
print(text)