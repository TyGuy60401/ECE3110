import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


def get_id(V_ds, V_dd, R_D):
    return (-V_ds + V_dd )/ R_D


def plot_sweep_vgs():
    data = pd.read_csv("./data/scope_24.csv", header=1)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    V_dd = 5
    R_D = 1e3
    vals = [get_id(v_ds, V_dd, R_D) for v_ds in data['Volt.1']]

    ax.plot(data['Volt'], vals)
    ax.set_title(f"Sweep VGS 0 - 5 V")
    print(data)
    plt.savefig("./plots/sweep_vgs")

def plot_sweep_vds(R_D, filenumber):
    data = pd.read_csv(f"./data/scope_{filenumber}.csv", header=1)
    V_dd = 5
    
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    vals = []
    vds = list(data['Volt.1'])
    vdd = list(data['Volt'])
    for i in range(len(data['Volt'])):
        vals.append(get_id(vds[i], vdd[i], R_D))

    # vals = [get_id(v_ds, V_dd, R_D) for v_ds in data['Volt.1']]
    ax.plot(data['Volt.1'], vals)
    # ax.plot(data['Volt'], data['Volt.1'])
    ax.set_title(f"{filenumber}.csv - {R_D} $\\Omega$")

    plt.savefig(f"./plots/sweep_vds_{filenumber}_{R_D}")



def main():
    plot_sweep_vgs()
    plot_sweep_vds(330, "28")
    plot_sweep_vds(80, "34")
    plot_sweep_vds(33, "35")


if __name__ == '__main__':
    main()