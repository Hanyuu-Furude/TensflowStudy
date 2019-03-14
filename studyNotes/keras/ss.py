import keras
model = keras.models.Sequential()	#线性模型
model.add(keras.layers.Dense(32, activation='relu', input_dim=100))	#添加一个全连接层，relu，输入尺寸100
model.add(keras.layers.Dense(1, activation='sigmoid'))	#全连接层，sigmoid
model.compile(		#编译模型，多分类优化
	optimizer='rmsprop',
	loss='binary_crossentropy',
	metrics=['accuracy']
	)

import numpy as np
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))
model.fit(data,labels,epochs=10,batch_size=32)
