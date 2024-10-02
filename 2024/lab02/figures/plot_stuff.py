import pandas as pd
import matplotlib.pyplot as plt

def get_max_min(df, label, *col_names):
    print(label)
    for col in col_names:
        col_max = df[col].max()
        col_min = df[col].min()
        diff = col_max - col_min
        print(f"{col}:\nMax: {col_max}\nMin: {col_min}\nDiff: {diff}\n")


def half_wave_sim():
    data1 = pd.read_csv('./half-wave/half-wave-10pp.csv', sep='\t')
    data1_good = data1.loc[data1['time'] >= 0.002]
    data2 = pd.read_csv('./half-wave/half-wave-0.5pp.csv', sep='\t')
    data2_good = data2.loc[data2['time'] >= 0.002]

    data3 = pd.read_csv('./half-wave/half-wave_10V_9744.csv', sep='\t')
    data3_good = data3.loc[data3['time'] >= 0.002]

    data4 = pd.read_csv('./half-wave/half-wave_0.5V_9744.csv', sep='\t')
    data4_good = data4.loc[data4['time'] >= 0.002]


    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(data1_good['time'], data1_good['V(n001)'], label='$V_I$')
    ax1.plot(data1_good['time'], data1_good['V(n002)'], label='$V_O$')
    ax1.set_title('$10~V_{pp}$ Simulated')
    ax1.legend()
    ax1.set_xticklabels([f"{x * 1000 - 2:.3f}" for x in ax1.get_xticks().tolist()])
    ax1.set_xlabel('Time [ms]')
    ax1.set_ylabel('Voltage [V]')

    ax2.plot(data2_good['time'], data2_good['V(n001)'], label='Input')
    ax2.plot(data2_good['time'], data2_good['V(n002)'], label='Output')
    ax2.set_title('$0.5~V_{pp}$ Simulated')
    ax2.legend()
    ax2.set_xticklabels([f"{x * 1000 - 2:.3f}" for x in ax2.get_xticks().tolist()])
    ax2.set_xlabel('Time [ms]')
    ax2.set_ylabel('Voltage [V]')

    get_max_min(data1_good, 'Half wave sim 10Vpp', 'V(n002)')
    get_max_min(data2_good, 'Half wave sim 0.5Vpp', 'V(n002)')
    get_max_min(data3_good, 'Half wave sim 10Vpp 9.744k', 'V(n002)')
    get_max_min(data4_good, 'Half wave sim 0.5Vpp 9.744k', 'V(n002)')
    
    plt.tight_layout()
    plt.savefig('./half-wave/half-wave-sim.pdf')


def peak_rectifier_sim():
    data47k = pd.read_csv('./peak/peak_47k.csv', sep='\t')
    data47k_good = data47k.loc[data47k['time'] >= 0.002]

    data4_7k = pd.read_csv('./peak/peak_4.7k.csv', sep='\t')
    data4_7k_good = data4_7k.loc[data4_7k['time'] >= 0.002]

    data_44850 = pd.read_csv('./peak/peak_44850.csv', sep='\t')
    data_44850_good = data_44850.loc[data_44850['time'] >= 0.002]
    data_4607 = pd.read_csv('./peak/peak_4607.csv', sep='\t')
    data_4607_good = data_4607.loc[data_4607['time'] >= 0.002]


    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)


    ax1.plot(data47k_good['time'], data47k_good['V(n001)'], label='$V_I$')
    ax1.plot(data47k_good['time'], data47k_good['V(n002)'], label='$V_O$')
    ax1.legend()
    ax1.set_title(r'$R_{47k\Omega}$ Simulated')
    ax1.set_xticklabels([f"{x * 1000 - 2:.3f}" for x in ax1.get_xticks().tolist()])
    ax1.set_xlabel('Time [ms]')
    ax1.set_ylabel('Voltage [V]')


    ax2.plot(data4_7k_good['time'], data4_7k_good['V(n001)'], label='$V_I$')
    ax2.plot(data4_7k_good['time'], data4_7k_good['V(n002)'], label='$V_O$')
    ax2.legend()
    ax2.set_title(r'$R_{4.7k\Omega}$ Simulated')
    ax2.set_xticklabels([f"{x * 1000 - 2:.3f}" for x in ax2.get_xticks().tolist()])
    ax2.set_xlabel('Time [ms]')
    ax2.set_ylabel('Voltage [V]')

    get_max_min(data47k_good, 'Peak sim 47k', 'V(n002)')
    get_max_min(data4_7k_good, 'Peak sim 4.7k', 'V(n002)')
    get_max_min(data_44850_good, 'Peak sim 44.8k', 'V(n002)')
    get_max_min(data_4607_good, 'Peak sim 4.607k', 'V(n002)')


    plt.tight_layout()
    plt.savefig('./peak/peak_sim.pdf')

def precision_sim():
    data5 = pd.read_csv('./precision/precision_10pp.csv', sep='\t')
    data5_good = data5.loc[data5['time'] >= 0.002]
    data0_5 = pd.read_csv('./precision/precision_0.5pp.csv', sep='\t')
    data0_5_good = data0_5.loc[data0_5['time'] >= 0.002]

    data5_9744 = pd.read_csv('./precision/precision_data_10Vpp_9744.csv', sep='\t')
    data5_9744_good = data5_9744.loc[data5_9744['time'] >= 0.002]
    data0_5_9744 = pd.read_csv('./precision/precision_data_0.5vpp_9744.csv', sep='\t')
    data0_5_9744_good = data0_5_9744.loc[data0_5_9744['time'] >= 0.002]

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(data5_good['time'], data5_good['V(n002)'], label='$V_I$')
    ax1.plot(data5_good['time'], data5_good['V(n003)'], label='$V_O$')
    ax1.legend()
    ax1.set_title('$10~V_{pp}$ Simulated')
    ax1.set_xlabel('Time [ms]')
    ax1.set_xticklabels([f"{x * 1000 - 2:.3f}" for x in ax1.get_xticks().tolist()])
    ax1.set_ylabel('Voltage [V]')

    ax2.plot(data0_5_good['time'], data0_5_good['V(n002)'], label='$V_I')
    ax2.plot(data0_5_good['time'], data0_5_good['V(n003)'], label='$V_O')
    ax2.legend()
    ax2.set_title('$0.5~V_{pp}$ Simulated')
    ax2.set_xlabel('Time [ms]')
    ax2.set_xticklabels([f"{x * 1000 - 2:.3f}" for x in ax2.get_xticks().tolist()])
    ax2.set_ylabel('Voltage [V]')

    get_max_min(data5_good, 'Precision sim 10Vpp', 'V(n003)')
    get_max_min(data0_5_good, 'Precision sim 0.5Vpp', 'V(n003)')
    get_max_min(data5_9744_good, 'Precision sim 10Vpp 9744', 'V(n003)')
    get_max_min(data0_5_9744_good, 'Precision sim 0.5Vpp 9744', 'V(n003)')
    

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
    ax1.set_title('$10V_{pp}$ Measured')
    ax1.legend()
    ax1.set_xticklabels([f"{x * 1000 + 1:.3f}" for x in ax1.get_xticks().tolist()])
    ax1.set_xlabel('Time [ms]')
    ax1.set_ylabel('Voltage [V]')

    ax2.plot(data2['second'], data2['Volt'], label='$V_I$')
    ax2.plot(data2['second'], data2['Volt.1'], label='$V_O$')
    ax2.set_title('$0.5V_{pp}$ Measured')
    ax2.legend()
    ax2.set_xticklabels([f"{x * 1000 + 1:.3f}" for x in ax2.get_xticks().tolist()])
    ax2.set_xlabel('Time [ms]')
    ax2.set_ylabel('Voltage [V]')

    get_max_min(data1, 'Half wave meas 10Vpp', 'Volt.1')
    get_max_min(data2, 'Half wave meas 0.5Vpp', 'Volt.1')

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
    ax1.set_title(r'$R_{47k\Omega}$ Measured')
    ax1.legend()
    ax1.set_xticklabels([f"{x * 1000 + 1:.3f}" for x in ax1.get_xticks().tolist()])
    ax1.set_xlabel('Time [ms]')
    ax1.set_ylabel('Voltage [V]')

    ax2.plot(data2['second'], data2['Volt'], label='$V_I$')
    ax2.plot(data2['second'], data2['Volt.1'], label='$V_O$')
    ax2.set_title(r'$R_{4.7k\Omega}$ Measured')
    ax2.legend()
    ax2.set_xticklabels([f"{x * 1000 + 1:.3f}" for x in ax2.get_xticks().tolist()])
    ax2.set_xlabel('Time [ms]')
    ax2.set_ylabel('Voltage [V]')

    get_max_min(data1, 'Peak meas 47k', 'Volt.1')
    get_max_min(data2, 'Peak meas 4.7k', 'Volt.1')

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
    ax1.set_title(r'$10V_{pp}$ Measured')
    ax1.legend()
    ax1.set_xticklabels([f"{x * 1000 + 1:.3f}" for x in ax1.get_xticks().tolist()])
    ax1.set_xlabel('Time [ms]')
    ax1.set_ylabel('Voltage [V]')

    ax2.plot(data2['second'], data2['Volt'], label='$V_I$')
    ax2.plot(data2['second'], data2['Volt.1'], label='$V_O$')
    ax2.set_title(r'$0.5V_{pp}$ Measured')
    ax2.legend()
    ax2.set_xticklabels([f"{x * 1000 + 1:.3f}" for x in ax2.get_xticks().tolist()])
    ax2.set_xlabel('Time [ms]')
    ax2.set_ylabel('Voltage [V]')

    get_max_min(data1, 'Precision meas 10Vpp', 'Volt.1')
    get_max_min(data2, 'Precision meas 0.5Vpp', 'Volt.1')

    plt.tight_layout()
    plt.savefig('./precision/precision_measured.pdf')

def main():
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#aa989c', '#492365'])
    half_wave_sim()
    peak_rectifier_sim()
    precision_sim()

    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#aa989c', '#f16357'])
    half_wave_data()
    peak_data()
    precision_data()


if __name__ == "__main__":
    main()
