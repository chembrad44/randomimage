import argparse
from PIL import Image
import numpy as np

parser = argparse.ArgumentParser(description='Random Image Generator')
parser.add_argument('--width', type=int, help='The amount of pixels in our image\'s width')
parser.add_argument('--height', type=int, help='The amount of pixels in our image\'s height')
parser.add_argument('--outfile', type=str, help='Output file name')
parser.add_argument('--infile', type=str, help='Input file name')
parser.add_argument('--testing', action='store_true', help='Testing some features')
parser.set_defaults(testing=False)

args = parser.parse_args()

infile = args.infile
outfile = args.outfile
testing = args.testing
width = args.width
height = args.height

if infile:
    image = Image.open(infile)
    imageSize = image.size

    for w in range(imageSize[0]):
        for h in range(imageSize[1]):
            pixel = image.getpixel((w,h))
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            if green > 190:
                red = pixel[0] - 15
                green = pixel[1] - 100
                blue = pixel[2] - 15
            newPixel = (red, blue, green)
            image.putpixel((w,h), newPixel)

            '''
            if pixel[0] < 127:
                red = pixel[0] - 50
            else:
               red = pixel[0] + 50

            newPixel = (red,pixel[1],pixel[2])
            image.putpixel((w,h), newPixel)
            '''

    #pixel = image.getpixel((600,500))
    #print(pixel[0])
elif testing:
    array = np.random.randint(255,256,(width,height,3),dtype=np.uint8)
    image = Image.fromarray(array)
    wstep = 255//width
    hstep = 255//height
    r = 0
    b = 0
    g = 100
    for w in range(width):
        for h in range(height):
            color = (r, g, b)
            r = r + wstep
            image.putpixel((w,h), color)
        r = 0
        b = b + hstep

else:
    array = np.random.randint(255,256,(width,height,3),dtype=np.uint8)
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


#print(width)
#print(height)
#print(array)

if outfile:
    image.save("images/" + outfile)

# im = Image.open("/home/bbahls/src/nellie/git/randomimage/src/image1.png")
# im.show()

