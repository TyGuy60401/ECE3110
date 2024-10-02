import pandas as pd
import matplotlib.pyplot as plt



def half_wave_sim():
    data1 = pd.read_csv('./half-wave/half-wave-10pp.csv', sep='\t')
    data1_good = data1.loc[data1['time'] >= 0.002]
    data2 = pd.read_csv('./half-wave/half-wave-0.5pp.csv', sep='\t')
    data2_good = data2.loc[data2['time'] >= 0.002]
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(data1_good['time'], data1_good['V(n001)'], label='$V_I$')
    ax1.plot(data1_good['time'], data1_good['V(n002)'], label='$V_O$')
    ax1.set_title('$10~V_{pp}$')
    ax1.set_xticklabels([f"{x * 1000 - 2:.3f}" for x in ax1.get_xticks().tolist()])
    ax1.set_xlabel('Time [ms]')
    ax1.set_ylabel('Voltage [V]')

    ax2.plot(data2_good['time'], data2_good['V(n001)'], label='Input')
    ax2.plot(data2_good['time'], data2_good['V(n002)'], label='Output')
    ax2.set_title('$0.5~V_{pp}$')
    ax2.set_xticklabels([f"{x * 1000 - 2:.3f}" for x in ax2.get_xticks().tolist()])
    ax2.set_xlabel('Time [ms]')
    ax2.set_ylabel('Voltage [V]')

    plt.tight_layout()
    plt.savefig('./half-wave/half-wave-sim.pdf')


def peak_rectifier_sim():
    data47k = pd.read_csv('./peak/peak_47k.csv', sep='\t')
    data47k_good = data47k.loc[data47k['time'] >= 0.002]

    data4_7k = pd.read_csv('./peak/peak_4.7k.csv', sep='\t')
    data4_7k_good = data4_7k.loc[data4_7k['time'] >= 0.002]


    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)


    ax1.plot(data47k_good['time'], data47k_good['V(n001)'], label='$V_I$')
    ax1.plot(data47k_good['time'], data47k_good['V(n002)'], label='$V_O$')
    ax1.legend()
    ax1.set_title(r'$R_{47k\Omega}$')
    ax1.set_xticklabels([f"{x * 1000 - 2:.3f}" for x in ax1.get_xticks().tolist()])
    ax1.set_xlabel('Time [ms]')
    ax1.set_ylabel('Voltage [V]')

    ax1_min_val = min(data47k_good['V(n002)'])
    ax1_max_val = max(data47k_good['V(n002)'])
    print(ax1_min_val, ax1_max_val)

    ax2.plot(data4_7k_good['time'], data4_7k_good['V(n001)'], label='$V_I$')
    ax2.plot(data4_7k_good['time'], data4_7k_good['V(n002)'], label='$V_O$')
    ax2.legend()
    ax2.set_title(r'$R_{4.7k\Omega}$')
    ax2.set_xticklabels([f"{x * 1000 - 2:.3f}" for x in ax2.get_xticks().tolist()])
    ax2.set_xlabel('Time [ms]')
    ax2.set_ylabel('Voltage [V]')

    ax2_min_val = min(data4_7k_good['V(n002)'])
    ax2_max_val = max(data4_7k_good['V(n002)'])
    print(ax2_min_val, ax2_max_val)

    plt.tight_layout()
    plt.savefig('./peak/peak_sim.pdf')

def precision_sim():
    data5 = pd.read_csv('./precision/precision_10pp.csv', sep='\t')
    data5_good = data5.loc[data5['time'] >= 0.002]
    data0_5 = pd.read_csv('./precision/precision_0.5pp.csv', sep='\t')
    data0_5_good = data0_5.loc[data0_5['time'] >= 0.002]

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(data5_good['time'], data5_good['V(n002)'], label='$V_I$')
    ax1.plot(data5_good['time'], data5_good['V(n003)'], label='$V_O$')
    ax1.legend()
    ax1.set_title('$10~V_{pp}$')
    ax1.set_xlabel('Time [ms]')
    ax1.set_xticklabels([f"{x * 1000 - 2:.3f}" for x in ax1.get_xticks().tolist()])
    ax1.set_ylabel('Voltage [V]')

    ax2.plot(data0_5_good['time'], data0_5_good['V(n002)'], label='$V_I')
    ax2.plot(data0_5_good['time'], data0_5_good['V(n003)'], label='$V_O')
    ax2.legend()
    ax2.set_title('$0.5~V_{pp}$')
    ax2.set_xlabel('Time [ms]')
    ax2.set_xticklabels([f"{x * 1000 - 2:.3f}" for x in ax2.get_xticks().tolist()])
    ax2.set_ylabel('Voltage [V]')

    plt.tight_layout()
    plt.savefig('./precision/precision_sim.pdf')

def half_wave_data():
    data1 = pd.read_csv('./half-wave/half_wave_data_10vpp.csv', header=1)
    data2 = pd.read_csv('./half-wave/half_wave_data_0.5vpp.csv', header=1)

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(data1['second'], data1['Volt'], label='$V_I$')
    ax1.plot(data1['second'], data1['Volt.1'], label='$V_O$')
    ax1.set_title('$10V_{pp}$')
    ax1.set_xticklabels([f"{x * 1000 + 1:.3f}" for x in ax1.get_xticks().tolist()])
    ax1.set_xlabel('Time [ms]')
    ax1.set_ylabel('Voltage [V]')

    ax2.plot(data2['second'], data2['Volt'], label='$V_I$')
    ax2.plot(data2['second'], data2['Volt.1'], label='$V_O$')
    ax2.set_title('$0.5V_{pp}$')
    ax2.set_xticklabels([f"{x * 1000 + 1:.3f}" for x in ax2.get_xticks().tolist()])
    ax2.set_xlabel('Time [ms]')
    ax2.set_ylabel('Voltage [V]')

    plt.tight_layout()
    plt.savefig('./half-wave/half-wave-measured.pdf')

def peak_data():
    data1 = pd.read_csv('./peak/peak_data_47k.csv', header=1)
    data2 = pd.read_csv('./peak/peak_data_4.7k.csv', header=1)

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(data1['second'], data1['Volt'], label='$V_I$')
    ax1.plot(data1['second'], data1['Volt.1'], label='$V_O$')
    ax1.set_title(r'$R_{47k\Omega}$')
    ax1.set_xticklabels([f"{x * 1000 + 1:.3f}" for x in ax1.get_xticks().tolist()])
    ax1.set_xlabel('Time [ms]')
    ax1.set_ylabel('Voltage [V]')

    ax2.plot(data2['second'], data2['Volt'], label='$V_I$')
    ax2.plot(data2['second'], data2['Volt.1'], label='$V_O$')
    ax2.set_title(r'$R_{4.7k\Omega}$')
    ax2.set_xticklabels([f"{x * 1000 + 1:.3f}" for x in ax2.get_xticks().tolist()])
    ax2.set_xlabel('Time [ms]')
    ax2.set_ylabel('Voltage [V]')

    plt.tight_layout()
    plt.savefig('./peak/peak_measured.pdf')

def precision_data():
    data1 = pd.read_csv('./precision/precision_data_10vpp.csv', header=1)
    data2 = pd.read_csv('./precision/precision_data_0.5vpp.csv', header=1)

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(data1['second'], data1['Volt'], label='$V_I$')
    ax1.plot(data1['second'], data1['Volt.1'], label='$V_O$')
    ax1.set_title(r'$10V_{pp}$')
    ax1.set_xticklabels([f"{x * 1000 + 1:.3f}" for x in ax1.get_xticks().tolist()])
    ax1.set_xlabel('Time [ms]')
    ax1.set_ylabel('Voltage [V]')

    ax2.plot(data2['second'], data2['Volt'], label='$V_I$')
    ax2.plot(data2['second'], data2['Volt.1'], label='$V_O$')
    ax2.set_title(r'$0.5V_{pp}$')
    ax2.set_xticklabels([f"{x * 1000 + 1:.3f}" for x in ax2.get_xticks().tolist()])
    ax2.set_xlabel('Time [ms]')
    ax2.set_ylabel('Voltage [V]')

    plt.tight_layout()
    plt.savefig('./precision/precision_measured.pdf')

def main():
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#492365', '#aa989c'])
    half_wave_sim()
    peak_rectifier_sim()
    precision_sim()

    half_wave_data()
    peak_data()
    precision_data()


if __name__ == "__main__":
    main()
