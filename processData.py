# %%
# coding=utf-8
'''
    本程序适用于SIGLENT品牌示波器的CSV格式的波形数据文件的处理和图像绘制
    样例使用的示波器型号为SDS2502X Plus
'''
# 读取文件

f = open("SDS2502X Plus_CSV_C1_1.csv", "r") # 通道1是电流
# f = open("test.CSV")

s = f.readline()
RecordLength = int(s.split(',')[1].split(':')[1]) # 记录总数据个数

s = f.readline()
SampleInterval = float(s.split(',')[1].split(':')[1]) # 采样间隔

s = f.readline()
VerticalUnits = s.split(',')[1].split(':')[1] # 纵轴单位

s = f.readline()
VerticalScale = float(s.split(',')[1].split(':')[1]) # 纵轴分度

s = f.readline()
VerticalOffset = float(s.split(',')[1].split(':')[1]) # 纵轴触发点

s = f.readline()
HorizontalUnits = s.split(',')[1] # 横轴单位

s = f.readline()
HorizontalScale = float(s.split(',')[1]) # 横轴分度

s = f.readline()
Model = s.split(',')[1]

s = f.readline()
SerialNumber = s.split(',')[1]

s = f.readline()
SoftwareVersion = s.split(',')[1]

s = f.readline()
Source = s.split(',')[1]

s = f.readline() # 结束

# %%
time_data = []
value_data_current = []
s = f.readline()
original_time_point, temp_value = s.split(',')
original_time_point = eval(original_time_point)

while s:
    temp_time, temp_value = s.split(',')
    temp_time_ms = 1000 * (eval(temp_time) - original_time_point)
    time_data.append(temp_time_ms)
    temp_value_mA = eval(temp_value) * 5
    value_data_current.append(temp_value_mA)
    s = f.readline()

f.close()

# %%
# 数据切片

left_horizon_plot = 120000
right_horizon_plot = left_horizon_plot + 799999
data_for_plot_current = value_data_current[left_horizon_plot:right_horizon_plot]
time_for_plot = time_data[left_horizon_plot:right_horizon_plot]

# %%
import matplotlib.pyplot as plt

plt.figure(dpi=300)
ax1 = plt.subplot()
# ax2 = ax1.twinx()
ax1.plot(time_for_plot, data_for_plot_current, linewidth=0.1, color='orange', label='current')
# ax2.plot(x, y_current_handled, label='current')

ax1.set_ylabel('current')
# ax2.set_ylabel('current', color='b')
plt.legend()
plt.show()

# --------------------------------------------------------------------


# %%
# 读电压文件
f = open("SDS2502X Plus_CSV_C2_1.csv", "r")
# f = open("test.CSV")

s = f.readline()
RecordLength = int(s.split(',')[1].split(':')[1]) # 记录总数据个数

s = f.readline()
SampleInterval = float(s.split(',')[1].split(':')[1]) # 采样间隔

s = f.readline()
VerticalUnits = s.split(',')[1].split(':')[1] # 纵轴单位

s = f.readline()
VerticalScale = float(s.split(',')[1].split(':')[1]) # 纵轴分度

s = f.readline()
VerticalOffset = float(s.split(',')[1].split(':')[1]) # 纵轴触发点

s = f.readline()
HorizontalUnits = s.split(',')[1] # 横轴单位

s = f.readline()
HorizontalScale = float(s.split(',')[1]) # 横轴分度

s = f.readline()
Model = s.split(',')[1]

s = f.readline()
SerialNumber = s.split(',')[1]

s = f.readline()
SoftwareVersion = s.split(',')[1]

s = f.readline()
Source = s.split(',')[1]

s = f.readline() # 结束

# %%
# 读电压
# time_data = []
value_data_voltage = []
s = f.readline()

while s:
    temp_time, temp_value = s.split(',')
    # time_data.append(eval(temp_time))
    temp_value_kV = 4.501 * eval(temp_value)
    value_data_voltage.append(temp_value_kV)
    s = f.readline()

f.close()

# %%
# 对电压波形平滑处理
'''
import statsmodels.api as sm 
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple scipy==1.2.1 --upgrade
lowess = sm.nonparametric.lowess
import numpy as np

n = RecordLength
x = np.linspace(0, 2500, n)
# yest = lowess(y, x)
y_voltage_handled = lowess(value_data_voltage, x, frac=0.015)[:,1] # 选0.015

plt.figure()
ax1 = plt.subplot()
ax1.plot(x, y_voltage_handled, color='orange', label='voltage')

ax1.set_ylabel('voltage', color='orange')
plt.legend()
plt.show()
'''

# %%
# 算功率
i = 0
total_power_within_duration = 0.0
while i < RecordLength:
    total_power_within_duration += SampleInterval * \
        value_data_current[i] * value_data_voltage[i]
    i += 1

print(total_power_within_duration)

# %%
print(total_power_within_duration * 25)

# %%
# 数据切片

# left_horizon_plot = 120000
# right_horizon_plot = left_horizon_plot + 799999
data_for_plot_voltage = value_data_voltage[left_horizon_plot:right_horizon_plot]
# time_for_plot = time_data[left_horizon_plot:right_horizon_plot]


# %%
plt.figure()
ax1 = plt.subplot()
# ax2 = ax1.twinx()
ax1.plot(time_for_plot, data_for_plot_voltage, linewidth=0.1, color='orange', label='voltage')
# ax2.plot(x, y_current_handled, label='current')

ax1.set_ylabel('current')
# ax2.set_ylabel('current', color='b')
plt.legend()
plt.show()

# %%
line_width = 0.2
plt.figure(dpi=300, figsize=(7,6))
# plt.figure()
plt.rc('font',family='Times New Roman', size=15)
ax1 = plt.subplot()
# ax1.spines['left'].set_color('blue')
l1, = ax1.plot(time_for_plot, data_for_plot_voltage, 
               linewidth=line_width, label='Voltage', color='blue')
ax1.set_ylabel('Voltage (kV)', size=20, color='blue')
# ax1.spines['top'].set_visible(False) #去掉上边框
# ax1.spines['bottom'].set_visible(False) #去掉下边框
ax1.tick_params(axis='y', colors='blue')
ax1.set_xlabel('Time (ms)', size=20)

ax2 = ax1.twinx()
l2, = ax2.plot(time_for_plot, data_for_plot_current,
                linewidth=line_width, label='Current', color='red')
ax2.set_ylabel('Current (mA)', size=20, color='red')

ax2.spines['left'].set_color('blue')
ax2.spines['right'].set_color('red')
ax2.tick_params(colors='red')
plt.legend(handles=[l1, l2])
plt.show()
# %%
