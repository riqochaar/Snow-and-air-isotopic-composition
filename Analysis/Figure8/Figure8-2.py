# This file was used to produce the Figure 8 trajectory plot

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
from mpl_toolkits import basemap as bm
from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np
import pandas as pd
import numpy.ma as ma
import joblib
import random
import xarray as xr

data_path = '/home/riqo/air_parcel_trajectories/'

files = ['lsl_20170126_00', 'lsl_20170126_01', 'lsl_20170126_02', 'lsl_20170126_03', 'lsl_20170126_04', 'lsl_20170126_05',
         'lsl_20170126_06', 'lsl_20170126_07', 'lsl_20170126_08', 'lsl_20170126_09', 'lsl_20170126_10', 'lsl_20170126_11',
         'lsl_20170126_12', 'lsl_20170126_13', 'lsl_20170126_14', 'lsl_20170126_15', 'lsl_20170126_16', 'lsl_20170126_17',
         'lsl_20170126_18', 'lsl_20170126_19', 'lsl_20170126_20', 'lsl_20170126_21', 'lsl_20170126_22', 'lsl_20170126_23',
         'lsl_20170127_00', 'lsl_20170127_01', 'lsl_20170127_02', 'lsl_20170127_03', 'lsl_20170127_04', 'lsl_20170127_05',
         'lsl_20170127_06', 'lsl_20170127_07', 'lsl_20170127_08', 'lsl_20170127_09', 'lsl_20170127_10', 'lsl_20170127_11',
         'lsl_20170127_12', 'lsl_20170127_13', 'lsl_20170127_14', 'lsl_20170127_15', 'lsl_20170127_16', 'lsl_20170127_17',
         'lsl_20170127_18', 'lsl_20170127_19', 'lsl_20170127_20', 'lsl_20170127_21', 'lsl_20170127_22', 'lsl_20170127_23',
         'lsl_20170128_00', 'lsl_20170128_01', 'lsl_20170128_02', 'lsl_20170128_03', 'lsl_20170128_04', 'lsl_20170128_05',
         'lsl_20170128_06', 'lsl_20170128_07', 'lsl_20170128_08', 'lsl_20170128_09', 'lsl_20170128_10', 'lsl_20170128_11',
         'lsl_20170128_12', 'lsl_20170128_13', 'lsl_20170128_14', 'lsl_20170128_15', 'lsl_20170128_16', 'lsl_20170128_17',
         'lsl_20170128_18', 'lsl_20170128_19', 'lsl_20170128_20', 'lsl_20170128_21', 'lsl_20170128_22', 'lsl_20170128_23',
         'lsl_20170129_00', 'lsl_20170129_01', 'lsl_20170129_02', 'lsl_20170129_03', 'lsl_20170129_04', 'lsl_20170129_05',
         'lsl_20170129_06', 'lsl_20170129_07', 'lsl_20170129_08', 'lsl_20170129_09', 'lsl_20170129_10', 'lsl_20170129_11',
         'lsl_20170129_12', 'lsl_20170129_13', 'lsl_20170129_14', 'lsl_20170129_15', 'lsl_20170129_16', 'lsl_20170129_17',
         'lsl_20170129_18', 'lsl_20170129_19', 'lsl_20170129_20', 'lsl_20170129_21', 'lsl_20170129_22', 'lsl_20170129_23',
         'lsl_20170130_00', 'lsl_20170130_01', 'lsl_20170130_02', 'lsl_20170130_03', 'lsl_20170130_04', 'lsl_20170130_05',
         'lsl_20170130_06', 'lsl_20170130_07', 'lsl_20170130_08', 'lsl_20170130_09', 'lsl_20170130_10', 'lsl_20170130_11',
         'lsl_20170130_12', 'lsl_20170130_13', 'lsl_20170130_14', 'lsl_20170130_15', 'lsl_20170130_16', 'lsl_20170130_17',
         'lsl_20170130_18', 'lsl_20170130_19', 'lsl_20170130_20', 'lsl_20170130_21', 'lsl_20170130_22', 'lsl_20170130_23',
         'lsl_20170131_00', 'lsl_20170131_01', 'lsl_20170131_02', 'lsl_20170131_03', 'lsl_20170131_04', 'lsl_20170131_05',
         'lsl_20170131_06', 'lsl_20170131_07', 'lsl_20170131_08', 'lsl_20170131_09', 'lsl_20170131_10', 'lsl_20170131_11',
         'lsl_20170131_12', 'lsl_20170131_13', 'lsl_20170131_14', 'lsl_20170131_15', 'lsl_20170131_16', 'lsl_20170131_17',
         'lsl_20170131_18', 'lsl_20170131_19', 'lsl_20170131_20', 'lsl_20170131_21', 'lsl_20170131_22', 'lsl_20170131_23',
         'lsl_20170201_00', 'lsl_20170201_01', 'lsl_20170201_02', 'lsl_20170201_03', 'lsl_20170201_04', 'lsl_20170201_05',
         'lsl_20170201_06', 'lsl_20170201_07', 'lsl_20170201_08', 'lsl_20170201_09', 'lsl_20170201_10', 'lsl_20170201_11',
         'lsl_20170201_12', 'lsl_20170201_13', 'lsl_20170201_14', 'lsl_20170201_15', 'lsl_20170201_16', 'lsl_20170201_17',
         'lsl_20170201_18', 'lsl_20170201_19', 'lsl_20170201_20', 'lsl_20170201_21', 'lsl_20170201_22', 'lsl_20170201_23',
         'lsl_20170202_00', 'lsl_20170202_01', 'lsl_20170202_02', 'lsl_20170202_03', 'lsl_20170202_04', 'lsl_20170202_05',
         'lsl_20170202_06', 'lsl_20170202_07', 'lsl_20170202_08', 'lsl_20170202_09', 'lsl_20170202_10', 'lsl_20170202_11',
         'lsl_20170202_12', 'lsl_20170202_13', 'lsl_20170202_14', 'lsl_20170202_15', 'lsl_20170202_16', 'lsl_20170202_17',
         'lsl_20170202_18', 'lsl_20170202_19', 'lsl_20170202_20', 'lsl_20170202_21', 'lsl_20170202_22', 'lsl_20170202_23']

D = joblib.load('/home/riqo/air_parcel_files/air_parcel_calculation_output')

hour_index = 88
b_test = 9

min = np.nanmin(D['delta_O_air'][hour_index,0:168,:])
max = np.nanmax(D['delta_O_air'][hour_index,0:168,:])

for a in range(0, 169):

    for b in range(0, 78):

        if D['longitude_trajectory'][hour_index,a,b] == -180.0:

            D['longitude_trajectory'][hour_index,a,b] = 180.0

traj = xr.open_dataset(data_path + files[hour_index])

P = np.flip(traj['P'].values, axis=0)

latitude_trajectory = D['latitude_trajectory'][hour_index,:,:]
longitude_trajectory = D['longitude_trajectory'][hour_index,:,:]
delta_O_snow_trajectory = D['delta_O_snow_trajectory'][hour_index,:,:]

E = {}

fig, ax = plt.subplots(figsize=(5,5))

E['delta_O_air_graph'] = np.empty((78, len(D['latitude']), len(D['longitude'])), dtype=np.float32)

##some fake data
lat = D['latitude'][:]
lon = np.hstack((D['longitude'], D['longitude'][:1]))
lon, lat = np.meshgrid(lon, lat)

height_indicator = []

for a in range(0, len(D['time'])-1):

    print(a)

    for b in range(b_test, b_test+1):

        lat_index = D['latitude'].index(latitude_trajectory[a,b])

        lon_index = D['longitude'].index(longitude_trajectory[a, b])

        E['delta_O_air_graph'][b,lat_index,lon_index] = D['delta_O_air'][hour_index,a,b]

E['delta_O_air_graph'][E['delta_O_air_graph']==0]=np.nan

def myround(x, prec=2, base=0.25):
    return round(base * round(float(x) / base), prec)

ship_position_lon = myround(np.mean(D['longitude_trajectory'][hour_index,-2,:]))
ship_position_lat = myround(np.mean(D['latitude_trajectory'][hour_index,-2,:]))

delta_O_air_0 = E['delta_O_air_graph'][b_test,:,:]

m = bm.Basemap(projection='spstere',boundinglat=-65,lon_0=180,resolution='l')
m.drawcoastlines(linewidth=0.5)

x,y = m(lon,lat)

a,b = m(ship_position_lon, ship_position_lat)

min_test = np.nanmin(delta_O_air_0)
max_test = np.nanmax(delta_O_air_0)

vmin_ = -45

vmax_ = -20

pcol_0 = ax.pcolormesh(x, y, delta_O_air_0, cmap='viridis', vmin = vmin_, vmax = vmax_)

ship = m.scatter(a, b, marker = 'o', color='r', zorder=5)

ax = plt.gca()
im = ax.imshow(delta_O_air_0)

divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)

x = plt.colorbar(im, cax=cax)

x.set_label(label='Modelled \u03B4$^{18}$O of water vapour\naccounting for fractionation\n(\u2030 vs VSMOW)', size='16')

Figures_paths = '/home/riqo/Figures/'

plt.savefig(Figures_paths + 'Figure8-2', bbox_inches='tight', pad_inches=0)

plt.show()