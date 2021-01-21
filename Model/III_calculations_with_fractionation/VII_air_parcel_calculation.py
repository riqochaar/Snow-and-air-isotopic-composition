# The file was used to calculate the isotopic composition of the water vapour in each air parcel
# along its trajectory for the 'with fractionation' case

# The simulated time period was comprised of trajectories reaching the ship from between
# 00:00, 26th of January 2017 and 22:00, 2nd of February 2017

import numpy as np
import joblib
import xarray as xr
import pandas as pd
import datetime


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

D = joblib.load('/home/riqo/air_parcel_files/air_parcel_calculation_input')

lsm_file = joblib.load('/home/riqo/era5_files/era5_data_pickle')

lsm = lsm_file['lsm']

D['latitude'] = D['latitude'].tolist()
D['longitude'] = D['longitude'].tolist()
D['time'].append('2017-02-03 00:00:00')

start_time_index = range(D['time'].index('2017-01-19 00:00:00'), D['time'].index('2017-01-26 23:00:00'))

end_time_index = range(D['time'].index('2017-01-26 01:00:00'), D['time'].index('2017-02-03 00:00:00'))

C = {}

C['delta_H_air'] = np.empty((len(files), 169, 78), dtype=np.float32)
C['delta_O_air'] = np.empty((len(files), 169, 78), dtype=np.float32)

C['H2O_air_start'] = np.empty((len(files), 169, 78), dtype=np.float32)
C['HDO_air_start'] = np.empty((len(files), 169, 78), dtype=np.float32)
C['H218O_air_start'] = np.empty((len(files), 169, 78), dtype=np.float32)

C['delta_H_snow_trajectory'] = np.empty((len(files), 169, 78), dtype=np.float32)
C['delta_O_snow_trajectory'] = np.empty((len(files), 169, 78), dtype=np.float32)

C['q_air_trajectory_start'] = np.empty((len(files), 169, 78), dtype=np.float32)
C['q_air_trajectory_end'] = np.empty((len(files), 169, 78), dtype=np.float32)

C['q_difference_after_add_LE'] = np.empty((len(files), 169, 78), dtype=np.float32)
C['q_modelled'] = np.empty((len(files), 169, 78), dtype=np.float32)

C['latitude_trajectory'] = np.empty((len(files), 169, 78), dtype=np.float32)
C['longitude_trajectory'] = np.empty((len(files), 169, 78), dtype=np.float32)

C['LE_trajectory'] = np.empty((len(files), 169, 78), dtype=np.float32)

C['delta_H_subl'] = np.empty((len(files), 169, 78), dtype=np.float32)
C['delta_O_subl'] = np.empty((len(files), 169, 78), dtype=np.float32)

z_test = 0

L_subl =  2.83*10**6
P_triple = 610.5                                       
T_triple = 273.16  
R_v = 461.9  

def round_(array):
   return np.around(array * 4.0) / 4.0

for z in range(0, 191):

    print(z)

    traj = xr.open_dataset(data_path + files[z])

    lon = np.flip(traj['lon'].values, axis=0)
    lat = np.flip(traj['lat'].values, axis=0)                # shape = 169 x 78
    time = np.ndarray.tolist(traj['time'].values[::-1])      # shape = 169
    ntra = np.ndarray.tolist(traj['ntra'].values)            # shape = 78
    HPBL = np.ndarray.tolist(traj['HPBL'].values)

    P = np.flip(traj['P'].values, axis=0)  # shape = 169 x 78

    start_time = D['time'][start_time_index[z]]
    end_time = D['time'][end_time_index[z]]

    C['time'] = D['time'][start_time_index[z]:end_time_index[z]]
    C['latitude'] = D['latitude']
    C['longitude'] = D['longitude']

    C['LE'] = D['LE'][start_time_index[z]:end_time_index[z],:,:]

    C['skt'] = D['skt'][start_time_index[z]:end_time_index[z],:,:]
    C['t2m'] = D['t2m'][start_time_index[z]:end_time_index[z],:,:]
    C['d2m'] = D['d2m'][start_time_index[z]:end_time_index[z],:,:]
    C['sp'] = D['sp'][start_time_index[z]:end_time_index[z],:,:]

    C['delta_H_snow'] = D['delta_H_snow'][start_time_index[z]:end_time_index[z],:,:]
    C['delta_O_snow'] = D['delta_O_snow'][start_time_index[z]:end_time_index[z],:,:]

    C['q_air'] = D['q_air'][start_time_index[z]:end_time_index[z],:,:]

    M_H2O = 18
    M_HDO = 19
    M_H218O = 20

    H_VSMOW = 155.95 * (10 ** (-6))                         # VSMOW hydrogen isotopic ratio
    O_VSMOW = 2005.20 * (10 ** (-6))                        # VSMOW oxygen isotopic ratio

    air_W = 1                           # air area width (m)
    air_L = 1                           # air area length (m)
    air_D = 1000                         # air depth (m)
    air_A = air_W * air_L               # air area (m2)
    air_V = air_W * air_L * air_D       # air volume (m3)
    air_rho = 1.225                     # air density (kg/m3)
    air_mass_start = air_V * air_rho    # air mass (kg)

    rounded_lat = round_(np.asarray(lat))
    rounded_lon = round_(np.asarray(lon))

    for a in range(0, len(C['time'])):

        for b in range(0, len(ntra)):

            if rounded_lon[a, b] == 180:

                rounded_lon[a, b] = -180

    for i in range(0, len(C['longitude'])):

        if C['longitude'][i] > 180:
            C['longitude'][i] = C['longitude'][i] - 360

    a_test = len(C['time']) -2
    b_test = 2

    for a in range(0, len(C['time'])-1):

        for b in range(0, len(ntra)):

            if P[-2,b] >= 0:

                lat_index_start = C['latitude'].index(rounded_lat[a, b])
                lon_index_start = C['longitude'].index(rounded_lon[a, b])

                if lsm[lat_index_start,lon_index_start] == 0:

                    alpha_H = np.exp((1158.8 * (C['skt'][a][lat_index_start, lon_index_start]**3/10**(12))) - (1620.1 * (C['skt'][a][lat_index_start, lon_index_start]**2/10**9)) + (794.84 * (C['skt'][a][lat_index_start, lon_index_start]/10**6)) - 0.16104 + (2.9992 * (10**6/C['skt'][a][lat_index_start, lon_index_start]**3)))

                    alpha_O = np.exp(-0.007685 + (6.7123/C['skt'][a][lat_index_start, lon_index_start]) - (1.6664 * (10**3/C['skt'][a][lat_index_start, lon_index_start]**2)) + (0.35041 * (10**6/C['skt'][a][lat_index_start, lon_index_start]**3)))

                else:

                    alpha_H = np.exp(0.2133 - (203.10 / C['skt'][a][lat_index_start, lon_index_start]) + (48888 / (C['skt'][a][lat_index_start, lon_index_start]) ** 2))
                    alpha_O = np.exp(0.0831 - (49.192 / C['skt'][a][lat_index_start, lon_index_start]) + (8312.5 / (C['skt'][a][lat_index_start, lon_index_start]) ** 2))


                if a == 0:

                    R_H_air_start = ((np.mean(D['delta_H_snow_starting_delta'][264:432, lat_index_start, lon_index_start]) / 1000) + 1) * H_VSMOW / alpha_H      
                    R_O_air_start = ((np.mean(D['delta_O_snow_starting_delta'][264:432, lat_index_start, lon_index_start]) / 1000) + 1) * O_VSMOW / alpha_O

                    q_air_start = C['q_air'][a][lat_index_start, lon_index_start]
                    water_vapour_mass = q_air_start * air_mass_start / (1 - q_air_start)

                    H2O_air_start = water_vapour_mass / (1 + ((1 / M_H2O) * ((R_H_air_start * M_HDO) + (R_O_air_start * M_H218O))))
                    HDO_air_start = H2O_air_start * R_H_air_start * (M_HDO / M_H2O)
                    H218O_air_start = H2O_air_start * R_O_air_start * (M_H218O / M_H2O)

                else:

                    H2O_air_start = C['H2O_air_start'][z, a-1, b]
                    HDO_air_start = C['HDO_air_start'][z, a-1, b]
                    H218O_air_start = C['H218O_air_start'][z, a-1, b]

                    delta_H_air_start = C['delta_H_air'][z,a-1,b]
                    delta_O_air_start = C['delta_O_air'][z,a-1,b]

                    q_air_start = C['q_air_trajectory_end'][z, a-1, b]

                R_H_air_start = HDO_air_start / H2O_air_start * (M_H2O / M_HDO)
                R_O_air_start = H218O_air_start / H2O_air_start * (M_H2O / M_H218O)

                R_H_snow = ((np.mean(D['delta_H_snow_starting_delta'][a+264:a+432, lat_index_start, lon_index_start], axis=0) / 1000) + 1) * H_VSMOW
                R_O_snow = ((np.mean(D['delta_O_snow_starting_delta'][a+264:a+432, lat_index_start, lon_index_start], axis=0) / 1000) + 1) * O_VSMOW

                delta_H_snow = ((R_H_snow / H_VSMOW) - 1) * 1000
                delta_O_snow = ((R_O_snow / O_VSMOW) - 1) * 1000

                R_H_subl = R_H_snow / alpha_H
                R_O_subl = R_O_snow / alpha_O

                delta_H_subl = ((R_H_subl / H_VSMOW) - 1) * 1000
                delta_O_subl = ((R_O_subl / O_VSMOW) - 1) * 1000

                H2O_subl = abs(C['LE'][a][lat_index_start, lon_index_start] * air_A) / (1 + ((1 / M_H2O) * ((R_H_subl * M_HDO) + (R_O_subl * M_H218O))))
                HDO_subl = H2O_subl * R_H_subl * (M_HDO / M_H2O)
                H218O_subl = H2O_subl * R_O_subl * (M_H218O / M_H2O)

                H2O_air = H2O_air_start + H2O_subl
                HDO_air = HDO_air_start + HDO_subl
                H218O_air = H218O_air_start + H218O_subl

                R_H_air_intermediate = HDO_air / H2O_air * (M_H2O / M_HDO)
                R_O_air_intermediate = H218O_air / H2O_air * (M_H2O / M_H218O)

                water_vapour_mass_modelled = H2O_air + HDO_air + H218O_air
                q_modelled = water_vapour_mass_modelled / (water_vapour_mass_modelled + air_mass_start)

                lat_index = C['latitude'].index(rounded_lat[a + 1, b])
                lon_index = C['longitude'].index(rounded_lon[a + 1, b])

                q_air_end = C['q_air'][a + 1][lat_index, lon_index]

                q_difference_graph = q_air_end - q_modelled

                if q_modelled > q_air_end:

                    q_difference = q_modelled - q_air_end

                    water_vapour_difference = q_difference * air_mass_start / (1 - q_difference)

                    H2O_air_difference = water_vapour_difference / (1 + ((1 / M_H2O) * ((R_H_air_intermediate * M_HDO) + (R_O_air_intermediate * M_H218O))))
                    HDO_air_difference = H2O_air_difference * R_H_air_intermediate * (M_HDO / M_H2O)
                    H218O_air_difference = H2O_air_difference * R_O_air_intermediate * (M_H218O / M_H2O)

                    H2O_air = H2O_air - H2O_air_difference
                    HDO_air = HDO_air - HDO_air_difference
                    H218O_air = H218O_air - H218O_air_difference

                else:

                    q_difference = q_air_end - q_modelled

                    water_vapour_difference = q_difference * air_mass_start / (1 - q_difference)

                    H2O_air_difference = water_vapour_difference / (1 + ((1 / M_H2O) * ((R_H_air_intermediate * M_HDO) + (R_O_air_intermediate * M_H218O))))
                    HDO_air_difference = H2O_air_difference * R_H_air_intermediate * (M_HDO / M_H2O)
                    H218O_air_difference = H2O_air_difference * R_O_air_intermediate * (M_H218O / M_H2O)

                    H2O_air = H2O_air + H2O_air_difference
                    HDO_air = HDO_air + HDO_air_difference
                    H218O_air = H218O_air + H218O_air_difference

                R_H_air = HDO_air / H2O_air * (M_H2O / M_HDO)
                R_O_air = H218O_air / H2O_air * (M_H2O / M_H218O)

                delta_H_air = ((R_H_air / H_VSMOW) - 1) * 1000
                delta_O_air = ((R_O_air / O_VSMOW) - 1) * 1000

                C['delta_H_air'][z,a,b] = delta_H_air
                C['delta_O_air'][z,a,b] = delta_O_air

                C['delta_H_snow_trajectory'][z, a, b] = delta_H_snow
                C['delta_O_snow_trajectory'][z, a, b] = delta_O_snow

                C['q_air_trajectory_start'][z, a, b] = q_air_start
                C['q_air_trajectory_end'][z, a, b] = q_air_end

                C['q_difference_after_add_LE'][z,a,b] = q_difference_graph
                C['q_modelled'][z,a,b] = q_modelled

                C['latitude_trajectory'][z, a, b] = rounded_lat[a, b]
                C['longitude_trajectory'][z, a, b] = rounded_lon[a, b]

                C['LE_trajectory'][z, a, b] = C['LE'][a][lat_index_start, lon_index_start]

                C['H2O_air_start'][z,a,b] = H2O_air
                C['HDO_air_start'][z,a,b] = HDO_air
                C['H218O_air_start'][z,a,b] = H218O_air

                C['delta_H_subl'][z,a,b] = delta_H_subl
                C['delta_O_subl'][z,a,b] = delta_O_subl


            else:

                C['delta_H_air'][z,a,b] = np.nan
                C['delta_O_air'][z,a,b] = np.nan

                C['delta_H_snow_trajectory'][z, a, b] = np.nan
                C['delta_O_snow_trajectory'][z, a, b] = np.nan

                C['q_air_trajectory_start'][z, a, b] = np.nan
                C['q_air_trajectory_end'][z, a, b] = np.nan

                C['q_difference_after_add_LE'][z,a,b] = np.nan
                C['q_modelled'][z,a,b] = np.nan

                C['latitude_trajectory'][z, a, b] = np.nan
                C['longitude_trajectory'][z, a, b] = np.nan

                C['LE_trajectory'][z, a, b] = np.nan

                C['H2O_air_start'][z, a, b] = np.nan
                C['HDO_air_start'][z, a, b] = np.nan
                C['H218O_air_start'][z, a, b] = np.nan

                C['delta_H_subl'][z,a,b] = np.nan
                C['delta_O_subl'][z,a,b] = np.nan


def myround(x, prec=2, base=0.25):
    return round(base * round(float(x) / base), prec)

for z in range(0, len(files)):

    print(z)

    traj = xr.open_dataset(data_path + files[z])

    lon = np.flip(traj['lon'].values, axis=0)
    lat = np.flip(traj['lat'].values, axis=0)                # shape = 169 x 78
    time = np.ndarray.tolist(traj['time'].values[::-1])      # shape = 169
    ntra = np.ndarray.tolist(traj['ntra'].values)            # shape = 78

    for a in range(0, len(time)):

        for b in range(0, len(ntra)):

            rounded_lat = myround(lat[a,b])
            rounded_lon = myround(lon[a,b])

            if rounded_lon == 180:

                rounded_lon = -180

            C['latitude_trajectory'][z,a,b] = rounded_lat
            C['longitude_trajectory'][z,a,b] = rounded_lon

for i in range(0, len(C['longitude'])):

    if C['longitude'][i] == -180.75:

        C['longitude'][i] = 179.25

    if C['longitude'][i] == -180.50:

        C['longitude'][i] = 179.50

    if C['longitude'][i] == -180.25:

        C['longitude'][i] = 179.75

start = datetime.datetime.strptime('2017-01-26 00:00:00', '%Y-%m-%d %H:%M:%S')
end = datetime.datetime.strptime('2017-02-02 23:00:00', '%Y-%m-%d %H:%M:%S')

dif = int((end-start).total_seconds()/3600) ## time difference in hours

time_list = [(start + datetime.timedelta(hours=x)).strftime('%Y-%m-%d %H:%M:%S') for x in range(dif+1)]

C['time_192'] = time_list

f = open('/home/riqo/air_parcel_files/air_parcel_calculation_output', "wb")

joblib.dump(C, f)

f.close()


