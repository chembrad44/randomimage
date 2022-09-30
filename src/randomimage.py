import argparse
from PIL import Image
import numpy as np

parser = argparse.ArgumentParser(description='Random Image Generator')
parser.add_argument('--width', type=int, help='The amount of pixels in our image\'s width')
parser.add_argument('--height', type=int, help='The amount of pixels in our image\'s height')
parser.add_argument('--outfile', type=str, help='Output file name')

args = parser.parse_args()

width = args.width
height = args.height
filename = args.outfile

array = np.random.randint(0,256,(width,height,3),dtype=np.uint8)
image = Image.fromarray(array)

myBlueColor = (82,108,168)
upperLeft = (0,0)
lowerLeft = (0,height-1)
upperRight = (width-1,0)
lowerRight = (width-1,height-1)
middle = (width//2, height//2)

image.putpixel(upperLeft, myBlueColor)
image.putpixel(lowerRight, myBlueColor)
image.putpixel(upperRight, myBlueColor)
image.putpixel(lowerLeft, myBlueColor)
image.putpixel(middle, myBlueColor)

image.show()

print(width)
print(height)
print(array)


# im = Image.open("/home/bbahls/src/nellie/git/randomimage/src/image1.png")
# im.show()

