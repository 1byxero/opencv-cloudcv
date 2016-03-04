import cv2
import numpy as np
from matplotlib import pyplot as plt
from os import path

def grayscale(image):
	img = cv2.imread(image,0)
	imagename = str(image).split(".")[0]
 	cv2.imwrite(imagename+"_grayscale_processed.jpg",img)

def binarythreshold(image):
	img = cv2.imread(image,0)
	ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
	imagename = str(image).split(".")[0]
 	cv2.imwrite(imagename+"_binarythresholding_processed.jpg",thresh1)

def histogram(image):
	img = cv2.imread(image)
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)	
	hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
	imagename = str(image).split(".")[0]
	cv2.imwrite(imagename+"_histogram_processed.jpg",hist)

def cannyedge(image):
	img = cv2.imread(image,0)
	edges = cv2.Canny(img,100,200)
	imagename = str(image).split(".")[0]
	cv2.imwrite(imagename+"_edge_processed.jpg",edges)

def sobelfilter(image):
	img = cv2.imread(image,0)
	sobel = cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)
	imagename = str(image).split(".")[0]
	cv2.imwrite(imagename+"_sobelfilter_processed.jpg",sobel)


def gradientextraction(image):
	img = cv2.imread(image,0)

	# Output dtype = cv2.CV_8U
	sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)

	# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
	sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
	abs_sobel64f = np.absolute(sobelx64f)
	sobel_8u = np.uint8(abs_sobel64f)

	plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
	plt.title('Original'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
	plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
	plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

	plt.show()

def smoothing(image):
	img = cv2.imread(image)
	kernel = np.ones((5,5),np.float32)/25
	dst = cv2.filter2D(img,-1,kernel)

	# plt.subplot(121),plt.imshow(img),plt.title('Original')
	# plt.xticks([]), plt.yticks([])
	# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
	# plt.xticks([]), plt.yticks([])
	# plt.show()		

	imagename = str(image).split(".")[0]
 	cv2.imwrite(imagename+"_smoothing_processed.jpg",dst)	


def foregroundextract(image):
	img = cv2.imread(image)
	mask = np.zeros(img.shape[:2],np.uint8)

	bgdModel = np.zeros((1,65),np.float64)
	fgdModel = np.zeros((1,65),np.float64)

	rect = (50,50,450,290)
	cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

	mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
	img = img*mask2[:,:,np.newaxis]

	plt.imshow(img),plt.colorbar(),plt.show()


