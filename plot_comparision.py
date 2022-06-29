######### SERAJ Mostafa @UMBC #########
###### Using opencv thresholding ######
## apply to whole dir with same name ##

dir1 = ('/your/path/to/dir1/')
dir2 = ('/your/path/to/dir2/')

from matplotlib import pyplot as plt
import cv2, os

for file in os.scandir(dir1):
  img1 = cv2.imread(file.path)
  img2 = cv2.imread(dir2+'/'+file.name)
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 16))
  # fig.suptitle('Horizontally stacked subplots')
  ax1.imshow(img1)
  ax1.set_title('actual image')
  ax2.imshow(img2)
  ax2.set_title('converted image')