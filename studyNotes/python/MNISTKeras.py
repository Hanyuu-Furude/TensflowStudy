# MNISTKeras.py
# 引入 TensorFlow 库
import tensorflow as tf
# 引入 mnist 数据集
mnist = tf.keras.datasets.mnist
# 载入训练集和测试集
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
# 建立 Keras 序列模型
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
# 编译模型，optimizer 优化函数，loss 损失函数,metrics 评价标准
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
# 训练模型
model.fit(x_train, y_train, epochs=8)
# 评估模型
model.evaluate(x_test, y_test)
