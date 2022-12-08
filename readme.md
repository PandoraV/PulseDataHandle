# 单高压脉冲数据处理

| 修订时间   | 修订版本 | 修订内容 |
| ---       | ---      | --- |
|2022-06-23 | v0.1      |初始版本|
|2022-07-08 | v0.2      |使用Python进行文件批处理并加入Python计算与绘图|
|2022-07-08 | v0.3      |新增FAQ|

## 文件构成

- `dataRead`: 读取单文件中数据并执行滤波，用于测试滤波算法性能并测试绘图；

- `pathAccess`: 遍历指定目录下的`CSV`文件并读取其中文本数据，并将同一文件夹下的电压电流数据从两个`CSV`文件中分别提取出来，放进新数据集`OUTPUT.CSV`中，顺序固定为第一列为电压，第二列为电流；

- `powerCalculation`: 从`OUTPUT.CSV`中提取电压电流数据并滤波，滤波后计算原始功率和滤波后功率。注意，Python版本不包含从`OUTPUT.CSV`中计算的内容。

## **开始**

1. 处理单个波形数据文件时，打开`dataRead.py`/`ReadData.m`，读取单个波形图并执行滤波操作，然后绘制滤波前后波形；

2. 处理多个波形数据文件时，打开`pathAccess.py`/`fileProcessing.m`，执行滤波操作并整理电压电流至同一个文件；然后执行`powerCaculation.py`/`PowerCalculation.m`，对单个`OUTPUT.CSV`文件进行处理；`batchPowerCaculation`文件用以批量处理`OUTPUT.CSV`文件，并计算功率。

## 滤波算法

MATLAB使用的滤波算法是`rlowess`，Python使用的是`numpy`库带的`lowess`方法。参数设置如下：

- MATLAB窗宽为`30`

- Python中`frac`参数取`0.015`，多项式拟合阶数为`3`

---

## FAQ

* 在导入lowess计算包的时候报错：

```
ImportError: cannot import name 'factorial' from 'scipy.misc'
```

往往是因为版本不兼容引起的，需要降级，在`terminal`内操作。

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple scipy==1.2.1 --upgrade
```

Ref: [mumujunV5的博客-CSDN博客](https://blog.csdn.net/youruolinmc/article/details/104548407/)

* `numpy`包的`savetxt`函数报错：

```
Mismatch between array dtype ('＜U40') and format specifier ('%.18e')
```

解决方案为在`numpy.savetxt()`函数中增加参数`fmt='%s'`，示例：

```python
np.savetxt("file.csv", staticData, delimiter=',', fmt='%s')
```

Ref: [王大渣的博客-CSDN博客](https://blog.csdn.net/qq_41221841/article/details/109571665)

* `CSV`文件读取相关错误：

请注意处理多文件的时候务必符合文件命名要求和路径要求。