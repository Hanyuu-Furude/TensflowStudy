import cv2
import matplotlib
import numpy
import matplotlib.pyplot as plt

# %matplotlib inline
# for ipynb
pic_name='example.png'
pic=cv2.imread(pic_name)
cv2.imshow('example',pic)
a=cv2.waitKey(0)

pic_preprocessed  = cv2.cvtColor(cv2.GaussianBlur(pic, (7,7), 0), cv2.COLOR_BGR2GRAY)