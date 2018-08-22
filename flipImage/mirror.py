import sys
from PIL import Image

img = Image.open(sys.argv[1])
flag = raw_input("Enter How to Flip (h/v) : ")

def flip_vert(img):
    width  = img.size[0]
    height = img.size[1]
    for y in range(height):
        for x in range(width//2):
            left = img.getpixel((x, y))
            right = img.getpixel((width - 1 - x, y))
            img.putpixel((width - 1 - x, y), left)
            img.putpixel((x, y), right)
    return img



flip_vert (img)
img.save('img_mirror.jpg')