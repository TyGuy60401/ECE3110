import pandas as pd
import matplotlib.pyplot as plt


def half_wave_sim():
    data1 = pd.read_csv('./half-wave/half-wave-10pp.csv', sep='\t')
    data2 = pd.read_csv('./half-wave/half-wave-0.5pp.csv', sep='\t')
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(data1['time'], data1['V(n001)'], label='$V_I$')
    ax1.plot(data1['time'], data1['V(n002)'], label='$V_O$')
    ax1.set_title('$10~V_{pp}$')

    ax2.plot(data2['time'], data2['V(n001)'], label='Input')
    ax2.plot(data2['time'], data2['V(n002)'], label='Output')
    ax2.set_title('$0.5~V_{pp}$')

    plt.tight_layout()
    plt.savefig('./half-wave/half-wave-sim.pdf')


def peak_rectifier_sim():
    data47k = pd.read_csv('./peak/peak_47k.csv', sep='\t')
    data4_7k = pd.read_csv('./peak/peak_4.7k.csv', sep='\t')

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(data47k['time'], data47k['V(n001)'], label='$V_I$')
    ax1.plot(data47k['time'], data47k['V(n002)'], label='$V_O$')
    ax1.legend()
    ax1.set_title('$R_{47k}$')

    ax2.plot(data4_7k['time'], data4_7k['V(n001)'], label='$V_I$')
    ax2.plot(data4_7k['time'], data4_7k['V(n002)'], label='$V_O$')
    ax2.legend()
    ax2.set_title('$R_{4.7k}$')

    plt.tight_layout()
    plt.savefig('./peak/peak_sim.pdf')

def precision():
    data5 = pd.read_csv('./precision/precision_10pp.csv', sep='\t')
    data0_5 = pd.read_csv('./precision/precision_0.5pp.csv', sep='\t')

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(data5['time'], data5['V(n002)'], label='$V_I$')
    ax1.plot(data5['time'], data5['V(n003)'], label='$V_O$')
    ax1.legend()
    ax1.set_title('$10~V_{pp}$')

    ax2.plot(data0_5['time'], data0_5['V(n002)'], label='$V_I')
    ax2.plot(data0_5['time'], data0_5['V(n003)'], label='$V_O')
    ax2.legend()
    ax2.set_title('$0.5~V_{pp}$')

    plt.tight_layout()
    plt.savefig('./precision/precision_sim.pdf')

def main():
    half_wave_sim()
    peak_rectifier_sim()
    precision()


if __name__ == "__main__":
    main()