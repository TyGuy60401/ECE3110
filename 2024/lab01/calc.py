import numpy as np
import matplotlib.pyplot as plt

# GLOBALS
T = 294.26
k = 1.380649e-23
q = 1.6021733e-19
V_TH = k * T / q

def i_r(v, V_S, R):
    "Value of the current through the resistor for a given V_S, v, and R"
    return (V_S - v) / R

def i_d(v, I_s, V_th):
    "Value of the current through the diode for a given I_s, V_th, and v"
    return I_s * np.exp(v / V_th)

def main():
    v_i_vals = [
        {
            'v': 0.5997,
            'i': 1.417e-3,
            'prefix': "measured_diode",
        },
        {
            'v': 0.93, 
            'i': 1,
            'prefix': "datasheet_diode",
        }
    ]
    for vals in v_i_vals:
        v = vals['v']
        i = vals['i']
        pre = vals['prefix']
        for v_s in [10, 1.2, 0.75, 0.55]:
            R = 1000
            V_th = 25.9e-3
            calc_and_plot(v, i, V_th, v_s, R, pre)


def calc_and_plot(V_F, I_F, V_th, V_S, R, prefix):
    """
    Parameters
    ----------
    V_F : float
        The forward voltage of a characterizing point of the diode (used to calculate I_s)
    I_F : float
        The forward current of a characterizing point of the diode (used to calculate I_s)
    V_th : float
        The thermal voltage for use in the calculations
    V_S : float
        The supply voltage in Volts in the circuit
    R   : float
        The value in Ohms for the resistor in the circuit
    prefix : string
        Prefix for the file that will be saved
    """
    v_vals = np.linspace(0, V_S, 100000)

    I_s = I_F / np.exp(V_F / V_th)
    print("I_s:", I_s)
    i_r_vals = [i_r(v, V_S, R) for v in v_vals]
    i_d_vals = [i_d(v, I_s, V_th) for v in v_vals]

    # Solving for V_D and V_I
    diff_vals = np.array(i_r_vals) - np.array(i_d_vals)
    diff_vals = np.abs(diff_vals)
    idx = diff_vals.tolist().index(min(diff_vals))
    V_D = v_vals[idx]
    I_D = i_d_vals[idx]
    print("V_D:", V_D)
    print("I_D:", I_D)

    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    ax.set_title("Graphical solution for voltage and current through diode.")
    ax.set_xlabel("Voltage [V]")
    ax.set_ylabel("Current [A]")

    y_bottom = -V_S / R / 8
    y_top = V_S / R * 1.1
    ax.set_ylim([y_bottom, y_top]) # type:ignore

    ax.plot(v_vals, i_r_vals, 'xkcd:silver', label=r'$i_D = I_s e^{v / v_{th}}$')
    ax.plot(v_vals, i_d_vals, '#492365', label=r'$i_D = \frac{V_S - v}{R}$')
    ax.plot(v_vals[idx], i_d_vals[idx], marker='o', color='#492365', linestyle='', label=f'Solution')
    y_diff = (y_top - y_bottom) / 30
    x_offset = 0.05
    x_size = (ax.get_xlim()[1] - ax.get_xlim()[0])
    if V_D > x_size / 2:
        x_offset = - x_size / 3
    ax.annotate(f'V: {V_D:.3f} V, I: {I_D*1000:.2f} mA', xy=(V_D + x_offset, I_D + y_diff))
    if I_F < y_top * 0.9:
        ax.plot(V_F, I_F, 'o', marker='o', color='xkcd:silver', linestyle='', label='Characteristic point')
        x_offset = 0.05
        if V_F > (ax.get_xlim()[1] - ax.get_xlim()[0]) / 2:
            x_offset = -2
        ax.annotate(f'V: {V_F:.3f} V, I: {I_F*1000:.2f} mA', xy=(V_F + x_offset, I_F + y_diff))

    ax.legend()
    ax.grid()

    # plt.show()

    for f_type in ['pdf', 'png']:
        fig_name = f"plots/{f_type}/{prefix}_{V_S}V.{f_type}"
        print(f"Saving {fig_name} ...")
        plt.savefig(fig_name)


if __name__ == "__main__":
    main()
