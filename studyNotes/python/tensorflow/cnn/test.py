import numpy as np
import tensorflow as tf
import sys
import os
from matplotlib import pyplot as plt

fig_size = [15, 4]
plt.rcParams["figure.figsize"] = fig_size

import urllib.request

slim = tf.contrib.slim

# from nets import vgg
from tensorflow.contrib.slim.nets import vgg
# from preprocessing import vgg_preprocessing
from keras_preprocessing import vgg_preprocessing
# 加载像素均值以及为每个像素进行减法运算的函数
from preprocessing.vgg_preprocessing import (_mean_image_subtraction,
                                            _R_MEAN, _G_MEAN, _B_MEAN)

upsample_factor = 32
number_of_classes = 2
log_folder = '/home/dpakhom1/tf_projects/segmentation/log_folder'

vgg_checkpoint_path = os.path.join(checkpoints_dir, 'vgg_16.ckpt')

# 在与像素均值做差前，将图像转换至float32类型
image_float = tf.to_float(image_tensor, name='ToFloat')

# 将每个像素的具体数值与像素均值做差
mean_centered_image = _mean_image_subtraction(image_float,
                                          [_R_MEAN, _G_MEAN, _B_MEAN])

processed_images = tf.expand_dims(mean_centered_image, 0)

upsample_filter_np = bilinear_upsample_weights(upsample_factor,
                                               number_of_classes)

upsample_filter_tensor = tf.constant(upsample_filter_np)

# 定义将要使用的模型——指定在最后一层仅使用两个类别
with slim.arg_scope(vgg.vgg_arg_scope()):

    logits, end_points = vgg.vgg_16(processed_images,
                           num_classes=2,
                           is_training=is_training_placeholder,
                           spatial_squeeze=False,
                           fc_conv_padding='SAME')

downsampled_logits_shape = tf.shape(logits)

# 计算上采样数据的输出大小
upsampled_logits_shape = tf.pack([
                                  downsampled_logits_shape[0],
                                  downsampled_logits_shape[1] * upsample_factor,
                                  downsampled_logits_shape[2] * upsample_factor,
                                  downsampled_logits_shape[3]
                                 ])

# 进行上采样处理
upsampled_logits = tf.nn.conv2d_transpose(logits, upsample_filter_tensor,
                                 output_shape=upsampled_logits_shape,
                                 strides=[1, upsample_factor, upsample_factor, 1])

# 展开预测结果，以便于我们计算每个像素的交叉熵，并获得交叉熵的总和
flat_logits = tf.reshape(tensor=upsampled_logits, shape=(-1, number_of_classes))

cross_entropies = tf.nn.softmax_cross_entropy_with_logits(logits=flat_logits,
                                                          labels=flat_labels)

cross_entropy_sum = tf.reduce_sum(cross_entropies)

# 获得每个像素的最终预测结果——请注意，在这种情况下我们并不需要
# 使用softmax，因为我们只需要得到最终的决策。如果我们还需要各
# 个类别的概率，那么我们必须应用softmax
pred = tf.argmax(upsampled_logits, dimension=3)

probabilities = tf.nn.softmax(upsampled_logits)

# 在这里我们定义了一个优化器，并添加了所有将要创建至命名
# 空间'adam_vars'下的变量。这样做有利于我们后续轻松地访问
# 它们。这些变量供adam优化器使用，并且与vgg模型中的变量无关

# 我们还获得了每个变量的梯度数据
# 这样，我们可以在tensorboard中可视化这些变量
# optimizer.compute_gradients与optimizer.apply_gradients
# 等价于执行：
# train_step = tf.train.AdamOptimizer(learning_rate=0.0001).minimize(cross_entropy_sum)
with tf.variable_scope("adam_vars"):
    optimizer = tf.train.AdamOptimizer(learning_rate=0.0001)
    gradients = optimizer.compute_gradients(loss=cross_entropy_sum)

    for grad_var_pair in gradients:

        current_variable = grad_var_pair[1]
        current_gradient = grad_var_pair[0]

        # 替换原始变量名中的一些字符
        # tensorboard不支持':'符号
        gradient_name_to_save = current_variable.name.replace(":", "_")

        # 得到每一层的梯度直方图，并随后在tensorboard中可视化这些数据
        tensorboard
        tf.summary.histogram(gradient_name_to_save, current_gradient)

    train_step = optimizer.apply_gradients(grads_and_vars=gradients)

# 在这里，我们定义了一个函数，调用时会从VGG模型检查点中读取权重数据，并加载至变量中。
# 我们从负责类别预测的最后一层中剔除了权重。我们这样做是因为我们将有不同数量的
# 类别进行预测，我们不能在初始化时使用原先的类别。
vgg_except_fc8_weights = slim.get_variables_to_restore(exclude=['vgg_16/fc8', 'adam_vars'])

# 这里我们得到了网络中最后一层的权重变量
# 正如我们看到的，VGG最初训练的类别数量与我们实际的类别数量
# 并不相同——在我们的情况下，总共只有两类
vgg_fc8_weights = slim.get_variables_to_restore(include=['vgg_16/fc8'])

adam_optimizer_variables = slim.get_variables_to_restore(include=['adam_vars'])

# 为模型损失添加一个summary OP——以便我们可以在tensorboard中看到它
tf.summary.scalar('cross_entropy_loss', cross_entropy_sum)

# 将所有summary OP合并至一个OP总
# 在运行程序时生成字符串
merged_summary_op = tf.summary.merge_all()

# 创建一个summary writer——用于将所有日志写入到一个特定文件中
# 这个文件后续可以由tensorboard读取
summary_string_writer = tf.summary.FileWriter(log_folder)

# 如果日志文件夹尚未存在，则创建一个新的文件夹
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# 创建一个OP，对VGG模型中各权重变量进行初始化操作
read_vgg_weights_except_fc8_func = slim.assign_from_checkpoint_fn(
                                   vgg_checkpoint_path,
                                   vgg_except_fc8_weights)

# 针对新的fc8层权重数据的初始化器——仅包括两类
vgg_fc8_weights_initializer = tf.variables_initializer(vgg_fc8_weights)

# adam变量的初始化器
optimization_variables_initializer = tf.variables_initializer(adam_optimizer_variables)

with tf.Session() as sess:
    # 运行初始化器
    read_vgg_weights_except_fc8_func(sess)
    sess.run(vgg_fc8_weights_initializer)
    sess.run(optimization_variables_initializer)

    train_image, train_annotation = sess.run([image_tensor, annotation_tensor],
                                              feed_dict=feed_dict_to_use)

    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.imshow(train_image)
    ax1.set_title('Input image')
    probability_graph = ax2.imshow(np.dstack((train_annotation,)*3)*100)
    ax2.set_title('Input Ground-Truth Annotation')
    plt.show()

    # 执行10次迭代
    for i in range(10):

        loss, summary_string = sess.run([cross_entropy_sum, merged_summary_op],
                                        feed_dict=feed_dict_to_use)

        sess.run(train_step, feed_dict=feed_dict_to_use)

        pred_np, probabilities_np = sess.run([pred, probabilities],
                                              feed_dict=feed_dict_to_use)

        summary_string_writer.add_summary(summary_string, i)

        cmap = plt.get_cmap('bwr')

        f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
        ax1.imshow(np.uint8(pred_np.squeeze() != 1), vmax=1.5, vmin=-0.4, cmap=cmap)
        ax1.set_title('Argmax. Iteration # ' + str(i))
        probability_graph = ax2.imshow(probabilities_np.squeeze()[:, :, 0])
        ax2.set_title('Probability of the Class. Iteration # ' + str(i))

        plt.colorbar(probability_graph)
        plt.show()

        print("Current Loss: " +  str(loss))

    feed_dict_to_use[is_training_placeholder] = False

    final_predictions, final_probabilities, final_loss = sess.run([pred,
                                                                   probabilities,
                                                                   cross_entropy_sum],
                                                         feed_dict=feed_dict_to_use)


    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

    ax1.imshow(np.uint8(final_predictions.squeeze() != 1),
               vmax=1.5,
               vmin=-0.4,
               cmap=cmap)

    ax1.set_title('Final Argmax')


    probability_graph = ax2.imshow(final_probabilities.squeeze()[:, :, 0])
    ax2.set_title('Final Probability of the Class')
    plt.colorbar(probability_graph)

    plt.show()

    print("Final Loss: " +  str(final_loss))

summary_string_writer.close()