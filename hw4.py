import numpy as np
import decimal


def main():
    q4()

def q1():
    N_A = 9.0E+17  # Acceptor concentration Na [1/cm^3]
    N_A_m = 9.0E+17 * 100 * 100 * 100  # Acceptor concentration Na [1/cm^3]
    N_D = 8.0E+15  # Donor concentration Nd [1/cm^3]
    N_D_m = 8.0E+15 * 100 * 100 * 100  # Donor concentration Nd [1/cm^3]
    A = 0.0001  # Cross-sectional area [cm^2]
    A_m = A / 100 / 100
    ni = 15000000000  # Intrinsic carrier concentration [1/cm^3]
    ni_m = ni * 100 * 100 * 100
    L_p = 4.9  # Hole diffusion length [µm]
    L_p_m = 4.9 * 1E-6
    L_n = 8  # Electron diffusion length [µm]
    L_n_m = 8 * 1E-6  # Electron diffusion length [µm]
    D_p = 11  # Hole Diffusivity [cm^2/(V*s)]
    D_p_m = 11 / 100 / 100  # Hole Diffusivity [m^2/(V*s)]
    D_n = 17  # Electron Diffusivity [cm^2/(V*s)]
    D_n_m = 17 / 100 / 100  # Electron Diffusivity [m^2/(V*s)]
    v = 0.61  # Forward Voltage [V)]

    q = 1.6022E-19 # Charge of an electron [coulomb]
    k = 8.62E-5  # Boltzmann's constant

    # Is = A * q * ni^2 * (D_p/(L_p * N_D) + D_n/(L_n * N_A))
    Is = A * q * ni**2 * (D_p/(L_p * N_D) + D_n/(L_n * N_A))
    Is = A_m * q * ni_m**2 * (D_p_m/(L_p_m * N_D_m) + D_n_m/(L_n_m * N_A_m))
    Is_eng = decimal.Decimal(Is)
    Is_eng = Is_eng.normalize().to_eng_string()
    print(f"Is is: {Is_eng}")

    # I = Ip + In
    # Ip = A * q * ni^2 * D_p/(L_p * N_D) * (e^(v/v_t) - 1) 
    # In = A * q * ni^2 * D_n/(L_n * N_A) * (e^(v/v_t) - 1) 
    # V_t = kT/q
    v_t = k*300/q
    v_t = 25.85E-3
    # print(v_t)
    Ip = A * q * ni**2 * D_p/(L_p * N_D) * (np.e**(v/v_t) - 1)
    Ip = A_m * q * ni_m**2 * D_p_m/(L_p_m * N_D_m) * (np.e**(v/v_t) - 1)
    In = A * q * ni**2 * D_n/(L_n * N_A) * (np.e**(v/v_t) - 1)
    In = A_m * q * ni_m**2 * D_n_m/(L_n_m * N_A_m) * (np.e**(v/v_t) - 1)
    I = Ip + In
    I_eng = decimal.Decimal(I) 
    I_eng = I_eng.normalize().to_eng_string()
    print(f"I is: {I_eng}")

    # tau_p = L_p^2 / D_p
    tau_p = L_p_m**2 / D_p_m
    tau_eng = decimal.Decimal(tau_p)
    tau_eng = tau_eng.normalize().to_eng_string()
    print(f"Tau_p is: {tau_eng}")

    # Cd = Tau_p / V_t * I
    Cd = tau_p / v_t * I
    Cd_eng = decimal.Decimal(Cd)
    Cd_eng = Cd_eng.normalize().to_eng_string()
    print(f"Cd is: {Cd_eng}")

def q2():
    # np0 = ni^2/Na
    B = 7.3E15
    T = 300
    Eg = 1.12
    k = 8.62E-5
    ni = B*T**(3/2) * np.e**(-Eg/(2*k*T))

    Na = 1.1E18
    # ni_eng = decimal.Decimal(ni)
    # ni_eng = ni_eng.normalize().to_eng_string()
    np0 = ni**2 / Na
    print(f"Np is: {np0}")

    Nd = 8.0E15
    pn0 = ni**2 / Nd
    print(f"Pn is: {pn0}")

    # Built-in voltage
    v_t = 25.85e-3
    V0 = v_t * np.log(Na * Nd / (ni**2))
    print(f"V0 is: {V0}")

def q3():
    I = 0.0009 # Forward current at given voltage [A]
    v = 0.61  # Applied Voltage [V]
    Nd = 1.3E+16  # Donor concentration Nd [1/cm^3]
    Nd_m = Nd * 100 * 100 * 100
    A = 0.0001  # Cross-sectional area [cm^2]
    A_m = A / 100 / 100
    ni = 15000000000  # Intrinsic carrier concentration [1/cm^3]
    ni_m = ni * 100 * 100 * 100
    L_n = 4.9  # Hole diffusion length [µm]
    L_n_m = L_n * 1E-6
    L_p = 11  # Electron diffusion length [µm]
    L_p_m = L_p * 1E-6
    D_p = 9  # Hole Diffusivity [cm^2/(V*s)]
    D_p_m = D_p / 100 / 100
    D_n = 19  # Electron Diffusivity [cm^2/(V*s)]
    D_n_m = D_n / 100 / 100

    v_t = 25.85e-3
    q = 1.6022E-19
    # I = IS(e^(V/VT) - 1)
    # 1 / Is = 1/I * (e^(v/vt) - 1)
    # Is = 1 / (1/I * (e^(v/vt) - 1))
    Is = 1 / ((1/I) * (np.e**(v/v_t) - 1))
    print(f"Is is: {decimal.Decimal(Is).normalize().to_eng_string()}")

    Na_m = D_n_m / (L_n_m * (Is / (A_m * q * ni_m **2) - D_p_m / (L_p_m * Nd_m)))
    Na = D_n / (L_n * (Is / (A * q * ni **2) - D_p / (L_p * Nd)))
    Na_cm = Na_m / 100 / 100 / 100
    print(f"Na is: {decimal.Decimal(Na_cm).normalize().to_eng_string()}")
    print(f"Na is: {Na_cm:4e}")
    print(f"Na is: {Na:4e}")

def q4():
    Na = 1.2E+18  # Acceptor concentration Na [1/cm^3]
    Nd = 1.0E+16  # Donor concentration Nd [1/cm^3]
    A = 8.0E-5  # Cross-sectional area [cm^2]
    ni = 15000000000  # Intrinsic carrier concentration [1/cm^3]
    L_p = 5  # Hole diffusion length [µm]
    L_n = 10  # Electron diffusion length [µm]
    D_p = 9  # Hole Diffusivity [cm^2/(V*s)]
    D_n = 16  # Electron Diffusivity [cm^2/(V*s)]
    v_r = -1.9  # Reverse Voltage [V)]
    v_t = 25.85E-3
    V0 = v_t * np.log(Na * Nd / (ni**2))
    print(V0)
    v0 = 0

    q = 1.6022E-19

    eps = 11.7 * 8.854E-14
    W = np.sqrt(2* eps/q * (1/Na + 1/Nd) * (V0 - v_r))
    print(f"W is: {W}")


if __name__ == '__main__':
    main()