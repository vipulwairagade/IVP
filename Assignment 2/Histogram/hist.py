import sys 												# For taking argument through terminal
import numpy as np
import matplotlib.pyplot as plt 						# Plotting of Histogram
import cv2


# Taking Argument Through Terminal and Validating

if len(sys.argv)>1:
	fname = sys.argv[1]
else :
    print("usage : python hist.py <image_file>")

im = cv2.imread(fname)

if im is None:
    print('Failed to load image file:', fname)
    sys.exit(1)
         
def generateHistogram(im):
	gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)			# Coverting into gray image
	hist = cv2.calcHist([gray],[0],None,[256],[0,256])	# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
	plt.plot(hist)										# Plotting using matplotlib
	plt.xlabel('Pixel Values')
	plt.ylabel('No. of Pixels')
	plt.title('Histogram of Image')						
	plt.grid(True)
	plt.show()											# Displaying histogram



cv2.imshow('image',im)									# Display original image
generateHistogram(im)									# Display loaded image

