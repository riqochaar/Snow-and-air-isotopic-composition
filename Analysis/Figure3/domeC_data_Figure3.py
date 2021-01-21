# The file was used to gather relevant data simulated at Dome C for Figure 3

import pandas as pd
import numpy as np
import joblib
import pickle
import time
from datetime import datetime
import random
import scipy.stats

D = joblib.load('/home/riqo/mass_flux_files/mass_flux_pickle')

I = joblib.load('/home/riqo/surface_snow_files/surface_snow_isotopic_composition_all')

I_nf = joblib.load('/home/riqo/surface_snow_files/surface_snow_isotopic_composition_no_fractionation_all')

S = joblib.load('/home/riqo/surface_snow_files/snowfall_summation')

D['latitude'] = D['latitude'].tolist()
D['longitude'] = D['longitude'].tolist()

b_test_index = D['latitude'].index(-75.0)
c_test_index = D['longitude'].index(123.25)

print(I['time'])

print(len(I['time']))
print(len(D['time']))

print(b_test_index)
print(c_test_index)

time = []

for i in range(len(I['time'])):
    time.append(datetime.strptime(D['time'][i], '%Y-%m-%d %H:%M:%S'))

s = I['time'].index('2017-01-01 00:00:00')

print(s) # 4464

print(I['time'][s])

print(I_nf['delta_O_snow'].shape)

jan = np.nanmean(D['t2m'][0+s:745+s,b_test_index,c_test_index])
feb = np.nanmean(D['t2m'][745+s:1417+s,b_test_index,c_test_index])
mar = np.nanmean(D['t2m'][1417+s:2161+s,b_test_index,c_test_index])
apr = np.nanmean(D['t2m'][2161+s:2881+s,b_test_index,c_test_index])
may = np.nanmean(D['t2m'][2881+s:3625+s,b_test_index,c_test_index])
jun = np.nanmean(D['t2m'][3625+s:4345+s,b_test_index,c_test_index])
jul = np.nanmean(D['t2m'][4345+s:5089+s,b_test_index,c_test_index])
aug = np.nanmean(D['t2m'][5089+s:5833+s,b_test_index,c_test_index])
sep = np.nanmean(D['t2m'][5833+s:6553+s,b_test_index,c_test_index])
ocb = np.nanmean(D['t2m'][6553+s:7297+s,b_test_index,c_test_index])
nov = np.nanmean(D['t2m'][7297+s:8017+s,b_test_index,c_test_index])
dec = np.nanmean(D['t2m'][8017+s:8761+s,b_test_index,c_test_index])

time_months = [time[373+s], time[1081+s], time[1789+s], time[2521+s], time[3253+s], time[3985+s], time[4717+s], time[5461+s], time[6193+s], time[6925+s], time[7657+s], time[8389+s]]
months =[jan,feb,mar,apr,may,jun,jul,aug,sep,ocb,nov,dec]

E = np.zeros((6, 8760), dtype=np.float32)


E[0,:] = I['delta_O_snow'][s:,b_test_index,c_test_index]
E[1,:] = I_nf['delta_O_snow'][s:, b_test_index, c_test_index]
E[2,:] = D['LE'][s:,b_test_index,c_test_index]
E[3,:] = S['snowfall_sum'][s:,b_test_index,c_test_index]
E[4,:] = D['t2m'][s:,b_test_index,c_test_index]
E[5,0:12] = months

for x in range(12, 8760):

    if E[5,x] == 0:

        E[5,x] = np.nan


PKL_paths_save = '/home/riqo/surface_snow_files/'

file_save = 'domeC_data_Figure3'

f = open(PKL_paths_save + file_save, "wb")

joblib.dump(E, f, compress = 9)

f.close()





