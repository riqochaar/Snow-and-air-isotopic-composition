# This file was used to produce the Figure 8 time series

import numpy as np
import joblib
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as md

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
D1 = joblib.load('/home/riqo/air_parcel_files/air_parcel_calculation_output_no_fractionation')

H_VSMOW = 155.95 * (10 ** (-6))  # VSMOW hydrogen isotopic ratio
O_VSMOW = 2005.20 * (10 ** (-6))  # VSMOW oxygen isotopic ratio

S = joblib.load('/home/riqo/mass_flux_files/mass_flux_pickle')

time_array = S['time']

fig, ax1 = plt.subplots(nrows=1, ncols=1, figsize=(10,5))

z_test = 88
a_test = len(D['time']) - 2
b_test = 9

traj = xr.open_dataset(data_path + files[z_test])

P = np.flip(traj['P'].values, axis=0)

air_W = 1                           # air area width (m)
air_L = 1                           # air area length (m)
air_D = 1000                        # air depth (m)
air_A = air_W * air_L               # air area (m2)
air_V = air_W * air_L * air_D       # air volume (m3)
air_rho = 1.225                     # air density (kg/m3)
air_mass_start = air_V * air_rho    # air mass (kg)

q_difference = D['q_air_trajectory_start'] - D['q_air_trajectory_end']

water_vapour_difference = q_difference * air_mass_start / (1 - q_difference)

time_end = '2017-01-29 16:00:00' # = time_at_z_test - 1 hour
time_start = '2017-01-22 16:00:00' # 7 days before

time_index = range(time_array.index(time_start), time_array.index(time_end))

time_list = time_array[time_index[0]:time_index[-1]]

time = []

for i in range(len(time_list)):
    time.append(datetime.strptime(time_list[i], '%Y-%m-%d %H:%M:%S'))

def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

fig.subplots_adjust(right=0.75)

p1_color = 'k'
p2_color = 'blue'
p3_color = 'purple'
p4_color = 'darkgreen'

p10_color = 'r'
p11_color = 'g'

ax2 = ax1.twinx()

D1['delta_O_air'][z_test,:a_test,b_test][0] = D['delta_O_air'][z_test,:a_test,b_test][0]

p1 = ax1.plot(time[:-1], D['delta_O_air'][z_test,:a_test,b_test][:-1], color=p1_color, label = 'air parcel (with fractionation)', linestyle = '-')
p2 = ax1.plot(time[:-1], D1['delta_O_air'][z_test,:a_test,b_test][:-1], color=p2_color, label = 'air parcel (without fractionation)', linestyle = '-')
p4 = ax1.plot(time[:-1], D['delta_O_subl'][z_test,:a_test,b_test][:-1], color=p1_color, label = 'surface water vapour mass flux (with fractionation)', linestyle = '--')
p4 = ax1.plot(time[:-1], D['delta_O_snow_trajectory'][z_test,:a_test,b_test][:-1], color=p2_color, label = 'surface water vapour mass flux (without fractionation)', linestyle = '--')
p5 = ax2.plot(time[:-1], D['LE_trajectory'][z_test,:a_test,b_test][:-1]*-1, color=p3_color, linestyle = '-')

ax1.set_xlabel('Day', size=16)
ax1.set_ylabel('\u03B4$^{18}O$ (\u2030 vs VSMOW)', size=16)
ax2.set_ylabel('Surface water vapour\nmass flux (kg/m$^2$h)', size=16, color=p3_color)


tkw = dict(size=4, width=1.5)
ax1.tick_params(axis='x', **tkw)

days = md.DayLocator()
format_2 = md.DateFormatter('\n%d')

ax1.xaxis.set_major_locator(days)
ax1.xaxis.set_major_formatter(format_2)

ax1.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)

plt.tight_layout()

Figures_paths = '/home/riqo/Figures/'

plt.savefig(Figures_paths + 'Figure8-1', bbox_inches='tight', pad_inches=0)

plt.show()