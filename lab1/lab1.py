import matplotlib.pyplot as plt
import numpy as np

def main():
    # We need two equations to start
    v_dd = 10              # Supply voltage
    r = 1000               # Ohms
    q = 1.602E-19       # Charge of an electron
    k = 1.381E-23          # Boltzmann's constant
    T = 293.71                # K
    # Is =  29.5E-17          # Saturation Current
    # Is = 30E-6
    Is = 9.767E-15
    # Is = 1

    v_th = k*T/q
    v_d = np.arange(0, 10, 0.0001)

    i_exp = exponential(v_d, Is, v_th)
    i_lin = linear(v_dd, v_d, r)

    iteration(1.1, 1, 25.9e-3, v_dd, r)

    plt.plot(v_d, i_exp, label='$I_s e^{\\frac{v_D}{v_{th}}}$')
    plt.plot(v_d, i_lin, label='$\\frac{v_{DD}-v_D}{R}$')
    diff = abs(i_exp - i_lin)
    diff_list = list(diff)
    idx = diff_list.index(min(diff_list))
    # print(v_d[idx], i_exp[idx])
    plt.plot(v_d[idx], i_exp[idx], 'o', color='black')
    plt.annotate(f"$v_D$: {v_d[idx]:.3f} V, $i_D$: {i_exp[idx]*1e3:.3f} mA",
                 (v_d[idx], i_exp[idx]),
                 textcoords='offset points',
                 xytext=(20, 10), ha='left')

    plt.axis([0, 5, 0, 0.011])
    plt.legend(loc='lower right', fontsize='16')
    plt.title("Solving for Voltage Across Diode\n$\\frac{v_{DD}-v_D}{R}=I_S e^{\\frac{v_D}{v_{th}}}$")
    # plt.tight_layout()
    plt.xlabel("Voltage across the diode $v_D$")
    plt.ylabel("Current through the diode $i_D$")
    plt.savefig('./out.png')


def iteration(v0, i0, v_th, v_dd, r):
    v_d = v0
    i_d = i0
    
    diff = 10000
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    count = 0
    while True:
        if count >= 1000:
            print("Count maximum reached, exiting")
            break
        some_i = eq2(v_dd, v_d, r)
        some_v = eq1(v_d, some_i, i_d, v_th)
        # plt.plot(v_d, i_d, 'o', color=colors[count % len(colors)])
        if abs(some_v - v_d) < 0.0000001:
            print(f"We did it {count} iterations\nv: {some_v} i: {some_i}")
            break
        v_d = some_v
        i_d = some_i
        count += 1
    
def eq1(v1, i2, i1, v_th):
    return v1 + 2.3*v_th*np.log10(i2/i1)

def eq2(vdd, vd, r):
    return (vdd-vd)/r

    
def exponential(v, Is, v_th):
    return Is * np.e ** (v / v_th)

def linear(v_dd, v_d, r):
    return (v_dd-v_d)/r

if __name__ == '__main__':
    main()