import numpy as np

def p1():
    Na = 1.2e18 # 1/cm3
    Nd = 1.2e16 # 1/cm3
    A  = 0.0001 # cm2
    ni = 15e9   # 1/cm3
    Lp = 5      # um
    Ln = 8      # um
    Dp = 12     # cm2 / (V*s)
    Dn = 16     # cm2 / (V*s)
    Vf = 0.6    # V

    # A q ni2 (Dp / (LpNd) + Dn / (LnNa))
    
    # Get everything to the right units (meters and such)
    Na_ = Na * 1e6 # 1/m3
    Nd_ = Na * 1e6 # 1/m3
    A_  = A  / 1e4 # m2
    ni_ = ni * 1e6 # 1/m3
    Lp_ = Lp / 1e6 # m
    Ln_ = Ln / 1e6 # m
    Dp_ = Dp / 1e4 # m2 / (V*s)
    Dn_ = Dn / 1e4 # m2 / (V*s)
    Vf_ = Vf       # V

    q = 1.6e-19
    V_th = 25.9e-3

    I_s = A_ * q * (ni_ * ni_) * (Dp_ / (Lp_ * Nd_) + Dn_ / (Ln_ * Na_))
    print("I_s:", I_s)
    I = I_s * (np.exp(Vf_ / V_th) - 1)
    print("I:", I)
    tau_p = (Ln_ * Ln_) / Dn_
    print("tau_p:", tau_p)



def main():
    p1()


if __name__ == "__main__":
    main()
