# %% IMPORT STATEMENTS
import numpy as np
import matplotlib.pyplot as plt

# %% FUNCTION DEFINITIONS


def lift_against_halbach_thickness(halbach_thickness, halbach_wavenumber):
    """Lift Force Functional dependence again halbach thickness"""
    k = halbach_wavenumber
    x = halbach_thickness
    return (1-np.exp(-k*x))**2


def mass_against_halbach_thickness(halbach_thickness, mass_per_unit_length, other_mass):
    """mass of system against halbach thickness"""
    return halbach_thickness * mass_per_unit_length + other_mass


def create_plot(function_input, x_min, x_max, resolution, *extra_inputs, y_min=None, y_max=None,
                graph_title='title', x_title='x', y_title='y', colour_input='navy'):
    """
    Will plot a range of x values into a function. If the function requires
    more than just the x value input, it will try putting in extra inputs one by one.
    If none works, code will exit.

    Returns
    -------
    0

    """

    fig = plt.figure()

    axes = fig.add_subplot(111)

    axes.set_title(graph_title)
    axes.set_xlabel(x_title)
    axes.set_ylabel(y_title)

    if y_min is not None:
        axes.set_ylim(bottom=y_min)
    if y_max is not None:
        axes.set_ylim(top=y_max)

    x_values = np.linspace(x_min, x_max, resolution)

    # Try to plot with each extra input until successful
    for i in range(len(extra_inputs) + 1):
        try:
            axes.plot(x_values, function_input(
                x_values, *extra_inputs[:i]), color=colour_input, label='Trend Prediction')
            break
        except Exception:
            continue
    else:
        return 1

    plt.savefig(graph_title + '.png', dpi=777)
    return 0


def array_plot(x_values, y_values, y_min=None, y_max=None, graph_title='title', x_title='x',
               y_title='y', colour_input='navy'):
    """
    Will plot a range of x values and y values.

    Returns
    -------
    0
    """

    fig = plt.figure()

    axes = fig.add_subplot(111)

    axes.set_title(graph_title)
    axes.set_xlabel(x_title)
    axes.set_ylabel(y_title)

    if y_min is not None:
        axes.set_ylim(bottom=y_min)
    if y_max is not None:
        axes.set_ylim(top=y_max)

    try:
        axes.plot(x_values, y_values, color=colour_input, label='Trend Prediction')
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

    plt.savefig(graph_title + '.png', dpi=777)
    return 0


# %% MAIN


def main():
    # setup parameters / geometries
    x_min, x_max = 0, 0.1
    halbach_wavelength = 2*np.pi / 0.04
    mass_per_unit_length = 80
    const_mass = 150
    lift_constant = 1

    # create thickness set
    resolution = 100
    thicknesses = np.linspace(x_min, x_max, resolution)

    # generate results
    lift_effects = lift_against_halbach_thickness(thicknesses, halbach_wavelength)
    masses = mass_against_halbach_thickness(thicknesses, halbach_wavelength)
    lift_density = (lift_constant) * lift_effects / masses

    # plot results
    create_plot(lift_against_halbach_thickness, x_min, x_max, resolution, halbach_wavelength,
                graph_title='Lift against Thickness', x_title='Thickness', y_title='Lift Effect',
                colour_input='Green')
    create_plot(mass_against_halbach_thickness, x_min, x_max, resolution, mass_per_unit_length, const_mass,
                y_min=100, y_max=200,
                graph_title='Mass against Thickness', x_title='Thickness', y_title='Mass',
                colour_input='Red')
    return 0


# %% MAIN EXECUTION
if __name__ == "__main__":
    main()
