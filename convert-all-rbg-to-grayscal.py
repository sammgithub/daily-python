######### SERAJ Mostafa @UMBC #########
######## Using OS and PIL in Python ###
###### folder/dir wise conversion #####

import os
from PIL import Image

dir1 = ('/your/path/to/dir1/')
dir2 = ('/your/path/to/dir2/')

for filename in os.listdir(dir1):                                                                                                                                                                
    img = Image.open(dir1 + filename).convert("L") ## LA is for grayscale with alpha channel
    img.save(dir2 + filename)
