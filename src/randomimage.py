import argparse
from PIL import Image

parser = argparse.ArgumentParser(description='Random Image Generator')
parser.add_argument('--width', type=int, help='The amount of pixels in our image\'s width')
parser.add_argument('--height', type=int, help='The amount of pixels in our image\'s height')
parser.add_argument('--outfile', type=str, help='Output file name')

args = parser.parse_args()

width = args.width
height = args.height
filename = args.outfile

print(width)
print(height)
print(filename)

print("Hello")

# im = Image.open("/home/bbahls/src/nellie/git/randomimage/src/image1.png")
# im.show()
