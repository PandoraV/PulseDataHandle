# %%
# coding=utf-8

from nis import cat
import os
import re
import numpy as np
import statsmodels.api as sm 
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple scipy==1.2.1 --upgrade
lowess = sm.nonparametric.lowess
import matplotlib.pyplot as plt

sortedPower = {}

path = './data'
parent_dir = os.listdir(path)
for child_dir in parent_dir:
    if child_dir == ".DS_Store":
        continue
    file_list = os.listdir(path + '/' + child_dir)
    for file_name in file_list:
        if file_name == ".DS_Store":
            continue
        searchObj = re.search(r'(.*).CSV', file_name, re.I|re.M)
        if searchObj:
            if (searchObj.group(0) == 'OUTPUT.CSV'):
                continue
            # 匹配到目标数据集
            target_path = path + '/' + child_dir + '/' + searchObj.group(0)
            # print(target_path)
            with open(target_path, mode='r') as f:
                data = np.loadtxt(f, str, delimiter=',')
                if searchObj.group(0)[7] == '1':
                    y1 = data[:, 4] # 电压
                else:
                    y2 = data[:, 4] # 电流
                # 记录采样间隔
                sample_interval = np.float64(data[1, 1])
                f.close()
    y = np.c_[y1, y2] # 要写入到文件里的数据
    storage_path = path + '/' + child_dir + '/' + "OUTPUT.CSV"
    np.savetxt(storage_path, y, delimiter=",", fmt="%s")

    # 开始处理OUTPUT.CSV
    n = 2500
    x = np.linspace(0, 2500, n)
    # yest = lowess(y, x)
    y_current_handled = lowess(y2, x, frac=0.015)[:,1] # 选0.015
    y_voltage_handled = lowess(y1, x, frac=0.015)[:,1] 

    # power_origin = np.array([], dtype=np.float64)
    # for i in range(2500):
    #     temp_power = np.float64(y1[i]) * np.float64(y2[i])
    #     power_origin = np.append(power_origin, temp_power)

    power_handled = np.array([], dtype=np.float64)
    for i in range(2500):
        temp_power = y_voltage_handled[i] * y_current_handled[i]
        power_handled = np.append(power_handled, temp_power)

    # 离散功率求和
    # total_power_origin = 0
    total_power_handled = 0
    for i in range(2500):
        # total_power_origin += power_origin[i]
        total_power_handled += power_handled[i]
    total_power_handled *= sample_interval
    # total_power_origin *= sample_interval

    # print("total power (handled) of %s is %f" % (child_dir, total_power_handled))
    # print("total power (origin) of %s is %f" % (child_dir, total_power_origin))

    # 加进列表
    sortedPower[child_dir] = total_power_handled


# %%
sortedPowerList = sorted(sortedPower.items())
num_of_powerList = len(sortedPowerList)
for i in range(num_of_powerList):
    print(sortedPowerList[i][1])

# %%
