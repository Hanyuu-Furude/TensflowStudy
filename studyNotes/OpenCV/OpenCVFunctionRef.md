# OpenCVFunctionRef

* 演示程序请参照[OpenCVFunctionRef.py](OpenCVFunctionRef.py)
***
## 1.图像读取
* cv2.imread()
``` py
import numpy as mp
import cv2
img =cv2.imread('example.jpg',0)
```
> Use the function cv2.imread() to read an image. The image should be in the working directory or a full path of image should be given.\
> Second argument is a flag which specifies the way image should be read.\
>>cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.\
>>cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode\
>>cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
>>- *Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.*


* cv2.inshow()
``` py
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
>Use the function cv2.imshow() to display an image in a window. The window automatically fits to the image size. \
>First argument is a window name which is a string. second argument is our image. You can create as many windows as you wish, but with different window names.

* cv2.waitKey()

>cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. The function waits for specified milliseconds for any keyboard event. If you press any key in that time, the program continues. If 0 is passed, it waits indefinitely for a key stroke. It can also be set to detect specific key strokes like, if key a is pressed etc which we will discuss below.
>> * Besides binding keyboard events this function also processes many other GUI events, so you MUST use it to actually display the image. 

* cv2.destoryAllWindows()
>cv2.destroyAllWindows() simply destroys all the windows we created. If you want to destroy any specific window, use the function cv2.destroyWindow() where you pass the exact window name as the argument.
>> * There is a special case where you can already create a window and load image to it later. In that case, you can specify whether window is resizable or not. It is done with the function cv2.namedWindow(). By default, the flag is cv2.WINDOW_AUTOSIZE. But if you specify flag to be cv2.WINDOW_NORMAL, you can resize window. It will be helpful when image is too large in dimension and adding track bar to windows. 

## 2.图像写入
* cv2.imwrite()
``` py
cv2.imwrite('messigray.png',img)
```
>Use the function cv2.imwrite() to save an image. \
>First argument is the file name, second argument is the image you want to save.