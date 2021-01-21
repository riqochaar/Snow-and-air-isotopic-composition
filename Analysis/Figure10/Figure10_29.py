# This file was used to produce the Figure 10 plot for 18:00, 29th January

# All Figure 10 files were compiled after being produced separately

from mpl_toolkits import basemap as bm
from matplotlib import pyplot as plt
import numpy as np
import joblib
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

hour_index = 90

traj = xr.open_dataset(data_path + files[hour_index])
P = np.flip(traj['P'].values, axis=0)

latitude_trajectory = D['latitude_trajectory'][hour_index,:,:]
longitude_trajectory = D['longitude_trajectory'][hour_index,:,:]

E = {}

fig, ax = plt.subplots(figsize=(3,3))

height_indicator = []

for b in range(0,78):

    if P[-1,b] >=700 and P[-1,b] <= 1000:

        height_indicator.append(b)

E['delta_O_air_graph'] = np.empty((len(height_indicator), len(D['latitude']), len(D['longitude'])), dtype=np.float32)

lat = D['latitude'][:]
lon = np.hstack((D['longitude'], D['longitude'][:1]))
lon, lat = np.meshgrid(lon, lat)

D['delta_H_air_included'] = np.empty((192, 169, len(height_indicator)), dtype=np.float32)

D['delta_O_air_included'] = np.empty((192, 169, len(height_indicator)), dtype=np.float32)

for a in range(0, 192):

    for b in range(0, 169):

        for x in range(0, len(height_indicator)):

            D['delta_H_air_included'][a,b,x] = D['delta_H_air'][a,b,height_indicator[x]]

            D['delta_O_air_included'][a,b,x] = D['delta_O_air'][a,b,height_indicator[x]]

for a in range(0, len(D['time'])-1):

    print(a)

    for b in range(0, len(height_indicator)):

        lat_index = D['latitude'].index(latitude_trajectory[a,b])

        lon_index = D['longitude'].index(longitude_trajectory[a, b])

        E['delta_O_air_graph'][b,lat_index,lon_index] = D['delta_O_air'][hour_index,a,b]

E['delta_O_air_graph'][E['delta_O_air_graph']==0]=np.nan

min = np.nanmin(E['delta_O_air_graph'][:,:,:])
max = np.nanmax(E['delta_O_air_graph'][:,:,:][np.nonzero(E['delta_O_air_graph'][:,:,:])])

def myround(x, prec=2, base=0.25):
    return round(base * round(float(x) / base), prec)

ship_position_lon = myround(np.mean(D['longitude_trajectory'][hour_index,-2,:]))
ship_position_lat = myround(np.mean(D['latitude_trajectory'][hour_index,-2,:]))

m = bm.Basemap(projection='spstere',boundinglat=-65,lon_0=180,resolution='l')
m.drawcoastlines(linewidth=0.5)

x,y = m(lon,lat)

a,b = m(ship_position_lon, ship_position_lat)

vmin = -60

vmax = -10

pcol_0 = ax.pcolormesh(x, y, E['delta_O_air_graph'][0, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_1 = ax.pcolormesh(x, y, E['delta_O_air_graph'][1, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_2 = ax.pcolormesh(x, y, E['delta_O_air_graph'][2, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_3 = ax.pcolormesh(x, y, E['delta_O_air_graph'][3, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_4 = ax.pcolormesh(x, y, E['delta_O_air_graph'][4, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_5 = ax.pcolormesh(x, y, E['delta_O_air_graph'][5, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_6 = ax.pcolormesh(x, y, E['delta_O_air_graph'][6, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_7 = ax.pcolormesh(x, y, E['delta_O_air_graph'][7, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_8 = ax.pcolormesh(x, y, E['delta_O_air_graph'][8, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_9 = ax.pcolormesh(x, y, E['delta_O_air_graph'][9, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_10 = ax.pcolormesh(x, y, E['delta_O_air_graph'][10, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_11 = ax.pcolormesh(x, y, E['delta_O_air_graph'][11, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_12 = ax.pcolormesh(x, y, E['delta_O_air_graph'][12, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_13 = ax.pcolormesh(x, y, E['delta_O_air_graph'][13, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_14 = ax.pcolormesh(x, y, E['delta_O_air_graph'][14, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_15 = ax.pcolormesh(x, y, E['delta_O_air_graph'][15, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_16 = ax.pcolormesh(x, y, E['delta_O_air_graph'][16, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_17 = ax.pcolormesh(x, y, E['delta_O_air_graph'][17, :, :], cmap='viridis', vmin=vmin, vmax=vmax)

pcol_18 = ax.pcolormesh(x, y, E['delta_O_air_graph'][18, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_19 = ax.pcolormesh(x, y, E['delta_O_air_graph'][19, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_20 = ax.pcolormesh(x, y, E['delta_O_air_graph'][20, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_21 = ax.pcolormesh(x, y, E['delta_O_air_graph'][21, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_22 = ax.pcolormesh(x, y, E['delta_O_air_graph'][22, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_23 = ax.pcolormesh(x, y, E['delta_O_air_graph'][23, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_24 = ax.pcolormesh(x, y, E['delta_O_air_graph'][24, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_25 = ax.pcolormesh(x, y, E['delta_O_air_graph'][25, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_26 = ax.pcolormesh(x, y, E['delta_O_air_graph'][26, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_27 = ax.pcolormesh(x, y, E['delta_O_air_graph'][27, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_28 = ax.pcolormesh(x, y, E['delta_O_air_graph'][28, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_29 = ax.pcolormesh(x, y, E['delta_O_air_graph'][29, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_30 = ax.pcolormesh(x, y, E['delta_O_air_graph'][30, :, :], cmap='viridis', vmin=vmin, vmax=vmax)

pcol_31 = ax.pcolormesh(x, y, E['delta_O_air_graph'][31, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_32 = ax.pcolormesh(x, y, E['delta_O_air_graph'][32, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_33 = ax.pcolormesh(x, y, E['delta_O_air_graph'][33, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_34 = ax.pcolormesh(x, y, E['delta_O_air_graph'][34, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_35 = ax.pcolormesh(x, y, E['delta_O_air_graph'][35, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_36 = ax.pcolormesh(x, y, E['delta_O_air_graph'][36, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_37 = ax.pcolormesh(x, y, E['delta_O_air_graph'][37, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_38 = ax.pcolormesh(x, y, E['delta_O_air_graph'][38, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_39 = ax.pcolormesh(x, y, E['delta_O_air_graph'][39, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_40 = ax.pcolormesh(x, y, E['delta_O_air_graph'][40, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_41 = ax.pcolormesh(x, y, E['delta_O_air_graph'][41, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_42 = ax.pcolormesh(x, y, E['delta_O_air_graph'][42, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_43 = ax.pcolormesh(x, y, E['delta_O_air_graph'][43, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_44 = ax.pcolormesh(x, y, E['delta_O_air_graph'][44, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_45 = ax.pcolormesh(x, y, E['delta_O_air_graph'][45, :, :], cmap='viridis', vmin=vmin, vmax=vmax)

'''''

pcol_46 = ax.pcolormesh(x, y, E['delta_O_air_graph'][46, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_47 = ax.pcolormesh(x, y, E['delta_O_air_graph'][47, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_48 = ax.pcolormesh(x, y, E['delta_O_air_graph'][48, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_49 = ax.pcolormesh(x, y, E['delta_O_air_graph'][49, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_50 = ax.pcolormesh(x, y, E['delta_O_air_graph'][50, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_51 = ax.pcolormesh(x, y, E['delta_O_air_graph'][51, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_52 = ax.pcolormesh(x, y, E['delta_O_air_graph'][52, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_53 = ax.pcolormesh(x, y, E['delta_O_air_graph'][53, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_54 = ax.pcolormesh(x, y, E['delta_O_air_graph'][54, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_55 = ax.pcolormesh(x, y, E['delta_O_air_graph'][55, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_56 = ax.pcolormesh(x, y, E['delta_O_air_graph'][56, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_57 = ax.pcolormesh(x, y, E['delta_O_air_graph'][57, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_58 = ax.pcolormesh(x, y, E['delta_O_air_graph'][58, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_59 = ax.pcolormesh(x, y, E['delta_O_air_graph'][59, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_60 = ax.pcolormesh(x, y, E['delta_O_air_graph'][60, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_61 = ax.pcolormesh(x, y, E['delta_O_air_graph'][61, :, :], cmap='viridis', vmin=vmin, vmax=vmax)



pcol_62 = ax.pcolormesh(x, y, E['delta_O_air_graph'][62, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_63 = ax.pcolormesh(x, y, E['delta_O_air_graph'][63, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_64 = ax.pcolormesh(x, y, E['delta_O_air_graph'][64, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_65 = ax.pcolormesh(x, y, E['delta_O_air_graph'][65, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_66 = ax.pcolormesh(x, y, E['delta_O_air_graph'][66, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_67 = ax.pcolormesh(x, y, E['delta_O_air_graph'][67, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_68 = ax.pcolormesh(x, y, E['delta_O_air_graph'][68, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_69 = ax.pcolormesh(x, y, E['delta_O_air_graph'][69, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_70 = ax.pcolormesh(x, y, E['delta_O_air_graph'][70, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_71 = ax.pcolormesh(x, y, E['delta_O_air_graph'][71, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_72 = ax.pcolormesh(x, y, E['delta_O_air_graph'][72, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_73 = ax.pcolormesh(x, y, E['delta_O_air_graph'][73, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_74 = ax.pcolormesh(x, y, E['delta_O_air_graph'][74, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_75 = ax.pcolormesh(x, y, E['delta_O_air_graph'][75, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_76 = ax.pcolormesh(x, y, E['delta_O_air_graph'][76, :, :], cmap='viridis', vmin=vmin, vmax=vmax)
pcol_77 = ax.pcolormesh(x, y, E['delta_O_air_graph'][77, :, :], cmap='viridis', vmin=vmin, vmax=vmax)

'''

ship = m.scatter(a, b, marker = 'o', color='r', zorder=5)

plt.tight_layout()

Figures_paths = '/home/riqo/Figures/'

plt.savefig(Figures_paths + 'Figure10_29', bbox_inches='tight', pad_inches=0)

plt.show()


