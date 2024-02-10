# %% IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt

from plotting_functions import create_plot
from plotting_functions import array_plot
# %% FUNCTION DEFINITIONS


def lift_against_halbach_thickness(halbach_thickness, halbach_wavenumber):
    """Lift Force Functional dependence again halbach thickness"""
    k = halbach_wavenumber
    x = halbach_thickness
    return (1-np.exp(-k*x))**2


def mass_against_halbach_thickness(halbach_thickness, mass_per_unit_length, other_mass):
    """mass of system against halbach thickness"""
    return halbach_thickness * mass_per_unit_length + other_mass

# %% MAIN


def main():
    # setup parameters / geometries
    x_min, x_max = 0, 0.1
    halbach_wavelength = 2*np.pi / 0.04
    mass_per_unit_length = 80
    const_mass = 120
    lift_constant = 1

    # create thickness set
    resolution = 100
    thicknesses = np.linspace(x_min, x_max, resolution)

    # generate results
    lift_effects = lift_against_halbach_thickness(thicknesses, halbach_wavelength)
    masses = mass_against_halbach_thickness(thicknesses, mass_per_unit_length, const_mass)
    lift_density = (lift_constant) * lift_effects / masses

    # plot results
    array_plot(thicknesses, lift_effects, y_min=None, y_max=None, graph_title='Lift against Thickness', x_title='Thickness',
               y_title='Lift Effect', colour_input='Green', show_maximum=True)
    array_plot(thicknesses, masses, y_min=100, y_max=150, graph_title='Mass against Thickness', x_title='Thickness',
               y_title='Mass', colour_input='Red')
    return 0


# %% MAIN EXECUTION
if __name__ == "__main__":
    main()
