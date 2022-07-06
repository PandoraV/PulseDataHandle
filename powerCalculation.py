# %%
# coding=utf-8

from cProfile import label
from encodings import utf_8
import numpy as np
import csv

path_current = './data/ALL0000/F0000CH2.CSV'
path_voltage = './data/ALL0000/F0000CH1.CSV'
with open(path_voltage, mode='r') as f:
    data_current = np.loadtxt(f, str, delimiter=',')
    y_current_origin = data_current[:, 4]
    y_current_origin = [np.float64(i) for i in y_current_origin]
    # print(data[:, 4])
    f.close()
with open(path_current, mode='r') as f:
    data_voltage = np.loadtxt(f, str, delimiter=',')
    y_voltage_origin = data_voltage[:, 4]
    y_voltage_origin = [np.float64(i) for i in y_voltage_origin]
    # print(data[:, 4])
    f.close()

# %%
import statsmodels.api as sm 
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple scipy==1.2.1 --upgrade
lowess = sm.nonparametric.lowess
import matplotlib.pyplot as plt

n = 2500
x = np.linspace(0, 2500, n)
# yest = lowess(y, x)
y_current_handled = lowess(y_current_origin, x, frac=0.015)[:,1] # 选0.015
y_voltage_handled = lowess(y_voltage_origin, x, frac=0.015)[:,1] 

# %%
plt.figure()
ax1 = plt.subplot()
ax2 = ax1.twinx()
ax1.plot(x, y_voltage_handled, color='orange', label='voltage')
ax2.plot(x, y_current_handled, label='current')

ax1.set_ylabel('voltage', color='orange')
ax2.set_ylabel('current', color='b')
plt.legend()
plt.show()


# %%
power_origin = np.array([], dtype=np.float64)
for i in range(2500):
    temp_power = y_voltage_origin[i] * y_current_origin[i]
    power_origin = np.append(power_origin, temp_power)

# %%
plt.figure()
plt.plot(x, power_origin)
plt.legend()
plt.show()

# %%
power_handled = np.array([], dtype=np.float64)
for i in range(2500):
    temp_power = y_voltage_handled[i] * y_current_handled[i]
    power_handled = np.append(power_handled, temp_power)

# %%
plt.figure()
plt.plot(x, power_handled)
plt.legend()
plt.show()

# %%
