import tensorflow as tf
import numpy as np
w=tf.Variable(0,dtype=tf.float32)

cost=tf.add(tf.add(w ** 2.,tf.multiply(-10.,w)),25)
train=tf.train.GradientDescentOptimizer(0.01).minimize(cost)
init =tf.global_variables_initializer()
session=tf.Session()
session.run(init)
session.run(w)
session.run(train)
print(session.run(w))
for i in range (1000):
    session.run(train)
    if (i%100==0):
        print(session.run(w))