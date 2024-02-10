# Halbach-Analysis
Projects to analyse how parameters affect the "lift effect" of halbach arrays in Magnetic Levitation contexts.

These codes were written in the context of the Hyperloop Manchester project https://www.linkedin.com/company/hyperloop-manchester/mycompany/
Here we are investigating what effects changing the dimensions of our Halbach array will have on our pod.


# Halbach Array Analysis

This repository contains Python scripts for analyzing the effects of various parameters of Halbach arrays on their properties. The scripts calculate the lift force and drag force for a given set of parameters.

## Dependencies

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

## Scripts

The repository includes the following scripts:

- `Hu_liftforce.py`: This script calculates the lift force of a Halbach array given a set of parameters. The parameters include the wavelength of one periodic unit of the Halbach array, the width and length of the Halbach, the height of the Halbach, the distance from the conductor plate to the bottom of the Halbach, the number of magnets per wavelength, the height of the conductor, the permeability, the conductivity, and the remnant magnetization.

- `Hu_dragforce.py`: This script calculates the drag force of a Halbach array given a set of parameters. The parameters are the same as those for the lift force calculation.
