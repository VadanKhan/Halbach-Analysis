% ________________TITLE________________
% Hyperloop: Magnetic Levitation Sub-team: Lift Force Against Width
% -------------------------------------
% This script is designed to quantatively inform how the lift force (provided
% from a halbach array in a passive levitaion) varies with the lateral width
% of the halbach array magnets.

% The Lift force (averaged over a full period of magnetic flux) is described
% by:

% F_x = [B_0^2*w_c^2*exp(-2k(dz))]/[2*k*L_c(1 + R_c^2/(w^2*L_c^2))]

% as described, with constant notation from: 
% "MODELING AND PERFORMANCE EVALUATION OF ELECTROMAGNETIC
% SUSPENSION SYSTEMS FOR THE HYPERLOOP" by ERIC CHAIDEZ

% In the above equation, the only constant dependant on lateral width (d)
% is B_0, the Peak Magnetic Field. This is described by (for an array with
% only square permanent magnets):

% B_0 = B_r * sinc(pi/M) * [1-exp(k * d)]
% where: 
% - B_r is the natural remnant magnetic field of the permanent magnet
%   material
% - M describes the number of permanent magnets in the Halbach array
% - k is the "wavenumber of magnets"
%     k = 2*pi / lambda
%     lambda is the length of the array
% - d is the width of the array

% This script will provide 3 functions:
% 1) plot some typical B_0^2 curves for our maglev system (as our lift 
%    force is proportional to B_0^2)
% 2) will determine a prefactor B_a
%    B_a = B_r * sinc(pi/M)
%    depedant on input parameters B_r and M. It will then plot the graph
%    of B_0 for input parameter lambda (over the typical d range)
% 3) Will calculate B_0 for given parameters B_r, M, lambda, d

% to not use 2) or 3), just input 0 each time. To use them input 1.

% Last Updated: 12/10/2022
% @author: Vadan Khan UID: 10823198

TYPICAL_B_r = 1.41;
TYPICAL_M = 10;
TYPICAL_lambdas = [0.1, 0.2, 0.3, 0.4, 0.5];

typical_ds = linspace(0, 0.5);
typical_B_0 = B_0calc(TYPICAL_B_r, TYPICAL_M, TYPICAL_lambdas(1), typical_ds);
typical_B_0sqrd = typical_B_0.^2;
xlabel("d (width) in m")
ylabel("B_0^2")
title("Typical B_0 Curves")
plot(typical_ds, typical_B_0sqrd)

hold on

typical_B_02 = B_0calc(TYPICAL_B_r, TYPICAL_M, TYPICAL_lambdas(2), typical_ds);
typical_B_0sqrd2 = typical_B_02.^2;
typical_B_03 = B_0calc(TYPICAL_B_r, TYPICAL_M, TYPICAL_lambdas(3), typical_ds);
typical_B_0sqrd3 = typical_B_03.^2;
typical_B_04 = B_0calc(TYPICAL_B_r, TYPICAL_M, TYPICAL_lambdas(4), typical_ds);
typical_B_0sqrd4 = typical_B_04.^2;
typical_B_05 = B_0calc(TYPICAL_B_r, TYPICAL_M, TYPICAL_lambdas(5), typical_ds);
typical_B_0sqrd5 = typical_B_05.^2;
plot(typical_ds, typical_B_0sqrd2)
plot(typical_ds, typical_B_0sqrd3)
plot(typical_ds, typical_B_0sqrd4)
plot(typical_ds, typical_B_0sqrd5)
legend("0.1m array", "0.2m array","0.3m array","0.4m array","0.5m array")

hold off

GraphPrefactor_logic = input("Please input a ""1"" if you would like the " + ...
    "graph of a specific B_a prefactor: ");
if GraphPrefactor_logic == 1
    B_r2 = input("input the remnant magnetic field:  ");
    M2 = input("input the number of magnets:  ");
    B_a2 = B_acalc(B_r2, M2);
    fprintf("The B_a Prefactor is: %g", B_a2);
    lambda2 = input("\ninput the array length:  ");
    B_02 = B_0ecalc(B_a2, lambda2, typical_ds);
    B_02sqrd = B_02.^2;
    xlabel("d (width) in m");
    ylabel("B_0^2");
    title("Specific B_0 Curve");
    plot(typical_ds, B_02sqrd);
end

SpecificB_0_logic = input("Please input a ""1"" if you would like a specific" + ...
    " value of B_0 for given parameters and width: ");
if SpecificB_0_logic == 1
    B_r3 = input("input the remnant magnetic field: ");
    M3 = input("input the number of magnets: ");
    lambda3 = input("input the array length: ");
    d3 = input("input the width of the array: ");
    B_03 = B_0calc(B_r3, M3, lambda3, d3);
    fprintf("The B_0 Value is: %g\n", B_03);
end

%Function definitions
function k = kcalc(lambda_input)
    k = 2*pi / lambda_input;
end

function sinc = sinc(x_input)
    sinc = sin(x_input) / x_input;
end

function B_a = B_acalc(B_r_input, M_input)
    B_a = B_r_input * sinc(pi/M_input);
end

function B_0 = B_0calc(B_r_input, M_input, lambda_input, d_input)
    k = kcalc(lambda_input);
    B_a = B_acalc(B_r_input, M_input);
    B_0 = B_a * (1-exp(-k*d_input));
end

function B_0e = B_0ecalc(B_a_input, lambda_input, d_input)
    k = kcalc(lambda_input);
    B_0e = B_a_input * (1-exp(-k*d_input));
end
