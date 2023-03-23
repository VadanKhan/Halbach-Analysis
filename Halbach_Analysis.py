# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:45:47 2022

@author: vadan
"""
# %% IMPORT STATEMENTS
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

# %% DECLARING CONSTANTS
MU0 = const.mu_0

# %% FUNCTION DEFINITIONS


def lift_against_height(halbach_height, wavenumber):
    k = wavenumber
    d = halbach_height
    return (1-np.exp(-k*d))**2


def lift_against_width(halbach_width):
    return halbach_width


def lift_against_length(halbach_length):
    return halbach_length


def lift_against_displacement_away(displacement_away, wavenumber):
    k = wavenumber
    y = displacement_away
    return np.exp(-2*k*y)


def lift_against_height_conductor_thickness(thickness, decay_constant):
    '''
    value of decay constant is given as a complex expressoin (Hu Paper 19)


    Parameters
    ----------
    thickness : float
    decay_constant : float

    Returns
    -------
    Float

    '''
    a = decay_constant
    h = thickness
    return 1-np.exp(-2*a*h)


def lift_against_magnet_resolution(magnet_resolution):

    ans = (np.sinc(np.pi/magnet_resolution))**2
    return ans


def lift_velocity_probe(velocity, other_constant):
    lift_factor = velocity**2 / (velocity**2 + other_constant)
    return lift_factor


def drag_velocity_probe(velocity, other_constant):
    '''
    Other constant up to research:
    According to Chaidez Paper (equation 4.16), other constant = R_c / (k*L_c)
    '''

    lift_factor = (other_constant*velocity) / \
        (velocity**2 + (other_constant)**2)
    return lift_factor


def create_plot(graph_title, x_title, y_title, x_min, x_max, function_input,
                resolution, extra_input1, extra_input2, colour_input):
    """
    Will plot a range of x values into a function. If the function requires
    more than just the x value input, it will try putting in extra_input1
    afterwards, and if not extra_input2 second. If neither works code will
    exit.

    Returns
    -------
    0

    """

    fig = plt.figure()

    axes = fig.add_subplot(111)

    axes.set_title(graph_title)
    axes.set_xlabel(x_title)
    axes.set_ylabel(y_title)

    x_values = np.linspace(x_min, x_max, resolution)

    # define random color
    col = (np.random.random(), np.random.random(), np.random.random())

    try:
        axes.plot(x_values, function_input(x_values), color=colour_input,
                  label='Trend Prediction')
    except Exception:
        axes.plot(x_values, function_input(x_values, extra_input1),
                  color=colour_input, label='Trend Prediction')
    except Exception:
        axes.plot(x_values, function_input(x_values, extra_input1,
                  extra_input2), color=colour_input, label='Trend Prediction')
    except Exception:
        return 1
    plt.savefig(graph_title + '.png', dpi=777)
    plt.show()
    return 0


def double_plot(graph_title, x_title, y_title, x_min, x_max, function_input1,
                name1, function_input2, name2, resolution, extra_input1,
                extra_input2, colour_input1, colour_input2):
    """
    plot 2 data sets
    -------
    0

    """
    x_values = np.linspace(x_min, x_max, resolution)

    fig = plt.figure()

    ax = fig.add_subplot(111)

    ax.set_title(graph_title)
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    try:
        ax.plot(x_values, function_input1(x_values),
                color=colour_input1, label=name1)
        ax.plot(x_values, function_input2(x_values), color=colour_input2,
                label=name2)
    except Exception:
        ax.plot(x_values, function_input1(x_values, extra_input1),
                color=colour_input1, label=name1)
        ax.plot(x_values, function_input2(x_values, extra_input1),
                color=colour_input2, label=name2)
    except Exception:
        ax.plot(x_values, function_input1(x_values, extra_input1, extra_input2),
                color=colour_input1, label=name1)
        ax.plot(x_values, function_input2(
            x_values, extra_input1, extra_input2),
            color=colour_input2, label=name2)
    except Exception:
        return 1
    plt.legend(loc='upper left', borderaxespad=0.5, fontsize='7')
    plt.tight_layout()
    plt.savefig(graph_title + '.png', dpi=1000)
    plt.show()

    return 0


def Hu_maxforceplot(v, l, d, s, lam, M, y, h, mu, sig, Br):
    '''
    lam = wavelength (length) of 1 periodic unit of halbach array
    k = 2pi / lam
    s = width of halbach
    l = length of halbach
    d = height of halbach
    y = distance from conductor plate to bottom of halbach
    M = number of magnets per wavelength
    h = height of conductor
    mu = Permeability
    sig = Conductivity
    Br = Remnant Magnetisation
    '''
    print('seperation of halbach array (m):', y)
    # cond = 1-np.exp(-2*a*h)
    k = 2*np.pi / lam
    print("Halbach Wavenumber: ", k)

    consts = mu * sig**2 * s * l * Br**2 / k**2
    print("Other Constants Effect: ", consts)
    magres = (np.sinc(np.pi/M))**2
    print("Magnetic Resolution Effect: ", magres)
    halheight = (1-np.exp(-k*d))**2
    print("Halbach Height Effect ", halheight)
    dist = np.exp(-2*k*y)
    print("Distance Effect: ", dist, "\n")
    velnum = v**2
    velden1 = (np.sqrt(1+(mu**2 * sig**2 * v**2)/(k**2))+1)**(3/2)
    velden2 = np.sqrt(np.sqrt(1+(mu**2 * sig**2 * v**2)/(k**2)) + 1)+np.sqrt(2)

    const_1 = s * l * Br / mu

    return v/v * const_1 * magres * halheight * dist


def Hu_liftforce(v, l, d, s, lam, M, y, h, mu, sig, Br):
    '''
    lam = wavelength (length) of 1 periodic unit of halbach array
    k = 2pi / lam
    s = width of halbach
    l = length of halbach
    d = height of halbach
    y = distance from conductor plate to bottom of halbach
    M = number of magnets per wavelength
    h = height of conductor
    mu = Permeability
    sig = Conductivity
    Br = Remnant Magnetisation
    '''
    print('seperation of halbach array (m):', y)
    # cond = 1-np.exp(-2*a*h)
    k = 2*np.pi / lam
    print("Halbach Wavenumber: ", k)

    consts = mu * sig**2 * s * l * Br**2 / k**2
    print("Other Constants Effect: ", consts)
    magres = (np.sinc(np.pi/M))**2
    print("Magnetic Resolution Effect: ", magres)
    halheight = (1-np.exp(-k*d))**2
    print("Halbach Height Effect ", halheight)
    dist = np.exp(-2*k*y)
    print("Distance Effect: ", dist, "\n")
    velnum = v**2
    velden1 = (np.sqrt(1+(mu**2 * sig**2 * v**2)/(k**2))+1)**(3/2)
    velden2 = np.sqrt(np.sqrt(1+(mu**2 * sig**2 * v**2)/(k**2)) + 1)+np.sqrt(2)

    const_1 = s * l * Br / mu

    return consts * magres * halheight * (velnum / (velden1*velden2)) * dist

def Hu_dragforce(v, l, d, s, lam, M, y, h, mu, sig, Br):
    '''
    lam = wavelength (length) of 1 periodic unit of halbach array
    k = 2pi / lam
    s = width of halbach
    l = length of halbach
    d = height of halbach
    y = distance from conductor plate to bottom of halbach
    M = number of magnets per wavelength
    h = height of conductor
    mu = Permeability
    sig = Conductivity
    Br = Remnant Magnetisation
    '''
    print('seperation of halbach array (m):', y)
    # cond = 1-np.exp(-2*a*h)
    k = 2*np.pi / lam
    print("Halbach Wavenumber: ", k)

    consts = np.sqrt(2) * sig * s * l * Br**2 / k
    print("Other Constants Effect: ", consts)
    magres = (np.sinc(np.pi/M))**2
    print("Magnetic Resolution Effect: ", magres)
    halheight = (1-np.exp(-k*d))**2
    print("Halbach Height Effect ", halheight)
    dist = np.exp(-2*k*y)
    print("Distance Effect: ", dist, "\n")
    velnum = v
    velden1 = (np.sqrt(1+(mu**2 * sig**2 * v**2)/(k**2))+1)
    velden2 = np.sqrt(np.sqrt(1+(mu**2 * sig**2 * v**2)/(k**2)) + 1)+np.sqrt(2)

    const_1 = s * l * Br / mu

    return consts * magres * halheight * (velnum / (velden1*velden2)) * dist


def create_plotm(graph_title, x_title, y_title, x_min, x_max, function_input,
                 resolution, extra_input1, extra_input2, ei3, ei4, ei5, ei6,
                 ei7, ei8, ei9, ei10, colour_input):
    """
    Will plot a range of x values into a function. If the function requires
    more than just the x value input, it will try putting in extra_input1
    afterwards, and if not extra_input2 second, etc for further ei{} constants.
    Otherwise code will exit.
    Returns
    -------
    0

    """

    fig = plt.figure()

    axes = fig.add_subplot(111)

    axes.set_title(graph_title)
    axes.set_xlabel(x_title)
    axes.set_ylabel(y_title)

    x_values = np.linspace(x_min, x_max, resolution)

    try:
        axes.plot(x_values, function_input(x_values, extra_input1,
                  extra_input2, ei3, ei4, ei5, ei6,
                  ei7, ei8, ei9, ei10), color=colour_input)
    except Exception:
        return 1
    plt.savefig(graph_title + '.png', dpi=777)
    plt.show()
    return 0


def create_plotmm(graph_title, x_title, y_title, x_min, x_max, function_input,
                  resolution, extra_input1, extra_input2, ei3, ei4, ei5, ei6,
                  ei7, ei8, ei9, ei10, colour_input, function_input2):
    """
    Will plot a range of x values into a function. If the function requires
    more than just the x value input, it will try putting in extra_input1
    afterwards, and if not extra_input2 second, etc for further ei{} constants.
    Otherwise code will exit.

    Will then plot a second function.

    Returns
    -------
    0

    """

    graph_title_consts = 'l={0:1.3g}, d={1:1.3g}, s={2:1.3g}, $\lambda$={3:1.3g},' \
        ' M={4:1.3g}, y={5:1.3g}, $\mu_r$={7:1.3g}, $\sigma$={8:1.3g},' \
        ' $B_r$={9:1.3g}'.format(
            extra_input1, extra_input2, ei3, ei4, ei5, ei6, ei7, ei8/MU0, ei9, ei10)

    fig, (axes, ax2) = plt.subplots(2)
    fig.suptitle(graph_title_consts, fontsize=10)

    axes.set_xlabel(x_title)
    axes.set_ylabel(y_title)

    x_values = np.linspace(x_min, x_max, resolution)

    try:
        axes.plot(x_values, function_input2(x_values, extra_input1,
                  extra_input2, ei3, ei4, ei5, ei6,
                  ei7, ei8, ei9, ei10), color='red', alpha=0.7,
                  linestyle='--', label='Max Lift Force')
        axes.legend(fontsize=8)
    except Exception:
        return 1

    try:
        axes.plot(x_values, function_input(x_values, extra_input1,
                  extra_input2, ei3, ei4, ei5, ei6,
                  ei7, ei8, ei9, ei10), color=colour_input)
    except Exception:
        return 1

    ax2.set_xlabel(x_title)
    ax2.set_ylabel(y_title)

    x_values = np.linspace(x_min, x_max, resolution)

    try:
        ax2.plot(x_values, function_input(x_values, extra_input1,
                                          extra_input2, ei3, ei4, ei5, ei6,
                                          ei7, ei8, ei9, ei10),
                 color=colour_input)
    except Exception:
        return 1
    plt.tight_layout()
    plt.savefig(graph_title + '.png', dpi=777)
    plt.subplots_adjust(bottom=0.1,
                        top=0.9,
                        hspace=0.4)
    plt.show()
    return 0


# %% MAIN


def main():
    """
    Main function. Will run all main_code, and if a 1 is returned, it will
    notify of a reading file error.
    """
    return_code = main_code()
    if return_code == 1:
        print("Error Graphing")
        sys.exit()
        return 1
    return 0


def main_code():
    """
    Contains all executed code. Should return 1 in the instance of a reading
    error.

    """
    # %% plot all functions
    # double_plot('Lift to Drag against Velocity', 'Velocity (ms^-1)',
    #             'Lift to Drag effect', 0, 20, lift_velocity_probe,
    #             'Lift Effect', drag_velocity_probe, 'Drag Effect', 250, 1,
    #             False, 'navy', 'red')
    # create_plot('Lift against Halbach array Height (array length = 50mm)',
    #             'Height (m)', 'Lift Effect', 0, 0.1, lift_against_height, 777,
    #             (2*np.pi/0.05), False, 'navy')
    # create_plot('Lift against Halbach array Width', 'Width (m)', 'Lift Effect',
    #             0, 0.5, lift_against_width, 777, False, False, 'navy')
    # create_plot('Lift against Halbach array Length', 'Length (m)',
    #             'Lift Effect', 0, 0.5, lift_against_length, 777, False, False,
    #             'navy')
    # create_plot('Lift against Halbach Displacement Away (array length = 50mm)',
    #             'Displacement Away (m)', 'Lift Effect', 0, 0.05,
    #             lift_against_displacement_away, 777, (2*np.pi/0.05), False,
    #             'red')
    # create_plot('Lift against Conductor Plate Thickness'
    #             '(decay constant = 10)', 'Plate Thickness (m)',
    #             'Lift Effect', 0, 0.5, lift_against_height_conductor_thickness,
    #             777, 10, False, 'blue')
    create_plot('Lift against No. Magnets per Wavelength',
                'No magnets', 'Lift Effect', 1, 20,
                lift_against_magnet_resolution, 100, False, False, 'orange')

    '''
    create_plotmm(graph_title, x_title, y_title, x_min, x_max, function_input,
                     resolution, extra_input1, extra_input2, ei3, ei4, ei5, ei6,
                     ei7, ei8, ei9, ei10, colour_input, function_input2):
    '''
    '''
    Hu_liftforce or Humaxforceplot(v, l, d, s, lam, M, y, h, mu, sig, Br)
    lam = wavelength (length) of 1 periodic unit of halbach array
    k = 2pi / lam
    s = width of halbach
    l = length of halbach
    d = height of halbach
    y = distance from conductor plate to bottom of halbach
    M = number of magnets per wavelength
    h = height of conductor
    mu = Permeability
    sig = Conductivity
    Br = Remnant Magnetisation
    '''
    create_plotmm('Lift Force against Velocity',
                  'velocity', 'Lift Force', 0, 20, Hu_liftforce, 777, 1, 0.1,
                  0.3, 0.4, 8, 0.01, 0.05, MU0*1.05, 2.2E6, 1.3, 'navy',
                  Hu_maxforceplot)
    create_plotmm('Drag Force against Velocity',
                  'velocity', 'Drag Force', 0, 20, Hu_dragforce, 777, 1, 0.1,
                  0.3, 0.4, 4, 0.01, 0.05, MU0*1.05, 2.2E6, 1.3, 'navy',
                  Hu_maxforceplot)
    return 0


# %% MAIN EXECUTION
if __name__ == "__main__":
    main()
