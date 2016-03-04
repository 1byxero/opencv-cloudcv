import cv2
import numpy as np
from matplotlib import pyplot as plt

def cannyedge(image):
	img = cv2.imread("filter.jpg",0)
	edges = cv2.Canny(img,100,200)

	plt.subplot(121),plt.imshow(img,cmap = 'gray')
	plt.title('Original Image'), plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(edges,cmap = 'gray')
	plt.title('Edge Image'), plt.xticks([]), plt.yticks([])


	cv2.imwrite("processed.jpg",edges)
	plt.show()



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

	plt.subplot(121),plt.imshow(img),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
	plt.xticks([]), plt.yticks([])
	plt.show()

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


