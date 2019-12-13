import numpy as np
import cv2

img = cv2.imread('new.jpg')
mask = (img.shape)
cv2.imshow('start', img)
x=int(474/2)

cv2.line(img, (125, 50), (115, 350), (0,0,255), 2)
cv2.line(img, (200, 29), (40, 30), (0,0,255), 2)
cv2.line(img, (1, 1), (474, 346), (0,0,255), 2)
cv2.line(img, (250, 250), (45, 45), (0,0,255), 2)
cv2.line(img, (300, 260), (400, 260), (0,0,255), 2)
cv2.line(img, (474, 1), (1, 346), (0,0,255), 2)
cv2.line(img, (x, 1), (x, 346), (0,0,255), 2)
#cv2.imwrite('lines.jpg', img)

cv2.line(mask, (125, 50), (115, 350), (255,255,255), 2)
cv2.line(mask, (200, 29), (40, 30), (255,255,255), 2)
cv2.line(mask, (1, 1), (474, 346), (255,255,255), 2)
cv2.line(mask, (250, 250), (45, 45), (255,255,255), 2)
cv2.line(mask, (300, 260), (400, 260), (255,255,255), 2)
cv2.line(mask, (474, 1), (1, 346), (255,255,255), 2)
cv2.line(mask, (x, 1), (x, 346), (255,255,255), 2)

dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)

cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
