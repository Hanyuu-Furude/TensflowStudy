import cv2

img = cv2.imread('example.jpg')
print('img[300,300]=%s' % img[300,300])
print('blue pixel %s' %img[300,300,0])
print('green pixel %s' %img[300,300,1])
print('red pixel %s' %img[300,300,2])
print(img[300,300,3])

cv2.imshow('img', img)
k = cv2.waitKey(0)  # & 0xff
if k == 27:  # ESC
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('Save.jpg', img)