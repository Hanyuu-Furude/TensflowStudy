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