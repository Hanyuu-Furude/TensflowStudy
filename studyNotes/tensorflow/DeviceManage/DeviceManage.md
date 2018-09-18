# DeciveManage
``` py
import tensorflow as tf
#选择设备 CPU->CPU:0
with tf.device('/gpu:1'):
    v1 = tf.constant([1.0, 2.0, 3.0], shape=[3], name='v1')
    v2 = tf.constant([1.0, 2.0, 3.0], shape=[3], name='v2')
    sumV12 = v1 + v2
    #config=tf.ConfigProto(log_device_placement=True)打印执行操作所用的设备
    with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
        print sess.run(sumV12)
```
