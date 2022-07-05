# coding=utf-8

import os
import re

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