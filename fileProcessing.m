clc;
clear;

directory_name = "ALL00";
file_name = "F00";
a = 0;
t = linspace(0,2500,2500);

for i = 1:1
    
    % 构建目录地址
    
    if a < 10
        directory_name = directory_name + '0';
        directory_name = directory_name + a;
        file_name = file_name + '0';
        file_name = file_name + a;
    elseif a < 100
        directory_name = directory_name + a;
        file_name = file_name + a;
    end
    
    % 开始访问底下的目录
    temp_path = "data/" + directory_name + '/' + file_name + "CH1.CSV";
    temp_origin_voltage = csvread("data/" + directory_name + '/' + file_name + "CH1.CSV", 0, 4, [0, 4, 2499, 4]);
    temp_origin_current = csvread("data/" + directory_name + '/' + file_name + "CH2.CSV", 0, 4, [0, 4, 2499, 4]);
    
    % 对数据进行滤波
    smooth_voltage = smooth(temp_origin_voltage, 30, 'rlowess'); % 窗宽需测试
    

    % 清空存储的路径信息

    directory_name = "ALL00";
    file_name = "F00";
    a = a + 1;
end

% dir("data/"+str)
