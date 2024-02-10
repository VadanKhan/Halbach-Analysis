
function [Flift,Flift2,Fdrag,Fdrag2] = forces_a(v,s,d,lambda,M,Br,h,y1,n)
k = 2*pi/lambda;
l = lambda*n; %length
mu = 4*pi * 10e-7; %permeability of air (H/m)
sigma = 3.5*10e7; %conductivity (W/m K)
omega = k*v;
a = sqrt(k^2 + sqrt(k^4 + mu^2*sigma^2*omega^2)/2);

% Flift = s*l*(Br^2)*(M^2)*(sin(pi/M)^2)*((1-exp(-k*d))^2)*(1-exp(-2*a*h))*exp(-2*k*y1) / (mu*pi^2);
v1 = mu*sigma^2*s*l*(Br^2)*(M^2)*(sin(pi/M)^2)*((1-exp(-k*d))^2)*(1-exp(-2*a*h))*exp(-2*k*y1)/(pi^2*k^2);
v2 = sqrt(1+(mu^2*sigma^2*v^2/k^2))+1;
v3 = v^2/(v2^1.5*(v2^0.5+sqrt(2)));
% Flift = v1*v3;
v1 = (sqrt(2)*sigma*s*l*(Br^2)*(M^2)) * (sin(pi/M)^2) * ((1-exp(-k*d))^2) * (1-exp(-2*a*h)) * (1+exp(-2*a*h)) * exp(-2*k*y1)/((pi^2)*k);
v3 = v / (v2 * (v2^0.5 + sqrt(2)));
Fdrag = v1*v3;
Flift2 = s*l*(Br^2)*(M^2)*(sin(pi/M)^2)*((1-exp(-k*d))^2)*(1-exp(-2*a*h))*exp(-2*k*y1)/(pi^2*mu);
Fdrag2 = (sqrt(2)*s*l*(Br^2)*(M^2)*(k^0.5)) * (sin(pi/M)^2) * ((1-exp(-k*d))^2) * (1-exp(-2*a*h)) * (1+exp(-2*a*h)) * exp(-2*k*y1)/((pi^2)*mu^1.5*sigma^0.5 * v^0.5);

%Vcode
k = 2*pi / lambda;
% Consistent

a = sqrt(0.5*(k^2+sqrt(k^4 + mu^2 * sigma^2 * (v*k)^2)));
% ↑ deviates, gets ~ twice as large for later velocity

consts = (mu * sigma^2 * s * l * Br^2) / (k^2);
% ↑ deviates, *1000 bigger

magres = (sin(pi/M)/(pi/M))^2;
% ↑ deviates, *2 bigger

halheight = (1-exp(-k*d))^2;
% Consistent

dist = exp(-2*k*y1);
% Consistent

cond = 1-exp(-2*a*h);
% ↑ deviates, however this has little effect (↑=1, whereas python as 0.997)

velnum = v^2 * cond;
velden1 = (sqrt(1+(mu^2 * sigma^2 * v^2)/(k^2))+1)^(3/2);
velden2 = sqrt(sqrt(1+(mu^2 * sigma^2 * v^2)/(k^2)) + 1)+sqrt(2);

Flift = consts * magres * halheight * (velnum / (velden1*velden2)) * dist;

end
% 
% *exp(-2*k*y1))
