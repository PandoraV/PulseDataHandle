clc;
clear;

directory_name = "ALL00";
file_name = "F00";
a = 0;
t = linspace(0,2500,2500);

origin_power = 0.0;
handle_power = 0.0;
sample_interval = 2e-5;

for j = 1:17
    
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
    temp_handle_voltage = smooth(temp_origin_voltage, 30, 'rlowess'); 

    % 寻找过零点，第一次出现0即可
    flag = 1;
    while (flag <= 200) 
        % 最多执行200次，找半个周期
        if temp_origin_voltage(flag, 1) == 0
            break
        end
        flag = flag + 1;
    end

    % 从零点后计算原始功率和处理后功率
    origin_power = 0.0;
    handle_power = 0.0;
    flag = flag - 1;
    for i = 1:2000
        temp_origin_power = temp_origin_voltage(flag + i, 1) * temp_origin_current(flag + i, 1);
        origin_power = origin_power + temp_origin_power;
        temp_handle_power = temp_handle_voltage(flag + i, 1) * temp_origin_current(flag + i, 1);
        handle_power = handle_power + temp_handle_power;
    end
    origin_power = origin_power * 25 * sample_interval; % 因为算了两个周期
    handle_power = handle_power * 25 * sample_interval;
    origin_power = origin_power * 4501 / 100; % 缩放比例
    handle_power = handle_power * 4501 / 100;
    
    % 打印功率
    fprintf("%s origin is %f, handled is %f\n", directory_name, origin_power, handle_power);

    % 清空存储的路径信息

    directory_name = "ALL00";
    file_name = "F00";
    a = a + 1;
end

% dir("data/"+str)
