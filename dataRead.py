# %%
# coding=utf-8

from cProfile import label
from encodings import utf_8
import numpy as np
import csv

path = './data/ALL0000/F0000CH2.CSV'
with open(path, mode='r') as f:
    data = np.loadtxt(f, str, delimiter=',')
    y = data[:, 4]
    y = [np.float64(i) for i in y]
    # print(data[:, 4])
    f.close()

# %%

import statsmodels.api as sm
lowess = sm.nonparametric.lowess
import matplotlib.pyplot as plt

n = 2500
x = np.linspace(0, 2500, n)
# yest = lowess(y, x)
y1 = lowess(y, x, frac=0.015)[:,1] # 选0.015

plt.figure()
plt.clf()
# plt.plot(x, y, label='y noisy')
plt.plot(x, y1, label='frac=0.015')
plt.legend()
plt.show()


# %%
# SG法
# Savitzky-Golay filter 平滑 
from scipy.signal import savgol_filter
zs=savgol_filter(y, 51, 3) # window size 51, polynomial order 3
# 第一个参数是窗宽，越宽滤波后的波形毛刺越少，第二个是拟合多项式阶数，越高保留变化越多
plt.figure()
# plt.plot(x,y)
plt.title('Savitzky-Golay filter')
plt.plot(x,zs,color='r',lw=1)
plt.show()

# %%
# 将lowess和SG法滤波后波形放在一起比较
plt.figure()
plt.plot(x, y1, label='lowess')
plt.plot(x, zs, label='SG')
plt.legend()
plt.show()

# %%
