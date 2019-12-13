import numpy as np
import cv2

img = cv2.imread('new2.jpg')
img_rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hls=cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

hsv_gray = cv2.cvtColor(img_hsv,cv2.COLOR_BGR2GRAY)
kernel_size = 5
hsv_blur = cv2.GaussianBlur(hsv_gray,(kernel_size, kernel_size),0)

ret, thresh = cv2.threshold(hsv_gray, 150, 255, cv2.THRESH_BINARY)
kernel = np.ones((2,2))
erosion = cv2.dilate(thresh,kernel,iterations = 1)

final = cv2.inpaint(img, thresh, 3, cv2.INPAINT_TELEA)

cv2.imshow('hsv_gray', hsv_gray)
cv2.imshow('img', img)
cv2.imshow('final', final)
cv2.imshow('erosion', erosion)
cv2.imshow('img_hsv', img_hsv)
#cv2.imshow('img_hls', img_hls)

cv2.waitKey(0)
cv2.destroyAllWindows()
