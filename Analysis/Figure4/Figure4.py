# This file was used to produce Figure 4

# Files 'I_retrieve_era5_data.py', 'II_netcdf_to_pickle.py', 'III_mass_flux_calculation.py', 'IV_surface_snow_calculation.py'
# and 'IV_surface_snow_calculation_no_fractionation.py' were reran from 2010 to 2016 for Dome C only

# Simulation ran for Dome C only to save on computing time

# Dome C coordinates: [-75, 123.25]

# In 'IV_surface_snow_calculation.py', b for loop refers to latitude (-75), and c for loop refers to longitude (123.25)

# Use the following to get the index values for the for loops.
# b_index = E['latitude'].index(-75.0)
# c_index = E['longitude'].index(123.25)

# To run for loop for one location: for x in range(x_index, x_index+1)

import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import joblib
import datetime
import matplotlib.dates as md
import datetime
import xlrd
import xlsxwriter

D = joblib.load('/home/riqo/mass_flux_files/mass_flux_pickle') # Modified version of file for DomeC between 2010 and 2016

I = joblib.load('/home/riqo/surface_snow_files/surface_snow_isotopic_composition_all') # Modified version of file for DomeC between 2010 and 2016

I_nf = joblib.load('/home/riqo/surface_snow_files/surface_snow_isotopic_composition_no_fractionation_all') # Modified version of file for DomeC between 2010 and 2016

excel = pd.read_excel('/home/riqo/surface_snow_files/domeC_observations.xls', sheet_name='Python') # Observations from Dome C

V = pd.DataFrame(excel, columns= ['date','delta_O_surface'])

E['latitude'] = E['latitude'].tolist()
E['longitude'] = E['longitude'].tolist()

b_index = E['latitude'].index(-75.0)
c_index = E['longitude'].index(123.25)

start = datetime.datetime.strptime('2010-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
end = datetime.datetime.strptime('2017-12-31 23:00:00', '%Y-%m-%d %H:%M:%S')

dif = int((end-start).total_seconds()/3600) ## time difference in hours

time_list = [(start + datetime.timedelta(hours=x)).strftime('%Y-%m-%d %H:%M:%S') for x in range(dif+1)]

time = []

for i in range(len(time_list)):
    time.append(datetime.datetime.strptime(time_list[i], '%Y-%m-%d %H:%M:%S'))

time_months = [time[373], time[1081], time[1789], time[2521], time[3253], time[3985], time[4717], time[5461], time[6193], time[6925], time[7657], time[8389]]

start_index = E['time'].index('2011-01-01 00:00:00')
end_index = E['time'].index('2016-01-01 00:00:00')

layers_1 = 5 #SUNITDC
layers_2 = 10 #PREREC
layers_3 = 15 #NIVO
total_cells = 50
cells_1 = total_cells - layers_1
cells_2 = total_cells - layers_2
cells_3 = total_cells - layers_3
start_time_index_1 = E['time'].index('2010-12-03 00:00:00')
start_time_index_2 = E['time'].index('2012-02-15 00:00:00')
start_time_index_3 = E['time'].index('2013-11-25 00:00:00')
end_time_index_1 = E['time'].index('2011-12-09 00:00:00')
end_time_index_2 = E['time'].index('2012-10-13 00:00:00')
end_time_index_3 = E['time'].index('2016-01-12 00:00:00')

delta_O_snow_1 = np.mean(I['delta_O_snow_layer_depth'][start_time_index_1:end_time_index_1,b_index,c_index,cells_1:], axis = 1)
delta_O_snow_2 = np.mean(I['delta_O_snow_layer_depth'][start_time_index_2:end_time_index_2,b_index,c_index,cells_2:], axis = 1)
delta_O_snow_3 = np.mean(I['delta_O_snow_layer_depth'][start_time_index_3:end_time_index_3,b_index,c_index,cells_3:], axis = 1)

delta_O_snow_1_nf = np.mean(I_nf['delta_O_snow_layer_depth'][start_time_index_1:end_time_index_1,b_index,c_index,cells_1:], axis = 1)
delta_O_snow_2_nf = np.mean(I_nf['delta_O_snow_layer_depth'][start_time_index_2:end_time_index_2,b_index,c_index,cells_2:], axis = 1)
delta_O_snow_3_nf = np.mean(I_nf['delta_O_snow_layer_depth'][start_time_index_3:end_time_index_3,b_index,c_index,cells_3:], axis = 1)

# graphs for 1 year

def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

fig, ax1 = plt.subplots()

fig.set_figwidth(10)

fig.subplots_adjust(right=0.75)

p1, = ax1.plot(time[start_time_index_1:end_time_index_1], delta_O_snow_1, color='k', label = 'from model (with fractionation)', zorder=100)
p2, = ax1.plot(time[start_time_index_2:end_time_index_2], delta_O_snow_2, color='k', zorder=100)
p3, = ax1.plot(time[start_time_index_3:end_time_index_3], delta_O_snow_3, color='k', zorder=100)

p10, = ax1.plot(V.date[:50], V.delta_O_surface[0:50], color='darkgreen', label = 'from literature', zorder=1) #SUNITDC
p20, = ax1.plot(V.date[50:122], V.delta_O_surface[50:122], color='darkgreen', zorder=1) #PREREC
p30, = ax1.plot(V.date[122:], V.delta_O_surface[122:], color='darkgreen', zorder=1) #NIVO

p100, = ax1.plot(time[start_time_index_1:end_time_index_1], delta_O_snow_1_nf, color='b', label = 'from model (without fractionation)', zorder=100)
p200, = ax1.plot(time[start_time_index_2:end_time_index_2], delta_O_snow_2_nf, color='b', zorder=100)
p300, = ax1.plot(time[start_time_index_3:end_time_index_3], delta_O_snow_3_nf, color='b', zorder=100)

ax1.set_ylabel('\u03B4$^{18}O$ of surface snow (\u2030 vs VSMOW)', size=16, color = 'k')
ax1.set_xlabel("Time", size=16)

ax1.yaxis.label.set_color(p1.get_color())

tkw = dict(size=4, width=1.5)
ax1.tick_params(axis='y', colors=p1.get_color(), **tkw)
ax1.tick_params(axis='x', **tkw)

ax1.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)

years = md.YearLocator()   # every year
months = md.MonthLocator()  # every month
format_ = md.DateFormatter('%Y')

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(format_)
ax1.xaxis.set_minor_locator(months)

ax1.axvline(x='2010-12-03 00:00:00', color='grey', linestyle='dashed')
ax1.axvline(x='2012-02-15 00:00:00', color='grey', linestyle='dashed')
ax1.axvline(x='2013-11-25 00:00:00', color='grey', linestyle='dashed')

ax1.axvline(x='2011-12-09 00:00:00', color='grey', linestyle='dashed')
ax1.axvline(x='2012-10-13 00:00:00', color='grey', linestyle='dashed')
ax1.axvline(x='2016-01-12 00:00:00', color='grey', linestyle='dashed')

plt.tight_layout()

Figures_paths = '/home/riqo/Figures/'

plt.savefig(Figures_paths + 'Figure4')
