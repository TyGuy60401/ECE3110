import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def graph_df(df, t_axis, *v_axes):
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    make_legend = False
    for v_axis in v_axes:
        if v_axis['label']:
            make_legend = True
        ax.plot(df[t_axis], df[v_axis['name']], label=v_axis['label'])

    if make_legend:
        ax.legend()
    return ax

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

def circuit_a():
    sim_tran = pd.read_csv('../sim_data_lab_03/circuit_a/circuit_a.csv')

    t_axis = 'X--Trace 1::[V(1) | V(Input)]'
    vin_axis = {
        'name': 'Y--Trace 1::[V(1) | V(Input)]',
        'label': "Input"
    }
    vout_axis = {
        'name': 'Y--Trace 2::[V(2) | V(Output)]',
        'label': "Output",
    }

    ax = graph_df(sim_tran, t_axis, vin_axis, vout_axis)
    set_labels(ax)
    save_file('./circuit_a/a_sim_trans')

    ax = graph_df(sim_tran, vin_axis['name'], {'name': vout_axis['name'], 'label': None})
    set_labels(ax, xlabel="Input Voltage [V]", ylabel="Output Voltage [V]", change_xtick=False)
    save_file('./circuit_a/a_sim_xy')

    meas_tran = pd.read_csv('../meas_data_lab_03/circuit_a/scope_0.csv', header=1)
    t_axis = 'second'
    vin_axis = {
        'name': 'Volt',
        'label': 'Input'
    }
    vout_axis = {
        'name': 'Volt.1',
        'label': 'Output'
    }
    ax = graph_df(meas_tran, t_axis, vin_axis, vout_axis)
    set_labels(ax)
    save_file('./circuit_a/a_meas_trans')

    meas_xy = pd.read_csv('../meas_data_lab_03/circuit_a/scope_2.csv', header=1)
    ax = graph_df(meas_xy, vin_axis['name'], {'name': vout_axis['name'], 'label': None})
    set_labels(ax, xlabel="Input Voltage [V]", ylabel="Output Voltage [V]", change_xtick=False)
    save_file('./circuit_a/a_meas_xy')



def circuit_b():
    sim_tran = pd.read_csv('../sim_data_lab_03/circuit_b/circuit_b_transient.csv')

    t_axis = 'X--Trace 1::[V(2) | V(Input)]'
    vin_axis = {
        'name': 'Y--Trace 1::[V(2) | V(Input)]',
        'label': 'Input'
    }
    vout_axis = {
        'name': 'Y--Trace 2::[V(3) | V(Output)]',
        'label': 'Output'
    }
    ax = graph_df(sim_tran, t_axis, vin_axis, vout_axis)
    set_labels(ax)
    save_file('./circuit_b/b_sim_trans')

    ax = graph_df(sim_tran, vin_axis['name'], {'name': vout_axis['name'], 'label': None})
    set_labels(ax, xlabel="Input Voltage [V]", ylabel="Output Voltage [V]", change_xtick=False)
    save_file('./circuit_b/b_sim_xy')


    meas_tran = pd.read_csv('../meas_data_lab_03/circuit_b/scope_5.csv', header=1)
    t_axis = 'second'
    vin_axis = {
        'name': 'Volt',
        'label': 'Input'
    }
    vout_axis = {
        'name': 'Volt.1',
        'label': 'Output'
    }
    ax = graph_df(meas_tran, t_axis, vin_axis, vout_axis)
    set_labels(ax)
    save_file('./circuit_b/b_meas_trans')

    meas_xy = pd.read_csv('../meas_data_lab_03/circuit_b/scope_7.csv', header=1)
    ax = graph_df(meas_xy, vin_axis['name'], {'name': vout_axis['name'], 'label': None})
    set_labels(ax, xlabel="Input Voltage [V]", ylabel="Output Voltage [V]", change_xtick=False)
    save_file('./circuit_b/b_meas_xy')


def circuit_c():
    sim_square = pd.read_csv('../sim_data_lab_03/circuit_c/circuit_c_transient_square.csv')

    t_axis = 'X--Trace 1::[V(1) | V(Input)]'
    vin_axis = {
        'name': 'Y--Trace 1::[V(1) | V(Input)]',
        'label': 'Input'
    }
    vout_axis = {
        'name': 'Y--Trace 2::[V(2) | V(Output)]',
        'label': 'Output'
    }

    ax = graph_df(sim_square, t_axis, vin_axis, vout_axis)
    set_labels(ax)
    save_file('./circuit_c/c_sim_trans')

    meas = pd.read_csv('../meas_data_lab_03/circuit_c/scope_15.csv', header=1)
    t_axis = 'second'
    vin_axis = {
        'name': 'Volt',
        'label': 'Input'
    }
    vout_axis = {
        'name': 'Volt.1',
        'label': 'Output'
    }
    ax = graph_df(meas, t_axis, vin_axis, vout_axis)
    set_labels(ax)
    save_file('./circuit_c/c_meas_trans')

    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    diff = meas[vin_axis['name']] - meas[vout_axis['name']]
    print("MEAN:", diff.mean())
    ax.plot(meas[t_axis], meas[vin_axis['name']], label='Input')
    ax.plot(meas[t_axis], meas[vout_axis['name']] + diff.mean() * 2, label='Output')
    set_labels(ax)
    ax.legend()
    save_file('./circuit_c/c_meas_-0_7')


def circuit_d():
    sim = pd.read_csv('../sim_data_lab_03/circuit_d/circuit_d_transient.csv')

    t_axis = 'X--Trace 1::[V(1) | V(Input)]'
    vin_axis = {
        'name': 'Y--Trace 1::[V(1) | V(Input)]',
        'label': 'Input'
    }
    vout_axis = {
        'name': 'Y--Trace 2::[V(3) | V(Output)]',
        'label': 'Output'
    }

    ax = graph_df(sim, t_axis, vin_axis, vout_axis)
    set_labels(ax)
    save_file('./circuit_d/d_sim_trans')

    meas = pd.read_csv('../meas_data_lab_03/circuit_d/scope_13.csv', header=1)
    t_axis = 'second'
    vin_axis = {
        'name': 'Volt',
        'label': 'Input'
    }
    vout_axis = {
        'name': 'Volt.1',
        'label': 'Output'
    }
    ax = graph_df(meas, t_axis, vin_axis, vout_axis)
    set_labels(ax)
    save_file('./circuit_d/d_meas_trans')



def main():
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#8a787c', '#492365'])
    circuit_a()
    circuit_b()
    circuit_c()
    circuit_d()

if __name__ == "__main__":
    main()
