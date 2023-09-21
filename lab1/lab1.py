import matplotlib.pyplot as plt
import numpy as np

def main():
    # We need two equations to start
    v_dd = 10              # Supply voltage
    r = 1000               # Ohms
    q = 1.602E-19       # Charge of an electron
    k = 1.381E-23          # Boltzmann's constant
    T = 293.71                # K
    Is =  29.5E-17          # Saturation Current
    Is = 30E-6
    Is = 9.767E-15
    # Is = 1

    v_th = k*T/q
    print(v_th)
    v_d = np.arange(0, 10, 0.001)

    i_exp = exponential(v_d, Is, v_th)
    i_lin = linear(v_dd, v_d, r)
    print(i_lin)

    plt.plot(v_d, i_exp)
    plt.plot(v_d, i_lin)
    plt.axis([0, 10, 0, 0.011])
    plt.show()
    
def exponential(v, Is, v_th):
    return Is * np.e ** (v / v_th)

def linear(v_dd, v_d, r):
    return (v_dd-v_d)/r

if __name__ == '__main__':
    main()