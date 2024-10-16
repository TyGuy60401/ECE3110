import matplotlib.pyplot as plt
import os
import pandas as pd

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
    fig = plt.figure()
    ax = plt.axes()
    fig.add_axes(ax)
    ax.set_xlabel(r"V$_{DS}$ [V]")
    ax.set_ylabel(r"I$_D$ [mA]")
    ax.grid()

    # ax.set_title(r"I$_D$ vs V$_{DS}$ Measured")
    for fileno, r, vgs_val in zip(file_numbers, r_vals, vgs_vals):
        data = pd.read_csv(f"./data/scope_{fileno}.csv", header=1)
        data['id'] = data.apply(lambda ser: get_id(ser['Volt.1'], ser['Volt'], r), axis=1)
        ax.plot(data['Volt.1'], data['id'], label=r'V$_{GS} = $' f'{vgs_val} V')

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
        
        v_ov = r'V$_{OV}$'
        i_d = r'i$_D$'
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
