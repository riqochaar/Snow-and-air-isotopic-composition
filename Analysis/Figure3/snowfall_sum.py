# This file was used to calculate the mass of accumulated snowfall for each location in Antarctica

import pandas as pd
import numpy as np
import joblib
import pandas

D = joblib.load('/home/chaar/mass_flux_files/mass_flux_pickle')

print(D['time'][0])

I = {}

I['snowfall_sum'] = np.empty((len(D['time']), len(D['latitude']), len(D['longitude'])), dtype=np.float32)

for a in range(0, len(D['time'])):

    print(a)

    if a == 0:

        mass_snowfall_sum_previous = D['mass_snowfall'][a]

    else:

        mass_snowfall_sum = mass_snowfall_sum_previous
        mass_snowfall_sum_previous = D['mass_snowfall'][a] + mass_snowfall_sum

    I['snowfall_sum'][a] = mass_snowfall_sum_previous

I['mass_snowfall'] = D['mass_snowfall']

I['summation_of_snowfall'] = I['snowfall_sum'][-1,:,:]

PKL_paths_save = '/home/riqo/surface_snow_files/'

file_save = 'snowfall_summation'

f = open(PKL_paths_save + file_save, "wb")

joblib.dump(I, f)

f.close()
