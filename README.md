
# Bubble Potential Plotter

This repository provides a Python utility to visualize the incompressible potential function of a bubble in a liquid. The plotting function takes into account various parameters like surface tension, drive pressure, and polytropic index, allowing for customizable and detailed potential plots.

## Installation

Clone the repository and install the required dependencies.

```bash
git clone https://github.com/shimonuri/bubble-dynamics-utils.git
cd bubble-dynamics-utils
pip install -r requirements.txt
```

### Dependencies
- `matplotlib`
- `numpy`
- `pathlib`

## Usage

The primary function in this module is `plot_potential`, which generates a potential plot based on user-defined inputs.

### Example (in project dir)
```python
import plot_potential

surface_tension = 0.072  # N/m
drive_pressure = 0.5 * 101325  # Pa
ambient_and_vapor_pressure = 1 * 101325  # Pa
ambient_equilibrium_point = 1e-6 ** (5 / 2)  # m^(5/2)
polytropic_index = 5 / 3

plot_potential.plot_potential(
    surface_tension=surface_tension,
    drive_pressure=drive_pressure,
    ambient_and_vapor_pressure=ambient_and_vapor_pressure,
    ambient_equilibrium_point=ambient_equilibrium_point,
    polytropic_index=polytropic_index,
    start_r=5e-8,  # Starting radius in meters
    end_r=1e-5,  # Ending radius in meters
    r_ticks_in_q_scale=[1e-6, 5e-6, 10e-6],  # Tick values for the Q scale
)
```

### Parameters

- `surface_tension`: Surface tension of the liquid (in N/m).
- `drive_pressure`: Pressure driving the bubble (in Pa).
- `ambient_and_vapor_pressure`: Difference between ambient and vapor pressure (in Pa).
- `ambient_equilibrium_point`: Equilibrium radius of the bubble (in m^(5/2)).
- `polytropic_index`: The polytropic index of the gas inside the bubble.
- `start_r`: Starting radius for the plot (in meters).
- `end_r`: Ending radius for the plot (in meters).
- `output_path`: (Optional) If provided, the plot will be saved at the given file path.
- `r_ticks_in_q_scale`: (Optional) List of radius values in meters to be displayed as ticks in the plot's Q scale.
- `color`, `linestyle`, `label`, `legend_location`: (Optional) Customizations for the plot appearance.

### Output
The plot displays the potential function in terms of the Q-scale (related to the radius of the bubble). The plot's x-axis represents the Q scale, and the y-axis represents the potential energy in ergs.

You can save the plot as an image by specifying the `output_path`. Otherwise, the plot will be shown interactively.

## License

This project is licensed under the MIT License.

Feel free to contribute to this repository by submitting pull requests or reporting issues!
