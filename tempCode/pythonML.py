import numpy as np
def gradientDescend(feature,label,maxCycle,alpha):
    '''利用梯度下降训练LR模型
    input:
        freture(mat)特征;
        label(mat)标签;
        maxCycle(mat)最大迭代次数;
        alpha（float)学习率；
    output:
        w(mat)权重
    '''
    n=np.shape(feature)[1] # 特征个数
    w=np.mat(np.ones((n,1))) # 初始化权重
    i=0
    while i<=maxCycle: # 计算Sigmoid
        i+=1
        a=siq(feature * w) # 计算Sigmoid值
        err=label:
