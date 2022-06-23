clc;

y = csvread('data/F0000CH2.CSV', 0, 4, [0, 4, 2499, 4]);

t = linspace(0,2500,2500);

% m1 = smooth(m);

%*************利用lowess方法对加噪信号进行平滑处理，绘制平滑波形图*************
yy2 = smooth(y,30,'lowess');  		% 利用lowess方法对y进行平滑处理
figure;  							% 新建一个图形窗口
plot(t,y,'k:');  					% 绘制加噪波形图
hold on;
plot(t,yy2,'k','linewidth',3);  	% 绘制平滑后波形图
xlabel('t');  						% 为X轴加标签
ylabel('lowess');  					% 为Y轴加标签
legend('加噪波形','平滑后波形');


%*************利用rlowess方法对加噪信号进行平滑处理，绘制平滑波形图************
yy3 = smooth(y,30,'rlowess');  		% 利用rlowess方法对y进行平滑处理
figure;  							% 新建一个图形窗口
plot(t,y,'k:');  					% 绘制加噪波形图
hold on;
plot(t,yy3,'k','linewidth',3);  	% 绘制平滑后波形图
xlabel('t');  						% 为X轴加标签
ylabel('rlowess');  				% 为Y轴加标签
legend('加噪波形','平滑后波形');


%*************利用loess方法对加噪信号进行平滑处理，绘制平滑波形图*************
yy4 = smooth(y,30,'loess');  		% 利用loess方法对y进行平滑处理
figure;  							% 新建一个图形窗口
plot(t,y,'k:');  					% 绘制加噪波形图
hold on;
plot(t,yy4,'k','linewidth',3);  	% 绘制平滑后波形图
xlabel('t');  						% 为X轴加标签
ylabel('loess');  					% 为Y轴加标签
legend('加噪波形','平滑后波形');


%*************利用sgolay方法对加噪信号进行平滑处理，绘制平滑波形图*************
yy5 = smooth(y,30,'sgolay',3);  	% 利用sgolay方法对y进行平滑处理
figure;  							% 新建一个图形窗口
plot(t,y,'k:');  					% 绘制加噪波形图
hold on;
plot(t,yy5,'k','linewidth',3);  	% 绘制平滑后波形图
xlabel('t');  						% 为X轴加标签
ylabel('sgolay');  					% 为Y轴加标签
legend('加噪波形','平滑后波形');
