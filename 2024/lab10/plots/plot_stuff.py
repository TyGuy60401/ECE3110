import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def save_file(path):
    folder, file = os.path.split(path)
    for ft in ['png', 'pdf']:
        new_path = os.path.join(folder, ft, file) + '.' + ft
        plt.savefig(new_path)


def set_labels(ax, xlabel=None, ylabel="Voltage [V]", change_xtick=True, grid=True):
    if xlabel is None:
        xlabel = "Time [ms]" if change_xtick else "Time [s]"
    if change_xtick:
        ax.set_xticklabels([f"{x * 1000:.3f}" for x in ax.get_xticks().tolist()])
    if grid:
        ax.grid()

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


def show_maxlines(ax : plt.Axes, data, xpos=-0.0009):
    max = data.max()
    min = data.min()
    ax.axhline(y=max, linewidth=1, linestyle='--')
    ax.annotate(xy=(xpos, max+0.0007), text=f"{max * 1000:.2f}".rstrip('0').rstrip('.') + " mV")
    ax.annotate(xy=(xpos, min+0.0007), text=f"{min * 1000:.2f}".rstrip('0').rstrip('.') + " mV")
    ax.axhline(y=min, linewidth=1, linestyle='--')
 

def plot_vin_vout(time, vin, vout, filename, xpos_vin=-0.0009, xpos_vout=-0.00025, legend_pos='best'):
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    # plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#8a787c', '#492365'])

    ax.plot(time, vin, label='$V_{in}$', color='#8a787c')
    ax.set_ybound([-3 * abs(min(vin)), 3 * abs(max(vin))])

    ax2 = ax.twinx()
    ax2.plot(time, vout, label='$V_{out}$', color='#492365')

    ax.set_xticklabels([f"{x * 1000:.3f}" for x in ax.get_xticks().tolist()])
    ax.set_xlabel("Time [ms]")
    ax.set_ylabel("Voltage In [V]")

    ax2.set_ylabel("Voltage out [V]")
    ax.grid()

    lines_1, labels_1 = ax.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

    plt.tight_layout()
    save_file(f'../plots/{filename}')

"""
X--Trace 1::[V(3) | V(Vi)]
Y--Trace 1::[V(3) | V(Vi)]

X--Trace 2::[V(8) | V(Vo)]
Y--Trace 2::[V(8) | V(Vo)]

X--Trace 3::[V(1) | V(Vsig)]
Y--Trace 3::[V(1) | V(Vsig)]

X--Trace 4::[I(Q1:B) | I(Ib)]
Y--Trace 4::[I(Q1:B) | I(Ib)]

X--Trace 5::[I(Q1:C) | I(Ic)]
Y--Trace 5::[I(Q1:C) | I(Ic)]

X--Trace 6::[-I(Q1:E) | I(Ie)]
Y--Trace 6::[-I(Q1:E) | I(Ie)]

X--Trace 7::[V(6) | V(Vc)]
Y--Trace 7::[V(6) | V(Vc)]

X--Trace 8::[V(5) | V(Ve)]
Y--Trace 8::[V(5) | V(Ve)]
"""

def simulation():
    data = pd.read_csv("sim_results_csv.csv")
    time = data['X--Trace 1::[V(3) | V(Vi)]']
    time -= 105e-3
    vin = data['Y--Trace 1::[V(3) | V(Vi)]']
    vout = data['Y--Trace 2::[V(8) | V(Vo)]']
    plot_vin_vout(time, vin, vout, 'simulation')

def measurements():
    data = pd.read_csv("scope_3.csv", header=1)

def main():
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#8a787c', '#492365'])
    simulation()

if __name__ == "__main__":
    main()
