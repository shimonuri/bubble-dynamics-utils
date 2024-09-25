import pathlib
from matplotlib import pyplot as plt
import numpy as np

# set default font size
plt.rcParams.update({"font.size": 18})


def plot_potential(
    surface_tension,
    drive_pressure,
    ambient_and_vapor_pressure,  # p_0 - p_v
    ambient_equilibrium_point,
    polytropic_index,
    start_r,
    end_r,
    output_path=None,
    r_ticks_in_q_scale=None,
    color=None,
    linestyle=None,
    label=None,
    legend_location=None,
):
    """
    Plot the incompressible potential function for a bubble in a liquid.
    :param surface_tension: surface tension of the liquid
    :param drive_pressure:
    :param ambient_and_vapor_pressure: p_0 - p_v
    :param ambient_equilibrium_point: Q_{E0}
    :param polytropic_index: k
    :param start_r:
    :param end_r:
    :param output_path: figure output path, if None, the figure is only shown
    :param r_ticks_in_q_scale:e r ticks to plot in Q scale, for example [1e-6, 5e-6, 10e-6]
    :param color:
    :param linestyle:
    :param label:
    :param legend_location:
    :return: the potential as a function of Q
    """
    if polytropic_index > 1 / 3:
        pge = ambient_and_vapor_pressure + 2 * surface_tension / (
            ambient_equilibrium_point ** (2 / 5)
        )
    else:
        pge = 0

    potential = get_potential(
        surface_tension=surface_tension,
        pressure_inf=ambient_and_vapor_pressure + drive_pressure,
        pg0=pge,
        ambient_equilibrium_point=ambient_equilibrium_point,
        polytropic_index=polytropic_index,
    )
    q = np.linspace(start_r ** (5 / 2), end_r ** (5 / 2), 10000)
    plt.plot(
        q * (1e6 ** (5 / 2)) / 1000,
        to_ergs(potential(q)),
        color=color,
        linestyle=linestyle,
        label="incompressible potential" if label is None else label,
    )

    if r_ticks_in_q_scale is not None:
        xticks = [r ** (5 / 2) * (1e6 ** (5 / 2)) / 1000 for r in r_ticks_in_q_scale]
        xticks_labels = [
            str(int(r * 1e6) if (r * 1e6).is_integer() else r * 1e6)
            for r in r_ticks_in_q_scale
        ]

        plt.xticks(
            xticks,
            xticks_labels,
        )
        plt.xlabel(r"R[$\mu$m, Q scale]")
    else:
        plt.xlabel(r"Q[$\mu m^{5/2} \times 10^3$]")

    plt.ylabel("U(Q) [ergs]")
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))

    if label is not None:
        plt.legend(loc=legend_location)

    if output_path is not None:
        plt.savefig(
            pathlib.Path(output_path).as_posix(),
            dpi=300,
            bbox_inches="tight",
        )
        plt.clf()
    else:
        plt.show()

    return potential


def get_potential(
    surface_tension, pressure_inf, pg0, ambient_equilibrium_point, polytropic_index
):
    external_pressure_term = (
        lambda q: (4 * np.pi / 3) * (5 / 6) * (q ** (6 / 5)) * pressure_inf
    )

    internal_pressure_term = lambda q: (4 * np.pi / 3) * (
        5
        / (6 * (polytropic_index - 1))
        * pg0
        * (ambient_equilibrium_point / q) ** (6 * polytropic_index / 5)
        * q ** (6 / 5)
    )
    surface_tension_term = lambda q: (4 * np.pi / 3) * (
        5 / 2 * surface_tension * q ** (4 / 5)
    )

    return (
        lambda q: external_pressure_term(q)
        + internal_pressure_term(q)
        + surface_tension_term(q)
    )


def to_ergs(joules):
    return joules * 1e7


if __name__ == "__main__":
    surface_tension = 0.072  # N/m
    drive_pressure = 0.5 * 101325  # Pa
    ambient_and_vapor_pressure = 1 * 101325  # Pa
    ambient_equilibrium_point = 1e-6 ** (5 / 2)  # m^(5/2)
    polytropic_index = 5 / 3

    plot_potential(
        surface_tension=surface_tension,
        drive_pressure=drive_pressure,
        ambient_and_vapor_pressure=ambient_and_vapor_pressure,
        ambient_equilibrium_point=ambient_equilibrium_point,
        polytropic_index=polytropic_index,
        start_r=5e-8,  # Starting radius in meters
        end_r=1e-5,  # Ending radius in meters
        r_ticks_in_q_scale=[1e-6, 5e-6, 10e-6],  # Tick values for the Q scale
    )
