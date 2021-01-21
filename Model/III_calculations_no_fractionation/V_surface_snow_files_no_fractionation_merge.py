# This file was used to merge the 'surface_snow_isotopic_composition_no_fractionation...' files
# generated from 'IV_surface_snow_calculation_no_fractionation.py'

import pandas as pd
import numpy as np
import joblib

# file names and path

PKL_path = '/home/riqo/surface_snow_files/'

files = [
'surface_snow_isotopic_composition_no_fractionation_01',
'surface_snow_isotopic_composition_no_fractionation_02',
'surface_snow_isotopic_composition_no_fractionation_03',
'surface_snow_isotopic_composition_no_fractionation_04',
'surface_snow_isotopic_composition_no_fractionation_05',
'surface_snow_isotopic_composition_no_fractionation_06',
'surface_snow_isotopic_composition_no_fractionation_07',
'surface_snow_isotopic_composition_no_fractionation_08',
'surface_snow_isotopic_composition_no_fractionation_09',
'surface_snow_isotopic_composition_no_fractionation_10',
'surface_snow_isotopic_composition_no_fractionation_11',
'surface_snow_isotopic_composition_no_fractionation_12',
'surface_snow_isotopic_composition_no_fractionation_13',
'surface_snow_isotopic_composition_no_fractionation_14',
'surface_snow_isotopic_composition_no_fractionation_15',
'surface_snow_isotopic_composition_no_fractionation_16',
'surface_snow_isotopic_composition_no_fractionation_17',
'surface_snow_isotopic_composition_no_fractionation_18',
'surface_snow_isotopic_composition_no_fractionation_19',
'surface_snow_isotopic_composition_no_fractionation_20',
'surface_snow_isotopic_composition_no_fractionation_21',
'surface_snow_isotopic_composition_no_fractionation_22',
'surface_snow_isotopic_composition_no_fractionation_23',
'surface_snow_isotopic_composition_no_fractionation_24',
]

I0 = joblib.load(PKL_paths + files[0])
I1 = joblib.load(PKL_paths + files[1])
I2 = joblib.load(PKL_paths + files[2])
I3 = joblib.load(PKL_paths + files[3])
I4 = joblib.load(PKL_paths + files[4])
I5 = joblib.load(PKL_paths + files[5])
I6 = joblib.load(PKL_paths + files[6])
I7 = joblib.load(PKL_paths + files[7])

I8 = joblib.load(PKL_paths + files[8])
I9 = joblib.load(PKL_paths + files[9])
I10 = joblib.load(PKL_paths + files[10])
I11 = joblib.load(PKL_paths + files[11])
I12 = joblib.load(PKL_paths + files[12])
I13 = joblib.load(PKL_paths + files[13])
I14 = joblib.load(PKL_paths + files[14])
I15 = joblib.load(PKL_paths + files[15])

I16 = joblib.load(PKL_paths + files[16])
I17 = joblib.load(PKL_paths + files[17])
I18 = joblib.load(PKL_paths + files[18])
I19 = joblib.load(PKL_paths + files[19])
I20 = joblib.load(PKL_paths + files[20])
I21 = joblib.load(PKL_paths + files[21])
I22 = joblib.load(PKL_paths + files[22])
I23 = joblib.load(PKL_paths + files[23])


start_of_2017 = I0['time'].index('2017-01-01 00:00:00')

I = {}

I['time'] = I0['time']
I['latitude'] = I0['latitude']
I['longitude'] = I0['longitude']

I['delta_H_snow'] = np.concatenate((I0['delta_H_snow'], I1['delta_H_snow'], I2['delta_H_snow'], I3['delta_H_snow'],
                                    I4['delta_H_snow'], I5['delta_H_snow'], I6['delta_H_snow'], I7['delta_H_snow'],
                                    I8['delta_H_snow'], I9['delta_H_snow'], I10['delta_H_snow'], I11['delta_H_snow'],
                                    I12['delta_H_snow'], I13['delta_H_snow'], I14['delta_H_snow'], I15['delta_H_snow'],
                                    I16['delta_H_snow'], I17['delta_H_snow'], I18['delta_H_snow'], I19['delta_H_snow'],
                                    I20['delta_H_snow'], I21['delta_H_snow'], I22['delta_H_snow'], I23['delta_H_snow']), axis = 2)

I['delta_O_snow'] = np.concatenate((I0['delta_O_snow'], I1['delta_O_snow'], I2['delta_O_snow'], I3['delta_O_snow'],
                                    I4['delta_O_snow'], I5['delta_O_snow'], I6['delta_O_snow'], I7['delta_O_snow'],
                                    I8['delta_O_snow'], I9['delta_O_snow'], I10['delta_O_snow'], I11['delta_O_snow'],
                                    I12['delta_O_snow'], I13['delta_O_snow'], I14['delta_O_snow'], I15['delta_O_snow'],
                                    I16['delta_O_snow'], I17['delta_O_snow'], I18['delta_O_snow'], I19['delta_O_snow'],
                                    I20['delta_O_snow'], I21['delta_O_snow'], I22['delta_O_snow'], I23['delta_O_snow']), axis = 2)

most_northern_point = 133

I['delta_H_snow'] = I['delta_H_snow'][:,most_northern_point:,:]
I['delta_O_snow'] = I['delta_O_snow'][:,most_northern_point:,:]

delta_water_array = np.zeros((len(I0['time']), most_northern_point, len(I0['longitude'])), dtype=np.float32)

I['delta_H_snow'] = np.concatenate((delta_water_array, I['delta_H_snow']), axis=1)
I['delta_O_snow'] = np.concatenate((delta_water_array, I['delta_O_snow']), axis=1)

I['lsm_only_antarctica'] = I0['lsm_only_antarctica']

PKL_path_save = '/home/riqo/surface_snow_files/'

file_save = 'surface_snow_isotopic_composition_no_fractionation_all'

f = open(PKL_paths_save + file_save, "wb")

joblib.dump(I, f)

f.close()





