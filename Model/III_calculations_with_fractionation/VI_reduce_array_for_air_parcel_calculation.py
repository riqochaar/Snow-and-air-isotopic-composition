# This file was used to reduce the surface snow array produced in 'V_surface_snow_files_merge.py'
# to only include time periods relevant for the air parcel analysis

# The output of this file was used as the input for 'VII_air_parcel_calculation.py'

import numpy as np
import pickle
import pandas as pd
import joblib


D = joblib.load('/home/riqo/mass_flux_files/mass_flux_pickle')

M = joblib.load('/home/riqo/surface_snow_files/surface_snow_isotopic_composition_all')

start_time_index_starting_delta = D['time'].index('2017-01-01 00:00:00')
start_time_index = D['time'].index('2017-01-19 00:00:00')
end_time_index = D['time'].index('2017-02-03 01:00:00')

# Cut array

C = {}

C['time_starting_delta'] = D['time'][start_time_index_starting_delta:end_time_index]
C['time'] = D['time'][start_time_index:end_time_index]
C['latitude'] = D['latitude']
C['longitude'] = D['longitude']

C['LE'] = D['LE'][start_time_index:end_time_index,:,:]

C['skt_starting_delta'] = D['skt'][start_time_index_starting_delta:end_time_index,:,:]
C['skt'] = D['skt'][start_time_index:end_time_index,:,:]
C['t2m'] = D['t2m'][start_time_index:end_time_index,:,:]
C['d2m'] = D['d2m'][start_time_index:end_time_index,:,:]
C['sp'] = D['sp'][start_time_index:end_time_index,:,:]

C['delta_H_snow_starting_delta'] = M['delta_H_snow'][start_time_index_starting_delta:end_time_index,:,:]
C['delta_O_snow_starting_delta'] = M['delta_O_snow'][start_time_index_starting_delta:end_time_index,:,:]
C['delta_H_snow'] = M['delta_H_snow'][start_time_index:end_time_index,:,:]
C['delta_O_snow'] = M['delta_O_snow'][start_time_index:end_time_index,:,:]

C['q_air'] = np.empty((len(C['time']), len(C['latitude']), len(C['longitude'])), dtype=np.float32)

P_triple = 610.5                                        # Triple point pressure (Pa)
T_triple = 273.16                                       # Triple point temperature (K)
R_v = 461.9                                             # Water vapor gas constant (J/kgK)

for a in range(0, len(C['time'])):
  
    print(a)

    L_subl = (2834.1 - (0.29 * (C['t2m'][a] - 273.15)) - (0.004 * (C['t2m'][a] - 273.15) ** 2)) * 1000

    e_surface = P_triple * np.exp((L_subl * (C['skt'][a] - T_triple)) / (R_v * C['skt'][a] * T_triple))
    q_surface = 0.622 * e_surface / (C['sp'][a] - (0.378 * e_surface))

    e_air = np.exp(((1 / C['t2m'][a]) - (1 / C['d2m'][a])) * (L_subl / R_v)) * e_surface
    q_air = 0.622 * e_air / (C['sp'][a] - (0.378 * e_air))

    C['q_air'][a] = q_air

PKL_paths_save = '/home/riqo/air_parcel_files/'

file_save = 'air_parcel_calculation_input'

f = open(PKL_paths_save + file_save, "wb")

joblib.dump(C, f)

f.close()

