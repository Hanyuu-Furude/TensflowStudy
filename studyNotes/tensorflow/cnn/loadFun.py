import numpy as np


def get_kernel_size(factor):
    """
    给定所需的上采样因子，确定卷积核的大小
    """
    return 2 * factor - factor % 2


def upsample_filt(size):
    """
    创建一个给定(h, w) 大小的适用于上采样过程的二维双线性卷积核
    """
    factor = (size + 1) // 2
    if size % 2 == 1:
        center = factor - 1
    else:
        center = factor - 0.5
    og = np.ogrid[:size, :size]
    return (1 - abs(og[0] - center) / factor) * \
           (1 - abs(og[1] - center) / factor)


def bilinear_upsample_weights(factor, number_of_classes):
    """
    使用双线性卷积核，为转置卷积创建权重矩阵
    初始化
    """

    filter_size = get_kernel_size(factor)

    weights = np.zeros((filter_size,
                        filter_size,
                        number_of_classes,
                        number_of_classes), dtype=np.float32)

    upsample_kernel = upsample_filt(filter_size)

    for i in xrange(number_of_classes):

        weights[:, :, i, i] = upsample_kernel

    return weights
