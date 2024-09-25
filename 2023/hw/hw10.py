import numpy as np
import matplotlib as mpl

eng = mpl.ticker.EngFormatter()

def q1(vth, kpn, aspect, l, id, vd1, vd2):
    # Looking for the following:
    # Overdrive Voltage [V]
    # Gate Voltage [V]
    # Minimum drain voltage [V]
    # Output resistance [kOhms]
    # Drain current for V1 [µA]
    # Drain current for V2 [µA]
    # Output resistance in saturation [kOhms]
    ""
    # Vov = vgs - vth



def q2(vdd, vss, vth, kn, aspect, i_d, vd):
    # Drain resistance Rd [kOhms]
    # Source resistance Rs [kOhms]

    # Finding Rd
    # v = iR
    # R = v/i
    rd = (vdd - vd) / (i_d)
    print(f"Rd: {eng(rd)}")

    # Finding Rs
    vgs = np.sqrt(i_d * 2 / kn) + vth
    vgsm = -np.sqrt(i_d * 2 / kn) + vth
    print(f"Vgs: {eng(vgs)}")
    print(f"Vgsm: {eng(vgsm)}")
    
    # Assuming we take vgs and not vgsm
    rs = (-vgsm - vss) / i_d
    print(f"Rs: {eng(rs)}")

def q3(vd, vth, kpn, aspect):
    ""
    vgs = vd
    i_d = 0.5 * kpn  * aspect * (vd - vth) ** 2
    rd = (1.8 - vd) / i_d
    print(f"Rd: {eng(rd)}")

def q4(vd, vth, kpn, aspect):
    " Looking for Resistance R2 [kOhms]"
    vgs = vd
    vds = vgs - vth
    vd = vds

    i_d = 0.5 * kpn * aspect * (vgs - vth) ** 2
    rd = (1.8 - vd) / i_d
    print(f"Rd: {eng(rd)}")

def q5(vdd, vd, vth, kpn, aspect):
    " Looking for several"
    # Finding Rd
    i_d = 0.5 * kpn * aspect * (vdd - vth) ** 2
    rd = (vdd - vd) / i_d
    print(f"Rd: {eng(rd)}")
     
    # Finding Rds
    vds = vd - 0
    rds = vds / i_d
    print(f"Rds: {eng(rds)}")

    # Finding i_d if rd is doubled
    # i_d should be the same
    print(f"Id: {eng(i_d)}")


    # rd = (vdd - vd) / i_d
    # rd * i_d = vdd - vd
    # vd = vdd - rd * i_d
    vd_new = vdd - rd*2 * i_d
    print(f"Vdnew: {eng(vd_new)}")


def q6(vdd, rg1, rg2, rd, rs, vth, kn):
    ""
    vg = 4

    irg1 = (vdd - vg) / rg1
    print(f"Irg1: {eng(irg1)}")




print("\nQ2:")
q2(2.4, -2.4, 1, 60e-6, 44, 0.4e-3, 0.4)

print("\nQ3:")
q3(1.2, 0.47, 0.35e-3, 5)

print("\nQ4:")
q4(0.6, 0.54, 0.4e-3, 3)

print("\nQ5:")
q5(5.1, 0.08, 0.9, 0.25e-3, 3)

print("\nQ6:")
q6(8, 12e6, 12e6, 7e3, 7e3, 0.9, 0.8e-3)