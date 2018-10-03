# OpenCVBasicOperations
* 演示程序请参照[OpenCVBasicOperations.py](OpenCVBasicOperations.py)
***
``` py
import cv2
import numpy as np
# Load a color image.
img = cv2.imread('example.jpg')
px = img[100,100]
print(px)
# accessing only blue pixel
# BGR color system!
blue = img[100,100,0]
print(blue)
```
>* You can access a pixel value by its row and column coordinates. For BGR image, it returns an array of Blue, Green, Red values. For grayscale image, just corresponding intensity is returned.
>* You can modify the pixel values the same way.
``` py
img[100,100]=[255,255,255]
print(img[100,100])
```
>* Numpy is a optimized library for fast array calculations. So simply accessing each and every pixel values and modifying it will be very slow and it is discouraged.
>* Above mentioned method is normally used for selecting a region of array, say first 5 rows and last 3 columns like that. For individual pixel access, Numpy array methods, array.item() and array.itemset() is considered to be better. But it always returns a scalar. So if you want to access all B,G,R values, you need to call array.item() separately for all.
