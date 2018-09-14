# Leadin
* 演示程序请参照Leadin.py

``` py
import tensorflow as tf 
```
* 常量
``` py
import tensorflow as tf 
node0 = tf.constant(3.0,dtype=tf.float32)
node1 = tf.constant(3.0,dtype)# also tf.float32 implicitly
```
* 会话
``` py
sess = tf.Session()
print(sess.run([node0,node1]))
```
* 相加计算
``` py
node2 = tf.add(node0, node1)
print('node2', sess.run(node2))
```
* Placeholder占位符
``` py
    a = tf.placeholder(tf.float32)
    b = tf.placeholder(tf.float32)
    adder_node = a + b  # + provides a shortcut for tf.add(a, b)
```
* feed_dict
```  py
    print(sess.run(adder_node, {a:3, b:4.5}))
    print(sess.run(adder_node, {a: [1,3], b: [2,4]}))
```