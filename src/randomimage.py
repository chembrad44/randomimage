import argparse

parser = argparse.ArgumentParser(description='Random Image Generator')
parser.add_argument('--width', type=int, help='The amount of pixels in our image\'s width')
parser.add_argument('--height', type=int, help='The amount of pixels in our image\'s height')


args = parser.parse_args()

width = args.width
height = args.height

print(width)
print(height)



print("Hello")