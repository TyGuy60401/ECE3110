import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

def get_id(V_ds, V_dd, R_D):
    return (-V_ds + V_dd )/ R_D



def save_file(path):
    folder, file = os.path.split(path)
    for ft in ['png', 'pdf']:
        new_path = os.path.join(folder, ft, file) + '.' + ft
        plt.savefig(new_path)

def meas_sweep_vgs():
    data = pd.read_csv("./data/scope_24.csv", header=1)
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    V_dd = 5
    R_D = 1e3
    data['id'] = data['Volt.1'].apply(lambda vds: get_id(vds, V_dd, R_D))

    ax.plot(data['Volt'], data['id'])
    # ax.set_title(r"I$_D$ vs V$_{GS}$ Measured")

    ax.grid()
    ax.set_xlabel(r"V$_{GS}$ [V]")
    ax.set_yticklabels([f"{int(x * 1000)}" for x in list(ax.get_yticks().tolist())])
    ax.set_ylabel(r"I$_D$ [mA]")
    save_file('./plots/sweep_vgs')

def meas_sweep_vds(xlim, ylim):
    file_numbers = reversed(["28", "34", "35"])
    r_vals = reversed([330, 80, 33])
    vgs_vals = reversed([2.5, 3.0, 3.5])
    vovs = reversed([(0.39, 8.5e-3), (0.8, 64e-3), (1.2, 150e-3)])
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.set_xlabel(r"V$_{DS}$ [V]")
    ax.set_ylabel(r"I$_D$ [mA]")
    ax.grid()

    # ax.set_title(r"I$_D$ vs V$_{DS}$ Measured")
    for fileno, r, vgs_val, vov in zip(file_numbers, r_vals, vgs_vals, vovs):
        data = pd.read_csv(f"./data/scope_{fileno}.csv", header=1)
        data['id'] = data.apply(lambda ser: get_id(ser['Volt.1'], ser['Volt'], r), axis=1)
        # ax.plot(data['Volt.1'], data['id'], label=r'V$_{GS} = $' f'{vgs_val} V')

        data_sorted = data.sort_values(by='Volt.1')
        data_grouped = data_sorted.groupby('Volt.1').mean().reset_index()
        vd_new = np.linspace(data_grouped['Volt.1'].min(), data_grouped['Volt.1'].max(), num=1000)
        id_new = np.interp(vd_new, data_grouped['Volt.1'], data_grouped['id'])
        data_new = pd.DataFrame({'vd': vd_new, 'id': id_new})
        ax.plot(data_new['vd'], data_new['id'], label=r'V$_{GS} = $' f'{vgs_val} V')


        v_ov = r'V$_{OV}$'
        i_d = r'I$_D$'
        ax.vlines(x=vov[0], ymax=vov[1], ymin=0, linestyles='dashed')
        ax.annotate(text=f'{v_ov} = {vov[0]} V\n{i_d} = {vov[1] * 1000:.1f} mA', xy=(vov[0] + 0.1, vov[1] - 0.012),
                    bbox=dict(boxstyle='round,pad=0.5', edgecolor='gray', facecolor='white', alpha=0.7)
                    )

        

    ax.legend()
    ax.set_yticklabels([f"{round(x * 1000)}" for x in list(ax.get_yticks().tolist())])
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    save_file(f"./plots/sweep_vds")




def sim_sweep_vgs():
    data = pd.read_csv('./sim/sweep_vgs_5V.csv')
    vgs = 'X--Trace 1::[-I(R1:1) | I(PR1)]'
    vds = 'Y--Trace 1::[-I(R1:1) | I(PR1)]'


    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    ax.plot(data[vgs], data[vds])

    ax.set_xlabel(r"V$_{GS}$ [V]")
    ax.set_yticklabels([f"{int(x * 1000)}" for x in list(ax.get_yticks().tolist())])
    ax.set_ylabel(r"I$_D$ [mA]")
    ax.grid()

    # ax.set_title(r"I$_D$ vs V$_{GS}$ Simulated")

    save_file('./plots/sim_sweep_vgs')

def sim_sweep_vds():
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)

    file_numbers = reversed(['2.5', '3.0', '3.5'])

    for file_no in file_numbers:
        data = pd.read_csv(f"./sim/sweep_vds_{file_no}.csv")
        ax.plot(data[data.columns[0]], data[data.columns[1]], label=r'V$_{GS}$ = ' f'{file_no} V')
        threshold = data[data.columns[1]].max() / 200
        data['next_value'] = data[data.columns[1]].shift(-1)
        data['difference'] = abs(data[data.columns[1]] - data['next_value'])
        close_values = data[data['difference'] < threshold]
        x_point = close_values[close_values.columns[0]].iloc[0]
        y_max = close_values[close_values.columns[1]].iloc[0]
        x_1 = close_values[close_values.columns[0]].iloc[0]
        y_1 = close_values[close_values.columns[1]].iloc[0]
        x_2 = close_values[close_values.columns[0]].iloc[-1]
        y_2 = close_values[close_values.columns[1]].iloc[-1]

        # m = (y2 - y1) / (x2 - x1)
        # (y-y1) = m(x - x1)
        # (0-y1)/m + x1 = x when y = 0
        slope = (y_2 - y_1) / (x_2 - x_1)
        x_int = -y_1/slope + x_1
        print(file_no)
        print('slope:', slope)
        print('Early voltage:', x_int)
        

        
        v_ov = r'V$_{OV}$'
        i_d = r'I$_D$'
        ax.vlines(x=x_point, ymax=y_max, ymin=0, linestyles='dashed')
        ax.annotate(text=f'{v_ov} = {x_point} V\n{i_d} = {y_max * 1000:.1f} mA', xy=(x_point + 0.1, y_max - 0.012),
                    bbox=dict(boxstyle='round,pad=0.5', edgecolor='gray', facecolor='white', alpha=0.7)
                    )


    ax.set_yticklabels([f"{round(x * 1000)}" for x in list(ax.get_yticks().tolist())])
    ax.grid()
    ax.set_xlabel(r"V$_{DS}$ [V]")
    ax.set_ylabel(r"I$_D$ [mA]")
    ax.legend()
    # ax.set_title(r"I$_D$ vs V$_{DS}$ Simulated")
    
    save_file('./plots/sim_sweep_vds')
    return ax.get_xlim(), ax.get_ylim()

def main():
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#492365', '#9bc3dc', '#a275b3', '#2dbbc4', '#91c74f', '#efad21', '#f16357', '#8a787c'])

    sim_sweep_vgs()
    xlim, ylim = sim_sweep_vds()
    meas_sweep_vgs()
    meas_sweep_vds(xlim, ylim)

if __name__ == '__main__':
    main()
