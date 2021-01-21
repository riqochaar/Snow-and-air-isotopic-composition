# This file was used to calculate the sublimation and evaporation mass fluxes

import numpy as np
import pandas as pd
import math as m
import datetime
import joblib


# file names and path

PKL_path = '/home/riqo/era5_files/'

file = 'era5_data_pickle'

D = joblib.load(PKL_path + file)

lsm = D['lsm']

L_subl = lsm

L_subl = np.where(L_subl==0, 2.26*10**6, L_subl)
L_subl = np.where(L_subl==1, 2.83*10**6, L_subl)

P_triple = 610.5                                        # Triple point pressure (Pa)
T_triple = 273.16                                       # Triple point temperature (K)
R_v = 461.9                                             # Water vapor gas constant (J/kgK)
k = 0.4                                                 # von Karman constant
rho_air = 1.225                                         # Density of air in kg/m3

Z_U = 10                                                # Height of wind speed measurements (m)
Z_T = 2                                                 # Height of temperature measurements (m)
Z_0 = 0.002                                             # Surface roughness (m)
g = 9.81                                                # Accelration due to gravity (m2/s)

D['LE'] = np.empty((len(D['time']), len(D['latitude']),len(D['longitude'])), dtype=np.float32)

for a in range (0,len(D['time'])):

    print(a)

    U_0 = (D['u10'][a]**2 + D['v10'][a]**2)**0.5

    U = np.where(U_0 > 0.1, U_0, 0.1)

    e_surface = P_triple * np.exp((L_subl * (D['skt'][a] - T_triple)) / (R_v * D['skt'][a] * T_triple))
    q_surface = 0.622 * e_surface / (D['sp'][a] - (0.378 * e_surface))

    e_air = np.exp(((1/D['t2m'][a])-(1/D['d2m'][a])) * (L_subl/R_v)) * e_surface
    q_air = 0.622 * e_air / (D['sp'][a] - (0.378 * e_air))

    for b in range (0, len(D['latitude'])):

        for c in range(0, len(D['longitude'])):

            LE_1 = 1
            LE_2 = 100

            psi = 0
            psi_hq = 0

            while abs(((LE_2 - LE_1) / LE_1)) * 100 > 5:

                Denom = np.log(Z_U/Z_0) - psi

                Denom_hq = np.log(Z_T / Z_0) - psi_hq

                LE_1 = rho_air * (k**2) * (U[b,c] * (q_air[b,c] - q_surface[b,c]) / (Denom * Denom_hq))

                SE = (k**2) * (U[b,c] * (D['t2m'][a][b,c] - D['skt'][a][b,c])/ (Denom * Denom_hq))

                u_star = k * U[b,c] / Denom

                OL = -u_star**3 * D['t2m'][a][b,c] / (k * g * SE)

                Z_L = Z_U / OL

                if Z_L > 10:

                    Z_L = 10

                if Z_L < -10:

                    Z_L = -10

                if Z_L < 0:

                    x = (1 - 16 * Z_L) ** (1 / 4)
                    psi = 2 * np.log((1 + x) / 2) + np.log((1 + x ** 2) / 2) - 2 * np.arctan(x) + np.pi / 2
                    psi_hq =  2 * np.log((1 + x ** 2) / 2)

                elif Z_L > 0 and Z_L < 1:

                    psi = -5 * Z_L
                    psi_hq = psi

                else:

                    psi = -5 * (np.log(Z_L) + 1)
                    psi_hq = psi

                LE_2 = rho_air * k ** 2 * (U[b,c] * (q_air[b,c] - q_surface[b,c]) / (Denom * Denom_hq))

            D['LE'][a][b,c] = LE_2

D['LE'] = D['LE'] * 3600

D['mass_snowfall'] = D['sf'] * 997

PKL_path_save = '/home/riqo/mass_flux_files/'

file_save = 'mass_flux_pickle'

f = open(PKL_path_save + file_save, "wb")

joblib.dump(D,f)

f.close()







