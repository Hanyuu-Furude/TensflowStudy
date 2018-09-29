# MNIST_ConvPool.py
# MNIST多层卷积网络

import tensorflow as tf


# 权重初始化
def weight_variable(shape):
	initial = tf.truncated_normal(shape, stddev=0.1)
	return tf.Variable(initial)


# 偏置初始化
def bias_variable(shape):
	initial = tf.constant(0.1, shape=shape)
	return tf.Variable(initial)


# 卷积和池化
# 最大池化，转化为2d
def conv2d(x, W):
	return tf.nn.max_pool(x, W, strides=[1, 1, 1, 1], padding='SAME')

#最大池化，2x2
def max_pool_2x2(x):
	return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
