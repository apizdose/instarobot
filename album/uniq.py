import random
from PIL import Image, ImageFilter
import glob
import os

def tspose(filename):
    im = Image.open(filename)
    #im = im.transpose(Image.FLIP_LEFT_RIGHT)
    pix = [(pixel[0], pixel[1], pixel[2]) for pixel in im.getdata()]
    for i in range(5):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255) 

        ran=random.randint(10,(len(pix) - 10))

        pix[ran] = (red, green, blue)

    im.putdata(pix)
    #im = im.filter(ImageFilter.GaussianBlur(3))
    im.save(filename)
    
path = os.getcwd()
mkfiles = glob.glob("album/*.jpg")


for i in mkfiles:
    print(i)
    tspose(i)
