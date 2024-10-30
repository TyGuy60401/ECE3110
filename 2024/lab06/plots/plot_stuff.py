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

    ax.plot(time, vin, label='$V_{in}$')
    ax.plot(time, vout, label='$V_{out}$')
    set_labels(ax)
    show_maxlines(ax, vin, xpos=xpos_vin)
    show_maxlines(ax, vout, xpos=xpos_vout)
    ax.legend(loc=legend_pos)
    save_file(f'../plots/{filename}')

def gain_6_67():
    data = pd.read_csv('../data/scope_37.csv', header=1)
    vin = data['Volt']
    vout = data['Volt.1'] - 8.03e-3
    plot_vin_vout(data['second'], vin, vout, 'gain6_67')

def gain_9_46():
    data = pd.read_csv("../data/scope_36.csv", header=1)
    vin = data['Volt']
    vout = data['Volt.1']
    plot_vin_vout(data['second'], vin, vout, 'gain9_46')

def rl_1meg():
    data = pd.read_csv('../data/scope_38.csv', header=1)
    vin = data['Volt']
    vout = data['Volt.1']
    plot_vin_vout(data['second'], vin, vout, 'rl_1meg', xpos_vin=-0.00025, xpos_vout=-0.0009, legend_pos='upper right')

def rl_470():
    data = pd.read_csv('../data/scope_39.csv', header=1)
    vin = data['Volt']
    vout = data['Volt.1']
    plot_vin_vout(data['second'], vin, vout, 'rl_470', legend_pos='upper right')

def vi_250m():
    data = pd.read_csv('../data/scope_40.csv', header=1)
    vin = data['Volt']
    vout = data['Volt.1']
    plot_vin_vout(data['second'], vin, vout, 'vi_250m', legend_pos='upper right')

def vi_1v():
    data = pd.read_csv('../data/scope_41.csv', header=1)
    vin = data['Volt']
    vout = data['Volt.1']
    plot_vin_vout(data['second'], vin, vout, 'vi_1v', xpos_vin=-0.0005, legend_pos='upper right')


def main():
    gain_6_67()
    gain_9_46()
    rl_1meg()
    rl_470()
    vi_250m()
    vi_1v()


if __name__ == "__main__":
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#8a787c', '#492365'])
    main()
