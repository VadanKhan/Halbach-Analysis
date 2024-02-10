# Halbach-Analysis

Projects to analyse how parameters affect the "lift effect" of Halbach arrays in Magnetic Levitation contexts.

These codes were written in the context of the Hyperloop Manchester project. Here we are investigating what effects changing the dimensions of our Halbach array will have on our pod.

- https://hyperloop-manchester.com/
- https://www.linkedin.com/company/hyperloop-manchester/mycompany/

## Halbach Array Analysis

This repository contains Python scripts for analyzing the effects of various parameters of Halbach arrays on their properties. The scripts calculate the lift force and drag force for a given set of parameters.

### Dependencies

The scripts depend on the following Python libraries:

- numpy
- matplotlib.pyplot
- scipy.constants

You can install these dependencies using pip:

```bash
pip install numpy matplotlib scipy
```

Or if you are using Poetry for managing virtual environments, you can add these dependencies to your `pyproject.toml` file and install them using Poetry:

```bash
poetry add numpy matplotlib scipy
```

### Scripts

#### Halbach_Analysis (`Halbach_Analysis.py`)

This script is a general large script that can plot the behaviour of the lift and drag of the system against certain parameters.

#### Optimum Lift Density Analysis (`optimum_lift_density.py`)

The `optimum_lift_density.py` script is designed to analyze and visualize the relationship between the thickness of a Halbach array and its lift effect, mass, and lift density.

#### Plotting Functions (`plotting_functions.py`)

The `plotting_functions.py` module provides two functions for creating plots: `create_plot` and `array_plot`. The `create_plot` function takes a function and a range of x values as input, and plots the function over that range. The `array_plot` function plots a range of x values and y values. It has optional parameters for setting the y-axis limits, the graph title, the x and y axis labels, and the color of the plot. It can also plot and label the maximum of the curve if desired.

## Citations

Chaidez, Eric, Shankar P. Bhattacharyya, and Adonios N. Karpetis. “Levitation Methods for Use in the Hyperloop High-Speed Transportation System.” Energies 12, no. 21: 4190

Hu, Yongpan, Zhiqiang Long, Jiewei Zeng, and Zhiqiang Wang. “Analytical Optimization of Electrodynamic Suspension for Ultrahigh-Speed Ground Transportation.” IEEE Transactions on Magnetics, vol. 57, no. 8, August 2021, 8000511
