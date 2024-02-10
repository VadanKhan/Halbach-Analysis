import numpy as np
import matplotlib.pyplot as plt


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
               y_title='y', colour_input='navy', show_maximum=False):
    """
    This function plots a range of x values and y values. It has optional features to set the y
        axis limits. Additionally can plot the maximum of the curve.

    Parameters:
    x_values (numpy.ndarray): The array of x values.
    y_values (numpy.ndarray): The array of y values.
    y_min (float, optional): The minimum limit for the y-axis. If not provided, the limit is set automatically.
    y_max (float, optional): The maximum limit for the y-axis. If not provided, the limit is set automatically.
    graph_title (str, optional): The title of the graph. Default is 'title'.
    x_title (str, optional): The label for the x-axis. Default is 'x'.
    y_title (str, optional): The label for the y-axis. Default is 'y'.
    colour_input (str, optional): The color of the plot. Default is 'navy'.
    show_maximum (bool, optional): If True, the maximum point is plotted and labeled. Default is False.

    Returns:
    int: 0 if the plot is successful, 1 otherwise.
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
        if show_maximum:
            max_y_index = np.argmax(y_values)
            max_y = y_values[max_y_index]
            max_x = x_values[max_y_index]
            axes.plot(max_x, max_y, 'ro', label=f'Maximum ({max_x}, {max_y})')
        plt.legend()
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

    plt.savefig(graph_title + '.png', dpi=777)
    return 0
