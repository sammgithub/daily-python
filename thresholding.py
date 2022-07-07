######### SERAJ Mostafa @UMBC #########
###### Using opencv thresholding ######
## apply to whole dir with same name ##
import os, cv2

target_value = 118
max_value = 255

def img_thresholding(img):
  image = img
  img_gr = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  _,thresh = cv2.threshold(img_gr,target_value,max_value,cv2.THRESH_BINARY)
  # _,thresh = cv2.threshold(img_gr,target_value,max_value,cv2.THRESH_BINARY_INV)
  # _,thresh = cv2.threshold(img_gr,target_value,max_value,cv2.THRESH_TRUNC)
  # _,thresh = cv2.threshold(img_gr,target_value,max_value,cv2.THRESH_TOZERO)

  return thresh

src = ('/your/path/to/src/dir/')
dst = ('/your/path/to/dst/dir/')

files = os.scandir(src)

for file in files:
  img = cv2.imread(file.path)
  im = img_thresholding(img)
  cv2.imwrite(dst+'/'+file.name, im)
