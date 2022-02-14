from ast import arg
from cgi import print_environ_usage
from distutils.log import error
from xml.dom import HierarchyRequestErr
from PIL import Image
import sys

def print_usage():
    print("\nTo use you need to select an image by path and the grid size:\npy carrousel_maker.py image_name.ext gridY gridX")

if __name__ == "__main__":
    # Check for correct usage
    if len(sys.argv)  != 4:
        print_usage()
        exit(0)
    else:
        try:
            im = Image.open(sys.argv[1])
            gridY = int(sys.argv[2])
            gridX = int(sys.argv[3])
            print("Image read!")
        except:
            print("Something went wrong reading the file!")
        
        width = im.width
        height = im.height

        cellX = round(width / gridX)
        cellY = round(height / gridY)

        print("Dividing image")
        for i in range(gridX):
            for j in range(gridY):
                im_crop = im.crop((cellX*i, cellY*j, cellX*(i+1), cellY*(j+1)))
                im_crop.save('out{}-{}.jpg'.format(i,j), quality=100)
        print("DONE!! See outX-Y.jpg")