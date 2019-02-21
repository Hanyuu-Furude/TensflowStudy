import numpy as np
import skimage.io as io
import tensorflow as tf
import sys
import os
# from __future__ import division
# import division
%matplotlib inline


os.environ["CUDA_VISIBLE_DEVICES"] = '1'
sys.path.append("/home/dpakhom1/workspace/my_models/slim/")
checkpoints_dir = '/home/dpakhom1/checkpoints'

image_filename = 'cat.jpg'
annotation_filename = 'cat_annotation.png'

image_filename_placeholder = tf.placeholder(tf.string)
annotation_filename_placeholder = tf.placeholder(tf.string)
is_training_placeholder = tf.placeholder(tf.bool)

feed_dict_to_use = {image_filename_placeholder: image_filename,
                    annotation_filename_placeholder: annotation_filename,
                    is_training_placeholder: True}

image_tensor = tf.read_file(image_filename_placeholder)
annotation_tensor = tf.read_file(annotation_filename_placeholder)

image_tensor = tf.image.decode_jpeg(image_tensor, channels=3)
annotation_tensor = tf.image.decode_png(annotation_tensor, channels=1)

# 对于每个类别，将其设置为1而不是一个数字——我们在后续计算
# 交叉熵时会用到。有的时候，实际分割区域的掩码可以有很多值，
# 不仅仅为0和1
class_labels_tensor = tf.equal(annotation_tensor, 1)
background_labels_tensor = tf.not_equal(annotation_tensor, 1)

#将布尔值转换为浮点数——这样才能正确地计算交叉熵损失
bit_mask_class = tf.to_float(class_labels_tensor)
bit_mask_background = tf.to_float(background_labels_tensor)

combined_mask = tf.concat(concat_dim=2, values=[bit_mask_class,
                                                bit_mask_background])

# 调整输入数据的大小，使其与tf.softmax_cross_entropy_with_logits中
# [batch_size, num_classes]的要求保持一致
flat_labels = tf.reshape(tensor=combined_mask, shape=(-1, 2))
