clc;
clear;

I_origin = csvread('data/ALL0001/OUTPUT.CSV', 0, 1, [0, 1, 2499, 1]);
U_origin = csvread('data/ALL0001/OUTPUT.CSV', 0, 0, [0, 0, 2499, 0]);

t = linspace(0,2500,2500);

U = smooth(U_origin,30,'rlowess');
I = smooth(I_origin,30,'rlowess');  		% 利用rlowess方法对y进行平滑处理

figure;  							        % 新建一个图形窗口

plot(t,I_origin,'k:');  			        % 绘制加噪波形图
hold on;      
plot(t,I,'k','linewidth',3);  	        % 绘制平滑后波形图
xlabel('t');  					        % 为X轴加标签
ylabel('rlowess');  				        % 为Y轴加标签
legend('加噪波形','平滑后波形');

power_origin = zeros(2500, 1);
power_handled = zeros(2500, 1);
total_power_origin = 0;
total_power_handled = 0;
for i = 1:2500
    power_origin(i, 1) = U_origin(i, 1) * I_origin(i, 1);
    power_handled(i, 1) = U(i, 1) * I(i, 1);
    total_power_origin = total_power_origin + power_origin(i, 1);
    total_power_handled = total_power_handled + power_handled(i, 1);
end

sample_interval = 2e-8;
total_power_handled = total_power_handled * sample_interval;
total_power_origin = total_power_origin * sample_interval;