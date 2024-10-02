import numpy as np

VT = 25.9e-3

def p6():
    # small signal
    # iD = ID(1 + (vd-v_new)/VT)
    # vd-v_new is v_change
    ID = 0.9e-3
    def ss(v_change):
        i_change = ID * (1 + v_change / VT)
        print(i_change)

    
    # exponential
    # iD = I_S * e ^ (v/VT)
    I_S = 3.5e-15
    def expn(v_change):
        i_change = I_S * np.exp(v_change/VT)
        print(i_change)

    ss(-10e-3)
    expn(-10e-3)
    ss(7e-3)
    expn(7e-3)
    ss(11e-3)
    expn(11e-3)


def p6():
    ID = 0.9e-3
    rd = VT / ID
    # V = iR
    # i = V/R
    for v_change in [-10e-3, 7e-3, 11e-3]:
        # small signal model
        i_change = v_change / rd
        print(i_change)

        # exponential model
        # i = I_S * e ^ (v/vt)
        # I_S = i / (e^(v/vt))
        I_S = ID / np.exp(0.7/VT)
        i_new = I_S * np.exp((0.7 + v_change)/VT
        print(i_new - ID)


def p7():
    # When IL = 0
    ...
    # System of linear equations
    # [1]  ID = (17 - 3) / R
    # [2]  rd = VT / ID
    # [2]  3 = 17*(rd * 4)/ (rd * 4 + R)

    # [2]  rd = 25.9e-3 / (14/R)
    # [2]  rd = 25.9e-3 * R / 14
    # [3]  3 = 17 * ((25.9e-3 * R / 14) * 4) / ((25.9e-3 * R / 14) * 4 + R)
    # [3]  3/17 * ((25.9e-3 * R * 4 / 14) + R) = (25.9e-3 * R * 4 / 14)
    # [3]  0.0013058823 * R + 0.176470588 * R = 0.0074 * R


    # [1]  



p6()
