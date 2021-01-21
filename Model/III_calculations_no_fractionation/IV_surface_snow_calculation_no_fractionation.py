# This file was used to calculate the surface snow isotopic composition for the 'without fractionation' case

# This is a function file which is called by 'IV_surface_snow_multiprocessing_no_fractionation.py'

import pandas as pd
import numpy as np
import joblib

PKL_path = '/home/riqo/mass_flux_files/'

file = 'mass_flux_pickle'

D = joblib.load(PKL_path + file)

lsm_file = joblib.load('/home/riqo/era5_files/era5_data_pickle')

lsm = lsm_file['lsm']

most_northern_point = 133

lsm_1 = lsm[:most_northern_point,:]

lsm_1 = np.where(lsm_1 == 1, 0, lsm_1)

lsm_2 = lsm[most_northern_point:,:]

lsm_only_antarctica = np.concatenate((lsm_1, lsm_2))

def isotope(longitude_start, longitude_end, change_name, depth):
    # other dictionary for quantities which don't have to be graphed

    I = {}

    O = {}

    # Molecular mass of isotopes in g/mol

    M_H2O = 18
    M_HDO = 19
    M_H218O = 20

    H_VSMOW = 155.95 * (10 ** (-6))  # VSMOW hydrogen isotopic ratio
    O_VSMOW = 2005.20 * (10 ** (-6))  # VSMOW oxygen isotopic ratio

    delta_H_lit_air = -260  # delta D value found from literature for water vapour
    delta_O_lit_air = -35  # delta O value found from literature for water vapour
    R_H_lit_air = ((delta_H_lit_air / 1000) + 1) * H_VSMOW  # Hydrogen ratio of water vapour from literature
    R_O_lit_air = ((delta_O_lit_air / 1000) + 1) * O_VSMOW  # Hydrogen ratio of water vapour from literature

    snow_W = 1  # Snow area width (m)
    snow_L = 1  # Snow area length (m)
    snow_D = depth  # Snow depth (m)
    snow_A = snow_W * snow_L  # Snow area (m2)
    snow_V = snow_W * snow_L * snow_D  # Snow volume (m3)
    snow_rho = 350  # Snow density (kg/m3)
    snow_mass_start = snow_V * snow_rho  # Snow mass (kg)

    longitude_store = longitude_end - longitude_start

    time = len(D['time'])

    I['lsm_only_antarctica'] = lsm_only_antarctica

    # Creating empty 3D numpy arrays to store calculated data

    I['time'] = D['time']
    I['latitude'] = D['latitude']
    I['longitude'] = D['longitude']

    O['H2O_mass_snow'] = np.empty((time, len(D['latitude']), len(D['longitude'])), dtype=np.float32)
    O['HDO_mass_snow'] = np.empty((time, len(D['latitude']), len(D['longitude'])), dtype=np.float32)
    O['H218O_mass_snow'] = np.empty((time, len(D['latitude']), len(D['longitude'])), dtype=np.float32)

    I['delta_H_snow'] = np.empty((time, len(D['latitude']), longitude_store), dtype=np.float32)
    I['delta_O_snow'] = np.empty((time, len(D['latitude']), longitude_store), dtype=np.float32)

    O['mass_snowfall_sum'] = np.empty((time, len(D['latitude']), len(D['longitude'])), dtype=np.float32)

    # Creating empty lists for storage of isotopic ratios of layers covered in snow after snowfall or deposition

    n = len(D['latitude']) * len(D['longitude'])

    R_H_snow_layer = [[] for _ in range(n)]
    R_O_snow_layer = [[] for _ in range(n)]

    R_H_snow_layer_50 = [[] for _ in range(n)]
    R_O_snow_layer_50 = [[] for _ in range(n)]

    final_snow_layers = []

    # LE > 0 = deposition
    # LE < 0 = sublimation

    for b in range(0, len(D['latitude'])):

        for c in range(0, len(D['longitude'])):
            snowfall_sum = np.sum(D['mass_snowfall'][:, b, c])

            final_snow_layers.append(np.floor(snowfall_sum / snow_mass_start))

    store_layers_number = 50

    for a in range(0, time):

        delta_O_lit_snow = 0.45 * (D['t2m'][a] - 273.15) - 31.5  # delta O correlation found from literature for surface snow
        delta_H_lit_snow = (7.75 * delta_O_lit_snow) - 4.93  # delta D correlation found from literature for surface snow

        R_H_lit_snow = ((delta_H_lit_snow / 1000) + 1) * H_VSMOW  # Hydrogen isotopic ratio of surface snow from literature
        R_O_lit_snow = ((delta_O_lit_snow / 1000) + 1) * O_VSMOW  # Oxygen isotopic ratio of surface snow from literature

        # literature isotopic ratios used to initialise simulation

        if a == 0:

            mass_snowfall_sum_previous = 0 * D['skt'][a]
            O['mass_snowfall_sum'][a] = 0 * D['skt'][a]

        # otherwise mass of isotope in snow at previous time step is used at the start of the next time step

        else:

            mass_snowfall_sum_previous = O['mass_snowfall_sum'][a - 1]

        # Calculating and storing the mass of snow in the layer

        # Calculating the delta values for snowfall from correlations found in literature

        delta_O_snowfall = 0.45 * (D['t2m'][a] - 273.15) - 31.5

        delta_H_snowfall = (7.75 * delta_O_snowfall) - 4.93

        # Calculating the isotopic ratios in the snowfall

        R_H_snowfall = ((delta_H_snowfall / 1000) + 1) * H_VSMOW
        R_O_snowfall = ((delta_O_snowfall / 1000) + 1) * O_VSMOW

        for b in range(most_northern_point, len(D['latitude'])):

            for c in range(longitude_start, longitude_end):

                if lsm_only_antarctica[b,c] == 0:

                    I['delta_H_snow'][a][b, c - longitude_start] = 0
                    I['delta_O_snow'][a][b, c - longitude_start] = 0

                else:

                    LE = D['LE'][a][b, c]

                    # if we have sublimation, do the following:

                    if LE <= 0:

                        if a == 0:
                            R_H_snow_layer[c + (b * 1440)].append(R_H_lit_snow[b, c])
                            R_H_snow_layer[c + (b * 1440)].append(R_H_lit_snow[b, c])

                            R_O_snow_layer[c + (b * 1440)].append(R_O_lit_snow[b, c])
                            R_O_snow_layer[c + (b * 1440)].append(R_O_lit_snow[b, c])

                            R_H_snow_layer_50[c + (b * 1440)] = store_layers_number * [R_H_lit_snow[b, c]]
                            R_O_snow_layer_50[c + (b * 1440)] = store_layers_number * [R_O_lit_snow[b, c]]

                        H2O_mass_snow_start = snow_mass_start / (1 + ((1 / M_H2O) * ((np.array(R_H_snow_layer[c + (b * 1440)][1:]) * M_HDO) + (np.array(R_O_snow_layer[c + (b * 1440)][1:]) * M_H218O))))
                        HDO_mass_snow_start = H2O_mass_snow_start * np.array(R_H_snow_layer[c + (b * 1440)][1:]) * (M_HDO / M_H2O)
                        H218O_mass_snow_start = H2O_mass_snow_start * np.array(R_O_snow_layer[c + (b * 1440)][1:]) * (M_H218O / M_H2O)

                        R_H_subl = np.array(R_H_snow_layer[c + (b * 1440)][1:])
                        R_O_subl = np.array(R_O_snow_layer[c + (b * 1440)][1:])

                        R_H_subl[-1] = np.array(R_H_snow_layer[c + (b * 1440)][-1])
                        R_O_subl[-1] = np.array(R_O_snow_layer[c + (b * 1440)][-1])

                        H2O_subl = abs(LE * snow_A) / (1 + ((1 / M_H2O) * ((R_H_subl * M_HDO) + (R_O_subl * M_H218O))))
                        HDO_subl = H2O_subl * R_H_subl * (M_HDO / M_H2O)
                        H218O_subl = H2O_subl * R_O_subl * (M_H218O / M_H2O)

                        H2O_mix = abs(LE * snow_A) / (1 + ((1 / M_H2O) * ((np.array(R_H_snow_layer[c + (b * 1440)][0:-1]) * M_HDO) + (np.array(R_O_snow_layer[c + (b * 1440)][0:-1]) * M_H218O))))
                        HDO_mix = H2O_mix * np.array(R_H_snow_layer[c + (b * 1440)][0:-1]) * (M_HDO / M_H2O)
                        H218O_mix = H2O_mix * np.array(R_O_snow_layer[c + (b * 1440)][0:-1]) * (M_H218O / M_H2O)

                        H2O_mass_snow = H2O_mass_snow_start - H2O_subl + H2O_mix
                        HDO_mass_snow = HDO_mass_snow_start - HDO_subl + HDO_mix
                        H218O_mass_snow = H218O_mass_snow_start - H218O_subl + H218O_mix

                        R_H_snow = HDO_mass_snow / H2O_mass_snow * (M_H2O / M_HDO)
                        R_O_snow = H218O_mass_snow / H2O_mass_snow * (M_H2O / M_H218O)

                        R_H_snow_layer[c + (b * 1440)][1:] = R_H_snow
                        R_O_snow_layer[c + (b * 1440)][1:] = R_O_snow

                    elif LE > 0:

                        if a == 0:
                            R_H_snow_layer[c + (b * 1440)].append(R_H_lit_snow[b, c])
                            R_H_snow_layer[c + (b * 1440)].append(R_H_lit_snow[b, c])

                            R_O_snow_layer[c + (b * 1440)].append(R_O_lit_snow[b, c])
                            R_O_snow_layer[c + (b * 1440)].append(R_O_lit_snow[b, c])

                        H2O_mass_snow_start = snow_mass_start / (1 + ((1 / M_H2O) * ((np.array(R_H_snow_layer[c + (b * 1440)][0:]) * M_HDO) + (np.array(R_O_snow_layer[c + (b * 1440)][0:]) * M_H218O))))
                        HDO_mass_snow_start = H2O_mass_snow_start * np.array(R_H_snow_layer[c + (b * 1440)][0:]) * (M_HDO / M_H2O)
                        H218O_mass_snow_start = H2O_mass_snow_start * np.array(R_O_snow_layer[c + (b * 1440)][0:]) * (M_H218O / M_H2O)

                        R_H_depo = np.array(R_H_snow_layer[c + (b * 1440)][1:])
                        R_O_depo = np.array(R_O_snow_layer[c + (b * 1440)][1:])

                        R_H_depo = np.append(R_H_depo, R_H_lit_air)
                        R_O_depo = np.append(R_O_depo, R_O_lit_air)

                        H2O_depo = abs(LE * snow_A) / (1 + ((1 / M_H2O) * ((R_H_depo * M_HDO) + (R_O_depo * M_H218O))))
                        HDO_depo = H2O_depo * R_H_depo * (M_HDO / M_H2O)
                        H218O_depo = H2O_depo * R_O_depo * (M_H218O / M_H2O)

                        H2O_mix = abs(LE * snow_A) / (1 + ((1 / M_H2O) * ((np.array(R_H_snow_layer[c + (b * 1440)][0:]) * M_HDO) + (np.array(R_O_snow_layer[c + (b * 1440)][0:]) * M_H218O))))
                        HDO_mix = H2O_mix * np.array(R_H_snow_layer[c + (b * 1440)][0:]) * (M_HDO / M_H2O)
                        H218O_mix = H2O_mix * np.array(R_O_snow_layer[c + (b * 1440)][0:]) * (M_H218O / M_H2O)

                        H2O_mass_snow = H2O_mass_snow_start + H2O_depo - H2O_mix
                        HDO_mass_snow = HDO_mass_snow_start + HDO_depo - HDO_mix
                        H218O_mass_snow = H218O_mass_snow_start + H218O_depo - H218O_mix

                        R_H_snow = HDO_mass_snow / H2O_mass_snow * (M_H2O / M_HDO)
                        R_O_snow = H218O_mass_snow / H2O_mass_snow * (M_H2O / M_H218O)

                        R_H_snow_layer[c + (b * 1440)][0:] = R_H_snow
                        R_O_snow_layer[c + (b * 1440)][0:] = R_O_snow

                    O['mass_snowfall_sum'][a][b, c] = mass_snowfall_sum_previous[b, c] + D['mass_snowfall'][a][b, c]

                    if a == 0:
                        H2O_mass_snow = np.append(H2O_mass_snow, snow_mass_start / (1 + ((1 / M_H2O) * ((R_H_snowfall[b, c] * M_HDO) + (R_O_snowfall[b, c] * M_H218O)))))
                        HDO_mass_snow = np.append(HDO_mass_snow, H2O_mass_snow[-1] * R_H_snowfall[b, c] * (M_HDO / M_H2O))
                        H218O_mass_snow = np.append(H218O_mass_snow, H2O_mass_snow[-1] * R_O_snowfall[b, c] * (M_H218O / M_H2O))

                        R_H_snow = HDO_mass_snow[-1] / H2O_mass_snow[-1] * (M_H2O / M_HDO)
                        R_O_snow = H218O_mass_snow[-1] / H2O_mass_snow[-1] * (M_H2O / M_H218O)

                        R_H_snow_layer[c + (b * 1440)].append(R_H_snow)
                        R_O_snow_layer[c + (b * 1440)].append(R_O_snow)

                        O['mass_snowfall_sum'][a][b, c] = 0

                    if O['mass_snowfall_sum'][a][b, c] >= snow_mass_start:

                        while O['mass_snowfall_sum'][a][b, c] >= snow_mass_start:
                            H2O_mass_snow = np.append(H2O_mass_snow, snow_mass_start / (1 + ((1 / M_H2O) * ((R_H_snowfall[b, c] * M_HDO) + (R_O_snowfall[b, c] * M_H218O)))))
                            HDO_mass_snow = np.append(HDO_mass_snow, H2O_mass_snow[-1] * R_H_snowfall[b, c] * (M_HDO / M_H2O))
                            H218O_mass_snow = np.append(H218O_mass_snow, H2O_mass_snow[-1] * R_O_snowfall[b, c] * (M_H218O / M_H2O))

                            R_H_snow = HDO_mass_snow[-1] / H2O_mass_snow[-1] * (M_H2O / M_HDO)
                            R_O_snow = H218O_mass_snow[-1] / H2O_mass_snow[-1] * (M_H2O / M_H218O)

                            R_H_snow_layer[c + (b * 1440)].append(R_H_snow)
                            R_O_snow_layer[c + (b * 1440)].append(R_O_snow)

                            O['mass_snowfall_sum'][a][b, c] = O['mass_snowfall_sum'][a][b, c] - snow_mass_start

                    O['H2O_mass_snow'][a][b, c] = H2O_mass_snow[-1]
                    O['HDO_mass_snow'][a][b, c] = HDO_mass_snow[-1]
                    O['H218O_mass_snow'][a][b, c] = H218O_mass_snow[-1]

                    R_H_snow = HDO_mass_snow[-1] / H2O_mass_snow[-1] * (M_H2O / M_HDO)
                    R_O_snow = H218O_mass_snow[-1] / H2O_mass_snow[-1] * (M_H2O / M_H218O)

                    # Calculating the final snow delta values (graphed)

                    delta_H_snow = ((R_H_snow / H_VSMOW) - 1) * 1000
                    delta_O_snow = ((R_O_snow / O_VSMOW) - 1) * 1000

                    # Saving these values in a list so we can graph them

                    I['delta_H_snow'][a][b, c - longitude_start] = delta_H_snow
                    I['delta_O_snow'][a][b, c - longitude_start] = delta_O_snow

    PKL_path_save = '/home/riqo/surface_snow_files/'

    file_save = 'surface_snow_isotopic_composition_no_fractionation' + str(change_name)

    f = open(PKL_path_save + file_save, "wb")

    joblib.dump(I, f, compress=9)

    f.close()

