import cv2 as cv2
import numpy as np
img=cv2.imread('a')
img = cv2.imread('example.jpg', 1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 0, 0), 2, cv2.LINE_AA)
cv2.imshow('image', img)
# Create a black image
img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image0', img)
# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.imshow('image1', img)
k = cv2.waitKey(0) & 0xffa
if k == 27:  # ESC
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Save.jpg', img)
