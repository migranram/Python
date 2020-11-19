import os
import argparse
from PIL import Image
from io import BytesIO
import math

unitdef = {'MB': 1000000, 'KB': 1000, 'GB': 1000000000, 'B': 1}

parser = argparse.ArgumentParser(description='Downgrade image to fit web-size requirements')
parser.add_argument('path',metavar='p',type=str)
parser.add_argument('size',metavar='s',type=float)
parser.add_argument('units',metavar='u',type=str)

arguments = parser.parse_args()

size_ob = arguments.size
scale = unitdef[arguments.units.upper()]

fill_color = 255

myimage = Image.open(arguments.path)
if myimage.mode in ('RGBA', 'LA'):
    background = Image.new(myimage.mode[:-1], myimage.size, fill_color)
    background.paste(myimage, myimage.split()[-1])
    myimage = background

img_file = BytesIO()
myimage.save(img_file,'jpeg')
size = img_file.tell()/scale

width, height = myimage.size

print('Size of the current picture: ',size, arguments.units.upper())

while(size > size_ob):
    img_file.seek(0)
    width, height = myimage.size
    width = math.floor(0.99*width)
    height = math.floor(0.99*height)
    myimage = myimage.resize([width,height])
    myimage.save(img_file,'jpeg')
    size = img_file.tell()/scale
    print('Resized: ',size, arguments.units.upper())

print('New size of the picture: ', size, arguments.units.upper())
myimage.save('output.jpeg')
