import tensorflow as tf
import numpy as np

xData = np.random.rand(100).astype('float32')
yData = xData * 2+3
w=tf.Variable(tf.random_uniform([1],-1.0,-1.0))
b=tf.Variable(tf.zeros([1]))
y=w*xData+b
loss=tf.reduce_mean(tf.square(y-yData))
optimizer=tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
init=tf.initialize_all_variables()
sess=tf.Session()
sess.run(init)
for x in range(2001):
    sess.run(train)
    print(x,sess.run(w),sess.run(b))

