import numpy as np

def iterative(V_DD, R, V, I, v_prec = 0.00001, i_prec = 0.00001, n=10000):
    """Find the voltage and current through a 
    series resitor-diode circuit using the iterative
    method."""

    v_1 = V
    i_1 = I

    count = 0
    for _ in range(n):
        count += 1
        i_new = (V_DD - v_1) / R
        v_new = v_1 + 25.9e-3 * np.log(i_new / i_1)
        if abs(v_1 - v_new) < v_prec and abs(i_1 - i_new) < i_prec:
            break
        v_1 = v_new
        i_1 = i_new
    print(count)
    return v_1, i_1


def main():
    # v, i = iterative(10, 1000, 0.93, 1, 0.000000000001)
    v, i = iterative(5, 12000, 0.7, 1e-3)
    print(f"Voltage: {v}")
    print(f"Current: {i}")

if __name__ == "__main__":
    main()
