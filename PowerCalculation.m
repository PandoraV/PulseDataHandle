clc;
clear;

I_origin = csvread('data/F0002CH2.CSV', 0, 4, [0, 4, 2499, 4]);
U_origin = csvread('data/F0002CH1.CSV', 0, 4, [0, 4, 2499, 4]);

t = linspace(0,2500,2500);


%*************利用rlowess方法对加噪信号进行平滑处理，绘制平滑波形图************
I = smooth(I_origin,30,'rlowess');  		% 利用rlowess方法对y进行平滑处理

% figure;  							        % 新建一个图形窗口
% plot(t,I_origin,'k:');  			        % 绘制加噪波形图
% hold on;      
% plot(t,I,'k','linewidth',3);  	        % 绘制平滑后波形图
% xlabel('t');  					        % 为X轴加标签
% ylabel('rlowess');  				        % 为Y轴加标签
% legend('加噪波形','平滑后波形');

