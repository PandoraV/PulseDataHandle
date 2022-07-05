# %%
# coding=utf-8

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
yest = lowess(y, x, frac=0.008)[:,1]

plt.figure()
plt.clf()
plt.plot(x, y, label='y noisy')
plt.plot(x, yest, label='y pred')
plt.legend()
plt.show()

# %%
