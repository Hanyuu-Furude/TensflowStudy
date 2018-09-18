import tensorflow as tf

# from string import Template

node0 = tf.constant(20.0, dtype=tf.float32)
node1 = tf.constant(15.0)
print(node0)
sess = tf.Session()
with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    with tf.device('/cpu:0'):
        print('node0,node1', sess.run([node0, node1]))
        node2 = tf.add(node0, node1)
        print('node2', sess.run(node2))
        a = tf.placeholder(tf.float32)
        b = tf.placeholder(tf.float32)
        adder_node = a + b  # + provides a shortcut for tf.add(a, b)
        print(sess.run(adder_node, {a: [1,3], b: [2,4]}))
        W = tf.Variable([.3], dtype=tf.float32)
        b = tf.Variable([-.3], dtype=tf.float32)
        x = tf.placeholder(tf.float32)
        linear_model = W*x + b
        init = tf.global_variables_initializer()
        print(sess.run(init))
        print('liner model', linear_model)
        print('calculate',sess.run(linear_model, {x: [1, 2, 3, 4]}))
        y = tf.placeholder(tf.float32)
        squared_deltas = tf.square(linear_model - y)
        loss = tf.reduce_sum(squared_deltas)
        print(sess.run(loss, {x: [1,2,3,4], y: [0, -1, -2, -3]}))
        optimizer = tf.train.GradientDescentOptimizer(0.01)
        train = optimizer.minimize(loss)
        sess.run(init)# reset values to incorrect defaults.
        for i in range(1000):
           sess.run(train, {x: [1,2,3,4], y: [0, -1, -2, -3]})
           #print(sess.run([W, b]))
        print(sess.run([W, b]))
        sess.close()