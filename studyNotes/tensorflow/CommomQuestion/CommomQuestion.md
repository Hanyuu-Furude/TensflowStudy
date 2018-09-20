# CommomQuestion
> ## 使用GPU计算
>  若要使用Tensorflow-gpu，请检查您是否有**算力大于3的NVIDIA显卡**。
>   * 查询显卡算力[地址](https://developer.nvidia.com/cuda-gpus#collapseOne)。
>
> 若要使用CUDA加速计算，请确保您已安装[CUDA Toolkit](https://developer.nvidia.com/cuda-downloads),并且按需下载并配置您需要的[Deep learning frameworks](https://developer.nvidia.com/deep-learning-software),目前，我们用到的frameworks有[cuDNN](https://developer.nvidia.com/cudnn),请确保您的framework和CUDA版本配套，否则**无法使用**。


> ## ImportError: No module named input_data
> 由于版本更新，Tensorflow已经不建议再使用input_data.如果需要继续使用，请查看[input_data.py](../Example/input_data.py)