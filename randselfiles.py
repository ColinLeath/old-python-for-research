import os
import random
import shutil
#Create randomized list of images:
#imagedir = 'x:\\new\\'
imagedir = 'x:\\tl\\'
imagelist = os.listdir(imagedir)
random.shuffle(imagelist)

for n in range(12):
    shutil.copy(imagedir + imagelist[n], 'x:\\tlpractice')
