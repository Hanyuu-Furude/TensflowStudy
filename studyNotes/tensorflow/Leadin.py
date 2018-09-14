import tensorflow as tf

# from string import Template

node0 = tf.constant(20.0, dtype=tf.float32)
node1 = tf.constant(15.0)
print(node0)
sess = tf.Session()
print('node0,node1', sess.run([node0, node1]))
node2 = tf.add(node0, node1)
print('node2', sess.run(node2))
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a, b)
print(sess.run(adder_node, {a: [1,3], b: [2,4]}))