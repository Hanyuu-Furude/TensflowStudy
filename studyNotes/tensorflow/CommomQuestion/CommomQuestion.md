# CommomQuestion
> ## <font color=red>**使用VSCode运行openCV劝退事宜**</font>
> 您若使用VSCode尝试Debug openCV-Python，<font color=red>我们**强烈**建议您立刻放弃这样的尝试</font>。因为目前VSCode插件pylint无法正常解析openCV-python.[详情请见VSCode团队官方issue](https://github.com/Microsoft/vscode/issues/46798)\
>推荐使用[PyCharm](https://www.jetbrains.com/pycharm/)或者[Vim(高级玩家限定)](https://www.vim.org/)

> ## 使用GPU计算
>  若要使用Tensorflow-gpu，请检查您是否有**算力大于3的NVIDIA显卡**。
>   * 查询显卡算力[地址](https://developer.nvidia.com/cuda-gpus#collapseOne)。
>
> 若要使用CUDA加速计算，请确保您已安装[CUDA Toolkit](https://developer.nvidia.com/cuda-downloads),并且按需下载并配置您需要的[Deep learning frameworks](https://developer.nvidia.com/deep-learning-software),目前，我们用到的frameworks有[cuDNN](https://developer.nvidia.com/cudnn),请确保您的framework和CUDA版本配套，否则**无法使用**。


> ## ImportError: No module named input_data
> 由于版本更新，Tensorflow已经不建议再使用input_data.如果需要继续使用，请查看[input_data.py](../Example/input_data.py)