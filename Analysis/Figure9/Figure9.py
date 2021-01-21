# This file was used to produce Figure 9

import joblib
import numpy as np
import pandas as pd
import xarray as xr
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as md
import xlsxwriter


M = pd.read_csv('/home/riqo/air_parcel_files/observed_composition_at_ship.csv') # Observations from ship

N = M[1604:1795]

ave_O = M.interpolate()['d18O'].mean()
ave_H = M.interpolate()['d2H'].mean()
ave_dexc = M.interpolate()['dexc'].mean()

O = N.interpolate()

S = O['d18O']
Q = O['d2H']
R = O['dexc']

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

hour_index = 172
traj = xr.open_dataset(data_path + files[hour_index])
P = np.flip(traj['P'].values, axis=0)

D = joblib.load('/home/riqo/air_parcel_files/air_parcel_calculation_output')
D1 = joblib.load('/home/riqo/air_parcel_files/air_parcel_calculation_output_no_fractionation')

height_indicator = []

for b in range(0,78):

    if P[-1,b] >=700 and P[-1,b] <= 1000:

        height_indicator.append(b)

D['delta_H_air_included'] = np.empty((192, 169, len(height_indicator)), dtype=np.float32)
D['delta_H_air_included_nf'] = np.empty((192, 169, len(height_indicator)), dtype=np.float32)
D['delta_H_snow_included'] = np.empty((192, 169, len(height_indicator)), dtype=np.float32)

D['delta_O_air_included'] = np.empty((192, 169, len(height_indicator)), dtype=np.float32)
D['delta_O_air_included_nf'] = np.empty((192, 169, len(height_indicator)), dtype=np.float32)
D['delta_O_snow_included'] = np.empty((192, 169, len(height_indicator)), dtype=np.float32)

D['LE_included'] = np.empty((192, 169, len(height_indicator)), dtype=np.float32)

for a in range(0, 192):

    for b in range(0, 169):

        for x in range(0, len(height_indicator)):

            D['delta_H_air_included'][a,b,x] = D['delta_H_air'][a,b,height_indicator[x]]
            D['delta_H_air_included_nf'][a,b,x] = D1['delta_H_air'][a,b,height_indicator[x]]
            D['delta_H_snow_included'][a,b,x] = D['delta_H_subl'][a,b,height_indicator[x]]

            D['delta_O_air_included'][a,b,x] = D['delta_O_air'][a,b,height_indicator[x]]
            D['delta_O_air_included_nf'][a,b,x] = D1['delta_O_air'][a,b,height_indicator[x]]
            D['delta_O_snow_included'][a,b,x] = D['delta_O_subl'][a,b,height_indicator[x]]

            D['LE_included'][a,b,x] = D['LE_trajectory'][a,b,height_indicator[x]]

path_indicator = np.empty((191, len(height_indicator)), dtype=np.float32)

path_indicator_mean_list = []
LE_indicator_mean_list = []
delta_snow_indicator_mean_list = []

for z in range(0,191):

    for b in range(0,len(height_indicator)):

        path_indicator[z,b] = np.count_nonzero(D['delta_O_snow_included'][z,:,b]==0)

    path_indicator_mean_list.append(np.mean(path_indicator[z,:])) # represents the average timesteps the air trajectories are over water for each of the group of trajectories ending at the position of the ship
    LE_indicator_mean_list.append(np.mean(D['LE_included'][z,:,:])*-1) # represents the average LE the air trajectories experiance for each of the group of trajectories ending at the position of the ship
    delta_snow_indicator_mean_list.append(np.mean(D['delta_O_snow_included'][z,:,:]))

time_index = D['time_192'].index('2017-02-01 07:00:00')

delta_H_ship = []
delta_H_ship_nf = []

delta_O_ship = []
delta_O_ship_nf = []

for a in range(0, 191):

    delta_H_ship.append(np.mean(D['delta_H_air_included'][a,-2,:]))
    delta_H_ship_nf.append(np.mean(D['delta_H_air_included_nf'][a,-2,:]))

    delta_O_ship.append(np.mean(D['delta_O_air_included'][a,-2,:]))
    delta_O_ship_nf.append(np.mean(D['delta_O_air_included_nf'][a,-2,:]))


time = []

for i in range(len(D['time_192'])-1):
    time.append(datetime.strptime(D['time_192'][i], '%Y-%m-%d %H:%M:%S'))

eight = [i * 8 for i in delta_O_ship]

d_excess = [a_i - b_i for a_i, b_i in zip(delta_H_ship, eight)]

fig, [ax1, ax2] = plt.subplots(nrows = 2, ncols = 1)

fig.set_figheight(8)
fig.set_figwidth(10)

time = time
#time = list(range(0,191))

def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

ax2.plot(time, delta_H_ship, color='k', label = 'modelled (with fractionation)', zorder = 100)
ax2.plot(time, delta_H_ship_nf, color='b', label = 'modelled (without fractionation)', zorder = 0)
ax2.plot(time, Q, color ='g', label = 'observed', zorder = 10)


ax2.set_xlabel('Day', size = 14)
ax2.set_ylabel('Average \u03B4D of water vapour\nat ship position (\u2030 vs VSMOW)', size=14)

days = md.DayLocator()
format_2 = md.DateFormatter('\n%d')

ax2.xaxis.set_major_locator(days)
ax2.xaxis.set_major_formatter(format_2)



ax1.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)

ax1.plot(time, delta_O_ship, color='k', label = 'modelled (with fractionation)', zorder = 100)
ax1.plot(time, delta_O_ship_nf, color='b', label = 'modelled (without fractionation)', zorder = 0)
ax1.plot(time, S, color ='g', label = 'observed', zorder = 10)

ax1.set_xlabel('Day', size=14)
ax1.set_ylabel('Average \u03B4$^{18}$O of water vapour\nat ship position (\u2030 vs VSMOW)', size=14)

ax1.xaxis.set_major_locator(days)
ax1.xaxis.set_major_formatter(format_2)

ax1.axvline(x='2017-01-28 01:00:00', color='grey', linestyle='dashed') #49
ax1.axvline(x='2017-01-29 18:00:00', color='grey', linestyle='dashed') #90
ax1.axvline(x='2017-01-30 12:00:00', color='grey', linestyle='dashed') #108
ax1.axvline(x='2017-02-02 01:00:00', color='grey', linestyle='dashed') #169

ax2.axvline(x='2017-01-28 01:00:00', color='grey', linestyle='dashed') #49
ax2.axvline(x='2017-01-29 18:00:00', color='grey', linestyle='dashed') #90
ax2.axvline(x='2017-01-30 12:00:00', color='grey', linestyle='dashed') #108
ax2.axvline(x='2017-02-02 01:00:00', color='grey', linestyle='dashed') #169

fig.subplots_adjust(hspace=0.4)

plt.tight_layout()

Figures_paths = '/home/riqo/Figures/'

plt.savefig(Figures_paths + 'Figure9', bbox_inches='tight', pad_inches=0)

plt.show()