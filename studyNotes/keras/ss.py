import keras.backend as K
import numpy as np
from keras import Sequential
from keras.layers import Dense, Activation
import keras
################################################################################
# # 多分类问题
# model.compile(optimizer='rmsprop',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])

# # 二分类问题
# model.compile(optimizer='rmsprop',
#               loss='binary_crossentropy',
#               metrics=['accuracy'])

# # 均方误差回归问题
# model.compile(optimizer='rmsprop',
#               loss='mse')

# # 自定义评估标准函数


# def mean_pred(y_true, y_pred):
#     return K.mean(y_pred)


# model.compile(optimizer='rmsprop',
#               loss='binary_crossentropy',
#               metrics=['accuracy', mean_pred])
################################################################################
# model = keras.models.Sequential()  # 线性模型
# model.add(keras.layers.Dense(32, activation='relu',
#                              input_dim=100))  # 添加一个全连接层，relu，输入尺寸100
# model.add(keras.layers.Dense(1, activation='sigmoid'))  # 全连接层，sigmoid
# model.compile(  # 编译模型，多分类优化
#     optimizer='rmsprop',
#     loss='binary_crossentropy',
#     metrics=['accuracy']
# )

# data = np.random.random((1000, 100))
# labels = np.random.randint(2, size=(1000, 1))

################################################################################

# model.fit(data, labels, epochs=10, batch_size=32)

# model = Sequential()
# model.add(Dense(32, activation='relu', input_dim=100))
# model.add(Dense(10, activation='softmax'))
# model.compile(optimizer='rmsprop',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])

# # 生成虚拟数据
# data = np.random.random((1000, 100))
# labels = np.random.randint(10, size=(1000, 1))

# # 将标签转换为分类的 one-hot 编码
# one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)

# # 训练模型，以 32 个样本为一个 batch 进行迭代
# model.fit(data, one_hot_labels, epochs=10, batch_size=32)
################################################################################
# #基于多层感知器 (MLP) 的 softmax 多分类：

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

# 生成虚拟数据
import numpy as np
x_train = np.random.random((1000, 20))
y_train = keras.utils.to_categorical(
    np.random.randint(10, size=(1000, 1)), num_classes=10)  # 将标签转化为one hot https://blog.csdn.net/nima1994/article/details/82468965
x_test = np.random.random((100, 20))
y_test = keras.utils.to_categorical(
    np.random.randint(10, size=(100, 1)), num_classes=10)

model = Sequential()
# Dense(64) 是一个具有 64 个隐藏神经元的全连接层。
# 在第一层必须指定所期望的输入数据尺寸：
# 在这里，是一个 20 维的向量。
model.add(Dense(64, activation='relu', input_dim=20))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)	# 随机梯度下降
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=20,
          batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)
