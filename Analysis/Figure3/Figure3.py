# This file was used to produce Figure 3

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

# I = ['delta_O_snow', 'delta_O_snow_nf', 'LE', 'snowfall_sum', 't2m', 'average_monthly_temperature']

I = joblib.load('/home/riqo/surface_snow_files/domeC_data_Figure3')

start = datetime.datetime.strptime('2017-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
end = datetime.datetime.strptime('2017-12-31 23:00:00', '%Y-%m-%d %H:%M:%S')

dif = int((end-start).total_seconds()/3600) ## time difference in hours

time_list = [(start + datetime.timedelta(hours=x)).strftime('%Y-%m-%d %H:%M:%S') for x in range(dif+1)]

first_index_new_snow_layer = []
final_index_new_snow_layer = []

delta_difference = []
average_LE = []

first_index_new_snow_layer.append(0)

for a in range(0,8759):

    if I[0,a] - 0.1 > I[0,a+1]:

        first_index_new_snow_layer.append(a+1)
        final_index_new_snow_layer.append(a)

for a in range(0,len(first_index_new_snow_layer)-1):

    delta_difference_value = I[0,final_index_new_snow_layer[a]] - I[0,first_index_new_snow_layer[a]]
    average_LE_value = np.mean(I[2,first_index_new_snow_layer[a]:final_index_new_snow_layer[a]])

    delta_difference.append(delta_difference_value)
    average_LE.append(average_LE_value)

average_delta_difference = np.nanmean(delta_difference)
average_LE_final_value = np.nanmean(average_LE)

# indicies = [[745,973], [2442,2906], [7430,7865]]

start_index = 7430
end_index = 7865

no_hours = end_index - start_index + 1

start_time = time_list[start_index]
end_time = time_list[end_index]

start_delta = I[0,start_index]
end_delta = I[0,end_index]

average_LE = np.mean(I[2,start_index:end_index])
increase_delta = (end_delta - start_delta) / no_hours

time = []

for i in range(len(time_list)):
    time.append(datetime.datetime.strptime(time_list[i], '%Y-%m-%d %H:%M:%S'))

time_months = [time[373], time[1081], time[1789], time[2521], time[3253], time[3985], time[4717], time[5461], time[6193], time[6925], time[7657], time[8389]]

test_month = 8760

# graphs for 1 year

def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

fig, ax1 = plt.subplots()

fig.set_figwidth(10)

fig.subplots_adjust(right=0.75)

ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax4 = ax1.twinx()

ax2.spines["right"].set_position(("axes", 1.2))
make_patch_spines_invisible(ax2)
ax2.spines["right"].set_visible(True)

ax4.spines["right"].set_position(("axes", 1.4))
make_patch_spines_invisible(ax4)
ax4.spines["right"].set_visible(True)

p2, = ax2.plot(time[:test_month], I[2,:]*-1, color='purple')
p1, = ax1.plot(time[:test_month], I[0,:], color='k', label = 'with fractionation')
p4, = ax1.plot(time[:test_month], I[1,:], color='blue', label = 'without fractionation')
p3, = ax3.plot(time[:test_month], I[3,:], color='dimgrey')
p5, = ax4.plot(time_months, I[5,0:12], color = 'darkgreen')

ax1.set_xlabel("Time", size=16)
ax1.set_ylabel('\u03B4$^{18}O$ of surface snow (\u2030 vs VSMOW)', size=16)
ax2.set_ylabel('Sublimation mass flux (kg/m$^2$h)', size=16)
ax3.set_ylabel("Mass of accumulated snowfall (kg/m$^2$)", size=16)
ax4.set_ylabel("Average monthly air temperature (K)", size=16)

ax1.yaxis.label.set_color(p1.get_color())
ax2.yaxis.label.set_color(p2.get_color())
ax3.yaxis.label.set_color(p3.get_color())
ax4.yaxis.label.set_color(p5.get_color())

tkw = dict(size=4, width=1.5)
ax1.tick_params(axis='y', colors=p1.get_color(), **tkw)
ax2.tick_params(axis='y', colors=p2.get_color(), **tkw)
ax3.tick_params(axis='y', colors=p3.get_color(), **tkw)
ax4.tick_params(axis='y', colors=p5.get_color(), **tkw)
ax1.tick_params(axis='x', **tkw)

ax3.grid()

ax1.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)

ax3.yaxis.set_major_locator(ticker.MultipleLocator(3.5))

months = md.MonthLocator()
format_ =  md.DateFormatter('%b')

ax1.xaxis.set_major_locator(months)
ax1.xaxis.set_major_formatter(format_)

ax1.set_zorder(ax3.get_zorder() + 1)
ax1.patch.set_visible(False)

ax3.set_zorder(ax2.get_zorder() + 1)
ax3.patch.set_visible(False)

ax4.set_zorder(ax1.get_zorder() + 1)
ax4.patch.set_visible(False)

plt.tight_layout()

Figures_paths = '/home/riqo/Figures/'

plt.savefig(Figures_paths + 'Figure3')