import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
 
mnist = read_data_sets("MNIST_data/", one_hot=True)
 
x = tf.placeholder('float', [None, 28*28])
y_ = tf.placeholder('float', [None, 10])
 
# 自定义全连接
# W = tf.Variable(tf.zeros([784, 10]))
# b = tf.Variable(tf.zeros([10]))
# logits = tf.matmul(x, W) + b
 
# cnn模型
x_image = tf.reshape(x, [-1,28,28,1])
w_init = tf.truncated_normal_initializer(stddev=0.1, seed=9)
b_init = tf.constant_initializer(0.1)
cnn1 = tf.layers.conv2d(x_image, 32, (5,5), padding='same', activation=tf.nn.relu, \
	kernel_initializer=w_init, bias_initializer=b_init)
mxpl1 = tf.layers.max_pooling2d(cnn1, 2, strides=2, padding='same')
cnn2 = tf.layers.conv2d(mxpl1, 64, (5,5), padding='same', activation=tf.nn.relu, \
	kernel_initializer=w_init, bias_initializer=b_init)
mxpl2 = tf.layers.max_pooling2d(cnn2, 2, strides=2, padding='same')
mxpl2_flat = tf.reshape(mxpl2, [-1,7*7*64])
fc1 = tf.layers.dense(mxpl2_flat, 1024, activation=tf.nn.relu, \
	kernel_initializer=w_init, bias_initializer=b_init)
keep_prob = tf.placeholder('float')
fc1_drop = tf.nn.dropout(fc1, keep_prob)
logits = tf.layers.dense(fc1_drop, 10, kernel_initializer=w_init, bias_initializer=b_init)
 
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_))
optmz = tf.train.AdamOptimizer(1e-4)
train_op = optmz.minimize(loss)
 
def get_eval_op(logits, labels):
	corr_prd = tf.equal(tf.argmax(logits,1), tf.argmax(labels,1))
	return tf.reduce_mean(tf.cast(corr_prd, 'float'))
eval_op = get_eval_op(logits, y_)
 
init = tf.initialize_all_variables()
 
# summary
logdir = './logs/m4d1'
def summary_op(datapart='train'):
	tf.summary.scalar(datapart + '-loss', loss)
	tf.summary.scalar(datapart + '-eval', eval_op)
	return tf.summary.merge_all()	
summary_op_train = summary_op()
summary_op_test = summary_op('test')
# whether to restore or not
ckpts_dir = 'ckpts/'
ckpt_nm = 'cnn-ckpt'
saver = tf.train.Saver(max_to_keep=50) # defaults to save all variables, using dict {'x':x,...} to save specified ones.
restore_step = ''
start_step = 0
train_steps = 100*200
best_loss = 1e6
best_step = 0
 
# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"
# config = tf.ConfigProto()  
# config.gpu_options.per_process_gpu_memory_fraction = 0.9
# config.gpu_options.allow_growth=True # allocate when needed
# with tf.Session(config=config) as sess:
with tf.Session() as sess:
	sess.run(init)
	if restore_step:
		ckpt = tf.train.get_checkpoint_state(ckpts_dir)
		if ckpt and ckpt.model_checkpoint_path: # ckpt.model_checkpoint_path means the latest ckpt
			if restore_step == 'latest':
				ckpt_f = tf.train.latest_checkpoint(ckpts_dir)
				start_step = int(ckpt_f.split('-')[-1]) + 1
			else:
				ckpt_f = ckpts_dir+ckpt_nm+'-'+restore_step
			print('loading wgt file: '+ ckpt_f)
			saver.restore(sess, ckpt_f) 
	summary_wrt = tf.summary.FileWriter(logdir,sess.graph)
	if restore_step in ['', 'latest']:
		for i in range(start_step, train_steps):
			batch_x, batch_y = mnist.train.next_batch(50)
			_, cur_loss, cur_train_eval, summary = sess.run([train_op, loss, eval_op, summary_op_train], \
						feed_dict={x: batch_x, y_: batch_y, keep_prob: 0.5} )
			# log to stdout and eval test set
			if i % 100 == 0 or i == train_steps-1:
				if cur_loss < best_loss:
					best_loss = cur_loss
					best_step = i
				saver.save(sess, ckpts_dir+ckpt_nm, global_step=i) # save variables
				summary_wrt.add_summary(summary, global_step=i)
				cur_test_eval, summary = sess.run([eval_op, summary_op_test], feed_dict={x:mnist.test.images, \
						y_:mnist.test.labels, keep_prob: 1.0})
				summary_wrt.add_summary(summary, global_step=i)
				print( 'step %5d, loss %.5f, acc train %.5f, acc test %.5f'%(i, \
					cur_loss, cur_train_eval, cur_test_eval))
		with open(ckpts_dir+'best.step','w') as f:
			f.write('best step is %d\n'%best_step)
		print ('best step is %d'%best_step)
	else:
		test_loss, test_eval = sess.run([loss, eval_op], feed_dict={x:mnist.test.images, \
						y_:mnist.test.labels, keep_prob: 1.0})
		print ('eval test: loss %.5f, acc %.5f'%(test_loss, test_eval))
		