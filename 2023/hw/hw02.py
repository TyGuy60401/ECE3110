import numpy as np

def p1(rs, rl1, av1, rs1, rl2, av2, rs2, rl3, av3, rs3, rl):
    vs = 1
    v1 = vs * rl1 / (rl1 + rs)
    v2 = 10 * v1 * rl2 / (rs1 + rl2)
    v3 = 80 * v2 * rl3 / (rl3 + rs2)
    vl = 1 * v3 * rl / (rl + rs3)
    print("Voltage gain:", vl / vs)
    print("Voltage gain (v1):", vl / v1)
    i_s = vs / (rs + rl1)
    i_l = vl / rl
    print("Current gain:", i_l / i_s)
    print("Power gain:", vl / vs * i_l / i_s)
    print("Power gain:", vl / v1 * i_l / i_s)

def p2():
    rl = 10 ** (39 / 20) / 0.008
    w = 2 * np.pi * 100e3
    c = rl / (w * 10 ** (3/ 20))
    tau = 123

    print("R_load:", rl)
    print("C_load:", c)

def p4(avo, ri_mult, rl_mult):
    print("Avo:", avo)
    print("Ri_mult:", ri_mult)
    print("Rl_mult:", rl_mult)


    vi = 1 * (ri_mult / (ri_mult + 1))
    vo = avo * vi * (rl_mult / (rl_mult + 1))

    print("Voltage Gain [V/V]:", vo)

def p5(v_gain, ri, ro, vs, rs, rl):
    vi = vs * (ri/(ri + rs))
    vl = v_gain * vi * (rl / (rl + ro))
    print("Load voltage:", vl)
    av = 20 * np.log10(vl/vs)
    print("Overall Av:", av)
    i_s = vs / (rs + ri)
    i_l = vl / rl
    ai = 20 * np.log10(i_l/i_s)
    print("Overall Ai:", ai)
    print("Overall Ap:", (ai + av)/2)

def main():
    # p1(100e3, 1e6, 10, 1100, 110000, 80, 1100, 9000, 1, 11, 80)
    # p2()
    # p4(11, 11, 10)
    # p4(11, 1.1, 1.1)
    # p4(11, 0.09, 0.12)
    p5(1.2, 900e3, 8, 0.9, 110e3, 100)

    
    

if __name__ == "__main__":
    main()
