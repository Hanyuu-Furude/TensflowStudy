import tensorflow as tf

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0)  # also tf.float32 implicitly
print(node1, node2)

sess = tf.Session()
print(sess.run([node1, node2]))

# from __future__ import print_function
node3 = tf.add(node1, node2)
print("node3:", node3)
print("sess.run(node3):", sess.run(node3))

# 占位符
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a, b)

print(sess.run(adder_node, {a: 3, b: 4.5}))
print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))

add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a: 3, b: 4.5}))

# 多个变量求值
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b

#  变量初始化
init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(linear_model, {x: [1, 2, 3, 4]}))

# loss function
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print("loss function", sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

ss = (0 - 0) * (0 - 0) + (0.3 + 1) * (0.3 + 1) + (0.6 + 2) * (0.6 + 2) + (0.9 + 3) * (0.9 + 3)  # 真实算法
print("真实算法ss", ss)

print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, 0.3, 0.6, 0.9]}))  # 测试参数

# ft.assign 变量重新赋值
fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])
sess.run([fixW, fixb])
print(sess.run(linear_model, {x: [1, 2, 3, 4]}))
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

# tf.train API
optimizer = tf.train.GradientDescentOptimizer(0.01)  # 梯度下降优化器
train = optimizer.minimize(loss)  # 最小化损失函数
sess.run(init)  # reset values to incorrect defaults.
for i in range(1000):
    sess.run(train, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})

print(sess.run([W, b]))