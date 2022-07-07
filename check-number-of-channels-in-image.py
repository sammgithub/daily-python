######### SERAJ Mostafa @UMBC #########
######## using PIL and openCV #########
#### check number of image channels ###

import cv2
from PIL import Image

img_pil = Image.open(r'file.png')
print('Pillow: ', img_pil.mode, img_pil.size)

img = cv2.imread('file.png', cv2.IMREAD_UNCHANGED)
print('OpenCV: ', img.shape)
