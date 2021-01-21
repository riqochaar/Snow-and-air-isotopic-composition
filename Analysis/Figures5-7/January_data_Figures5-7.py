# This file was used to compute the relevant average values during January 2017 for Figures 5-7

import pandas as pd
import numpy as np
import joblib
import pickle
import time
from datetime import datetime


D = joblib.load('/home/riqo/mass_flux_files/mass_flux_pickle')

M = joblib.load('/home/riqo/surface_snow_files/surface_snow_isotopic_composition_all')

s = I['time'].index('2017-01-01 00:00:00')

#I_nf = joblib.load('/home/chaar/isotope_antarctica_data/isotope_output_Antarctica_data_2010-2017_nf_pickle_FULL_DATA')

jan = [0+s,745+s]
feb = [745+s,1417+s]
mar = [1417+s,2161+s]
apr = [2161+s,2881+s]
may = [2881+s,3625+s]
jun = [3625+s,4345+s]
jul = [4345+s,5089+s]
aug = [5089+s,5833+s]
sep = [5833+s,6552+s]
ocb = [6552+s,7297+s]
nov = [7297+s,8017+s]
dec = [8017+s,8761+s]

month_start = jan[0]
month_end = jan[1]

M = {}

time = []

for i in range(len(D['time'])):
    time.append(datetime.strptime(D['time'][i], '%Y-%m-%d %H:%M:%S').date())


M['time'] = I['time'][month_start:month_end]

M['latitude'] = I['latitude']
M['longitude'] = I['longitude']

M['mass_snowfall'] = np.mean(D['mass_snowfall'][month_start:month_end, :, :], axis = 0)
M['LE'] = np.mean(D['LE'][month_start:month_end, :, :], axis = 0)
M['t2m'] = np.mean(D['t2m'][month_start:month_end, :, :], axis = 0)
M['skt'] = np.mean(D['skt'][month_start:month_end, :, :], axis = 0)

M['delta_H_snow'] = np.mean(I['delta_H_snow'][month_start:month_end, :, :], axis = 0)
M['delta_O_snow'] = np.mean(I['delta_O_snow'][month_start:month_end, :, :], axis = 0)


PKL_paths_save = '/home/riqo/surface_snow_files/'

file_save = 'average_values_january'

f = open(PKL_paths_save + file_save, "wb")

pickle.dump(M, f)

f.close()



