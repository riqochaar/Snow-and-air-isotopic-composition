# This file was used to produce Figure 6


from mpl_toolkits import basemap as bm
from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np
import pandas as pd
import numpy.ma as ma
import matplotlib.gridspec as gridspec

D0 = pd.read_pickle('/home/riqo/surface_snow_files/average_values_january')
D1 = pd.read_pickle('/home/riqo/surface_snow_files/average_values_february')
D2 = pd.read_pickle('/home/riqo/surface_snow_files/average_values_june')
D3 = pd.read_pickle('/home/riqo/surface_snow_files/average_values_october')

round_O = np.around(D1['LE']/5, decimals=0)*5

##some fake data
lat = D1['latitude'][:]
lon = np.hstack((D1['longitude'], D1['longitude'][:1]))
lon, lat = np.meshgrid(lon, lat)

LE0 = np.hstack((D0['LE']*-1, D0['LE'][:,:1]*-1))
LE1 = np.hstack((D1['LE']*-1, D1['LE'][:,:1]*-1))
LE2 = np.hstack((D2['LE']*-1, D2['LE'][:,:1]*-1))
LE3 = np.hstack((D3['LE']*-1, D3['LE'][:,:1]*-1))

most_northern_point = 100

minimum = min(
          np.nanmin(D0['LE'][most_northern_point:,:]), np.nanmin(D1['LE'][most_northern_point:,:]),
          np.nanmin(D2['LE'][most_northern_point:,:]), np.nanmin(D3['LE'][most_northern_point:,:])
)

maximum = max(
          np.nanmax(D0['LE'][most_northern_point:,:][np.nonzero(D0['LE'][most_northern_point:,:])]),
          np.nanmax(D1['LE'][most_northern_point:,:][np.nonzero(D1['LE'][most_northern_point:,:])]),
          np.nanmax(D2['LE'][most_northern_point:,:][np.nonzero(D2['LE'][most_northern_point:,:])]),
          np.nanmax(D3['LE'][most_northern_point:,:][np.nonzero(D3['LE'][most_northern_point:,:])])
)

rounded_minimum = 0.0001
rounded_maximum = 0.1

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6,6))

axes[0,0].set_title('January')
m = bm.Basemap(projection='spstere', boundinglat=-65, lon_0=180, resolution='l', ax = axes[0,0])
m.drawcoastlines(linewidth=0.5)

axes[0,1].set_title('February')
m = bm.Basemap(projection='spstere', boundinglat=-65, lon_0=180, resolution='l', ax = axes[0,1])
m.drawcoastlines(linewidth=0.5)

axes[1,0].set_title('June')
m = bm.Basemap(projection='spstere', boundinglat=-65, lon_0=180, resolution='l', ax = axes[1,0])
m.drawcoastlines(linewidth=0.5)

axes[1,1].set_title('October')
m = bm.Basemap(projection='spstere', boundinglat=-65, lon_0=180, resolution='l', ax = axes[1,1])
m.drawcoastlines(linewidth=0.5)

x,y = m(lon,lat)

pcol0 = axes[0,0].pcolormesh(x, y, LE0, cmap='viridis', vmin = rounded_minimum, vmax = rounded_maximum)
pcol1 = axes[0,1].pcolormesh(x, y, LE1, cmap='viridis', vmin = rounded_minimum, vmax = rounded_maximum)
pcol2 = axes[1,0].pcolormesh(x, y, LE2, cmap='viridis', vmin = rounded_minimum, vmax = rounded_maximum)
pcol3 = axes[1,1].pcolormesh(x, y, LE3, cmap='viridis', vmin = rounded_minimum, vmax = rounded_maximum)

Figures_paths = '/home/riqo/Figures/'

plt.savefig(Figures_paths + 'Figure6')

plt.show()


