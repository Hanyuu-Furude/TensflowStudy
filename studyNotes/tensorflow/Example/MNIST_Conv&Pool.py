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

#卷积和池化
