# Author:Hanyuu
# Date:20180919
# Leadin.py

import tensorflow as tf
import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
sess = tf.InteractiveSession()

# Softmax Model
# shape参数可选，定义形状可以判别出数据错误
# 训练数据x
x = tf.placeholder("float", shape=[None, 784])
# 训练数据y_hat
y_ = tf.placeholder("float", shape=[None, 10])
# 权重W
W = tf.Variable(tf.zeros([784, 10]))
# 偏重b
b = tf.Variable(tf.zeros([10]))

# 初始化所有变量
# sess.run(tf.initialize_all_variables())
sess.run(tf.global_variables_initializer())

# 计算SoftMax概率值
y = tf.nn.softmax(tf.matmul(x, W) + b)

# 损失函数loss定义(交叉熵）
# Tips:miniBatch=all
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

# 使用梯度下降法降低交叉熵
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

# 训练循环次数（1000））
for i in range(1000):
	# 从mnist数据集获取下50个变量
	batch = mnist.train.next_batch(50)
	# 运行梯度下降更新参数
	# tips:feed_dict可以替代任何张量
	train_step.run(feed_dict={x: batch[0], y_: batch[1]})

# 评估模型
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# 计算精度
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
# 计算测试集准确率
print("Accuracy on test set: ", accuracy.eval(
	feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
