import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def save_file(path):
    folder, file = os.path.split(path)
    for ft in ['png', 'pdf']:
        new_path = os.path.join(folder, ft, file) + '.' + ft
        plt.savefig(new_path)

def meas():
    data_sweep_vbe = pd.read_csv("../data/sweep_vbe.csv")
    x_sweep_vbe = data_sweep_vbe['Vbe']
    ys_sweep_vbe = {
        '$I_C$': data_sweep_vbe['Ic'],
    }
    plot_x_ys(x_sweep_vbe, ys_sweep_vbe, '../plots/meas_sweep_vbe')

    data_sweep_vce_06 = pd.read_csv("../data/vbe_0.6_sweep_vce.csv")
    data_sweep_vce_07 = pd.read_csv("../data/vbe_0.7_sweep_vce.csv")
    data_sweep_vce_08 = pd.read_csv("../data/vbe_0.8_sweep_vce.csv")
    x_sweep_vce = data_sweep_vce_06['V_ce']
    ys_sweep_vce = {
        '$I_C$ for $V_{BE} = 0.8$ V': data_sweep_vce_08['Ic'],
        '$I_C$ for $V_{BE} = 0.7$ V': data_sweep_vce_07['Ic_normal'],
        '$I_C$ for $V_{BE} = 0.6$ V': data_sweep_vce_06['Ic'],
    }
    plot_x_ys(x_sweep_vce, ys_sweep_vce, '../plots/meas_sweep_vce', xlabel='$V_{CE}$ [V]')

def sim():
    data_sweep_vbe = pd.read_csv("../sim/VCE5VB.8.csv")
    x_sweep_vbe = data_sweep_vbe['X--Trace 1::[I(Q1:C) | I(PR1)]']
    ys_sweep_vbe = {
        '$I_C$': data_sweep_vbe['Y--Trace 1::[I(Q1:C) | I(PR1)]']
    }
    print(pd.DataFrame([x_sweep_vbe, ys_sweep_vbe['$I_C$']]))
    plot_x_ys(x_sweep_vbe, ys_sweep_vbe, '../plots/sim_sweep_vbe')

    data_sweep_vce_06 = pd.read_csv('../sim/ICvVce.6.csv')
    data_sweep_vce_07 = pd.read_csv('../sim/ICvVce.7.csv')
    data_sweep_vce_08 = pd.read_csv('../sim/ICvVce.8.csv')
    x_sweep_vce = data_sweep_vce_06['X--Trace 1::[I(Q1:B) | I(Ib)]']

    ys_sweep_vce = {
        '$I_C$ for $V_{BE} = 0.8$ V': data_sweep_vce_08['Y--Trace 2::[I(Q1:C) | I(Ic)]'],
        '$I_C$ for $V_{BE} = 0.7$ V': data_sweep_vce_07['Y--Trace 2::[I(Q1:C) | I(Ic)]'],
        '$I_C$ for $V_{BE} = 0.6$ V': data_sweep_vce_06['Y--Trace 2::[I(Q1:C) | I(Ic)]'],
    }
    plot_x_ys(x_sweep_vce, ys_sweep_vce, 'sim_sweep_vce', xlabel='$V_{CE}$ [V]')



def plot_x_and_ys(filename, x_col, ys, fileout):
    data_1 = pd.read_csv(filename)
    x_1 = data_1[x_col]

    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    for y_name, y_col in ys.items():
        y_vals = data_1[y_col]

        ax.plot(x_1, y_vals, label=y_name)
    ax.legend()
    ax.grid()
    save_file(fileout)

def plot_x_ys(x_ser, ys, fileout, xlabel='$V_{BE}$ [V]', ylabel='$I_C$ [A]'):
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    for y_name, y_ser in ys.items():
        ax.plot(x_ser, y_ser, label=y_name)

    ax.legend()
    ax.grid()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    save_file(fileout)


def main():
    sim()
    meas()



if __name__ == "__main__":
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#492365', '#9bc3dc', '#a275b3', '#2dbbc4', '#91c74f', '#efad21', '#f16357', '#8a787c'])
    main()
