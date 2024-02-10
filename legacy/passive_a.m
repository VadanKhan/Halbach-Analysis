clc;
clear;

accuracy = 1001;

v = linspace(0,50,accuracy); %velocity m/s
s = 50e-3; %width of magnet
d = 50e-3; %height of magnet
lambda = 200e-3;
M = 8; %magnets per wavelength
Br = 1.285; %remenant magnetic field 
h = 10e-3; %conductor thickness
y1 = 15e-3; %levitation heigth
n = 1; %number of wavelengths
wc = 100e-3; %width of conductor
r = 200e-3;

% l = lambda*n; %length
% k = 2 * pi / lambda; 
% omega = k*v;

%% system A
lift = zeros(accuracy,0);
drag = zeros(accuracy,0);
lift2 = zeros(accuracy,0);
drag2 = zeros(accuracy,0);

for i = 1:accuracy
    [lift(i),lift2(i),drag(i),drag2(i)] = forces_a(v(i),s,d,lambda,M,Br,h,y1,n);
end

figure
% subplot(2,2,1)
hold on
plot(v,lift,'Color','g','DisplayName','lift force','LineWidth',2.0);
plot(v,drag,'Color','r','DisplayName','drag force','LineWidth',2.0);
title('Hu et al., (2021): y1 = 15mm');
xlabel('velocity (m/s)')
ylabel('Force (N)')
legend;
legend('AutoUpdate','off')
% subplot(2,2,2)
% hold on
% plot(v,lift2,'Color','g','DisplayName','drag force','LineWidth',2.0);
% plot(v,drag2,'Color','r','DisplayName','drag force','LineWidth',2.0);
% title('paper 1 approx');

%% system B

Blift = zeros(accuracy,0);
Bdrag = zeros(accuracy,0);

for i = 1:accuracy
    [Blift(i),Bdrag(i)] = forces_b(v(i),s,d,lambda,M,Br,h,y1,n);
end

% subplot(2,2,3)
figure
hold on
plot(v,Blift,'Color','g','DisplayName','drag force','LineWidth',2.0);
plot(v,Bdrag,'Color','r','DisplayName','drag force','LineWidth',2.0);
title('Post and Ryutov (1996): y1 = 15mm');
xlabel('velocity (m/s)')
ylabel('Force (N)')
legend;
legend('AutoUpdate','off')
%% system C

Clift = zeros(accuracy,0);
Cdrag = zeros(accuracy,0);

for i = 1:accuracy
    [Clift(i),Cdrag(i)] = forces_c(v(i),s,d,lambda,M,Br,h,y1,n,wc);
end

% subplot(2,2,4)
figure
hold on
plot(v,Clift,'Color','g','DisplayName','drag force','LineWidth',2.0);
plot(v,Cdrag,'Color','r','DisplayName','drag force','LineWidth',2.0);
title('Chaidez (2018): y1 = 15mm');
xlabel('velocity (m/s)');
ylabel('Force (N)');
legend;
legend('AutoUpdate','off')
%% difference

% DiffL = 100*abs(lift - Blift)./lift;
% DiffD = 100*abs(drag - Bdrag)./drag;
% 
% subplot(2,2,4)
% hold on
% plot(v,DiffL,'Color','g','DisplayName','drag force','LineWidth',2.0);
% plot(v,DiffD,'Color','r','DisplayName','drag force','LineWidth',2.0);
% title('percentage diff');

%% 
% 
% 
% M=8
% 
% for i = 1:accuracy
%     [lift(i),lift2(i),drag(i),drag2(i)] = forces_a(v(i),s,d,lambda,M,Br,h,y1,n);
% end
% 
% subplot(2,2,1)
% hold on
% plot(v,lift,'-.','Color','g','DisplayName','drag force','LineWidth',2.0);
% plot(v,drag,'-.','Color','r','DisplayName','drag force','LineWidth',2.0);
% title('paper 1');
% subplot(2,2,2)
% hold on
% plot(v,lift2,'Color','g','DisplayName','drag force','LineWidth',2.0);
% plot(v,drag2,'Color','r','DisplayName','drag force','LineWidth',2.0);
% title('paper 1 approx');
