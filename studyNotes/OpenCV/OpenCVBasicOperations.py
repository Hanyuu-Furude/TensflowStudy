import cv2

img =cv2.imread('example.jpg')
cv2.imshow('img',img)
k = cv2.waitKey(0)# & 0xff
if k == 27:  # ESC
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Save.jpg', img)
