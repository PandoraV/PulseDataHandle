# %%
# coding=utf-8

from nis import cat
import os
import re
import numpy as np

storage_flag = False

path = './data'
parent_dir = os.listdir(path)
for child_dir in parent_dir:
    file_list = os.listdir(path + '/' + child_dir)
    for file_name in file_list:
        searchObj = re.search(r'(.*).CSV', file_name, re.I|re.M)
        if searchObj:
            # 匹配到目标数据集
            target_path = path + '/' + child_dir + '/' + searchObj.group(0)
            # print(target_path)
            with open(target_path, mode='r') as f:
                data = np.loadtxt(f, str, delimiter=',')
                if storage_flag is False:
                    y1 = data[:, 4]
                    # y1.reshape(2500, 1)
                    storage_flag = True
                else:
                    y2 = data[:, 4]
                    storage_flag = False
                f.close()
    y = np.c_[y1, y2] # 要写入到文件里的数据
    storage_path = path + '/' + child_dir + '/' + "OUTPUT.CSV"
    np.savetxt(storage_path, y, delimiter=",", fmt="%s")

# %%
