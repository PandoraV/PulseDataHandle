# %%
# coding=utf-8

from nis import cat
import os
import re
import numpy as np

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
                    y1 = data[:, 4]
                else:
                    y2 = data[:, 4]
                f.close()
    y = np.c_[y1, y2] # 要写入到文件里的数据
    storage_path = path + '/' + child_dir + '/' + "OUTPUT.CSV"
    np.savetxt(storage_path, y, delimiter=",", fmt="%s")

# %%
