import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def save_file(path):
    folder, file = os.path.split(path)
    for ft in ['png', 'pdf']:
        new_path = os.path.join(folder, ft, file) + '.' + ft
        plt.savefig(new_path)


def set_labels(ax, xlabel=None, ylabel="Voltage [V]", change_xtick=True, change_ytick=True, grid=True):
    if xlabel is None:
        xlabel = "Time [ms]" if change_xtick else "Time [s]"
    if change_xtick:
        ax.set_xticklabels([f"{x * 1000:.3f}" for x in ax.get_xticks().tolist()])
    if change_ytick:
        ax.set_yticklabels([f"{x * 1000:.2f}" for x in ax.get_yticks().tolist()])
        ylabel = "Voltage [mV]"
    if grid:
        ax.grid()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

def show_maxlines(ax : plt.Axes, data: pd.Series, xpos=-0.0009):
    new_data = data.copy()
    new_data = new_data.sort_values()
    max_val = new_data.iloc[int(0.98 * len(new_data))]
    min_val = new_data.iloc[int(0.02 * len(new_data))]
    # max = data.max()
    # min_val = data.min()
    ax.axhline(y=max_val, linewidth=1, linestyle='--')
    ax.annotate(xy=(xpos, max_val+0.0001), text=f"{max_val * 1000:.2f}".rstrip('0').rstrip('.') + " mV")
    ax.annotate(xy=(xpos, min_val+0.0001), text=f"{min_val * 1000:.2f}".rstrip('0').rstrip('.') + " mV")
    ax.axhline(y=min_val, linewidth=1, linestyle='--')

def plot_vin_vout(time, vin, vout, filename, xpos_vin=-0.0009, xpos_vout=-0.00025, legend_pos='best'):
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    ax.plot(time, vin, label='$V_{in}$')
    ax.plot(time, vout, label='$V_{out}$')
    set_labels(ax)
    show_maxlines(ax, vin, xpos=xpos_vin)
    show_maxlines(ax, vout, xpos=xpos_vout)
    ax.legend(loc=legend_pos)
    save_file(f'../plots/{filename}')

def sim():
    data = pd.read_csv("../sim/sim_1.csv")
    time = data['X--Trace 2::[V(3) | V(Vin)]'] - 15
    vin = data['Y--Trace 2::[V(3) | V(Vin)]']
    vout = data['Y--Trace 3::[V(2) | V(Vout)]']
    plot_vin_vout(time, vin, vout, 'sim', xpos_vin=1.1e-3, xpos_vout=1.9e-3)


def meas():
    data = pd.read_csv("../meas/scope_42.csv", header=1)
    time = data['second']
    vin = data['Volt']
    vout = data['Volt.1']
    plot_vin_vout(time, vin, vout, 'meas', xpos_vout=-130e-6)



def main():
    sim()
    meas()


if __name__ == "__main__":
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#8a787c', '#492365'])
    main()
