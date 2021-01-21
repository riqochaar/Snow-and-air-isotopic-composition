# ERA 5 data comes as a .netcdf file

# This file was used to convert data from .netcdf to pickle format so it could be utilised in the model

import numpy as np
import netCDF4
from netCDF4 import Dataset
from datetime import datetime, timedelta
import os
from pathlib import Path
import ExtractingData as mrr
import joblib
from datetime import datetime, timedelta

data_path = Path('/home/riqo/era5_files/')

# create variables

D = {}

D_1D = {}

Time = []

# files to be read

file_list = sorted(os.listdir(data_path))

for file in file_list:

    file_path = data_path / file

    (D_i, D_1D_i) = mrr.extract_mrr_var(file_path, var_name=['u10', 'v10', 'd2m', 't2m', 'lsm', 'skt', 'sf', 'sp'], var_name_1D = ['longitude', 'latitude', 'time'])

    for r in D_i:

        if file == file_list[0]:

            Shape = np.asarray(D_i[r].shape)
            Shape[0] = 0
            D[r] = np.empty(Shape, dtype=np.float32)

        D[r] = np.vstack((D[r], D_i[r]))

    if file == file_list[0]:

        D_1D['time'] = np.empty(0, dtype=np.float32)

    D_1D['time'] = np.append(D_1D['time'], D_1D_i['time'], axis = 0)

    print(file)

for h in range(0, len(D_1D['time'])):

    hours = D_1D['time'][h]

    start = datetime(1900, 1, 1, 0)  # This is the "days since" part

    delta = timedelta(hours=hours.item())  # Create a time delta object from the number of days

    offset = start + delta

    Date = offset.strftime('%Y-%m-%d %H:%M:%S')

    Time.append(Date)

    print(h)

D['longitude'] = D_1D_i['longitude']
D['latitude'] = D_1D_i['latitude']
D['time'] = Time

PKL_path = '/home/riqo/era5_files/'

f = open(PKL_path + 'era5_data_pickle', "wb")

joblib.dump(D,f)

f.close()

