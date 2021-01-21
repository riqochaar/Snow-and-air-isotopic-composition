# This file was used to produce Figure 7

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

round_O = np.around(D1['t2m']/5, decimals=0)*5

##some fake data
lat = D1['latitude'][:]
lon = np.hstack((D1['longitude'], D1['longitude'][:1]))
lon, lat = np.meshgrid(lon, lat)

t2m0 = np.hstack((D0['t2m'], D0['t2m'][:,:1]))
t2m1 = np.hstack((D1['t2m'], D1['t2m'][:,:1]))
t2m2 = np.hstack((D2['t2m'], D2['t2m'][:,:1]))
t2m3 = np.hstack((D3['t2m'], D3['t2m'][:,:1]))

most_northern_point = 133

minimum = min(
          np.nanmin(D0['t2m'][most_northern_point:,:]), np.nanmin(D1['t2m'][most_northern_point:,:]),
          np.nanmin(D2['t2m'][most_northern_point:,:]), np.nanmin(D3['t2m'][most_northern_point:,:])
)

maximum = max(
          np.nanmax(D0['t2m'][most_northern_point:,:][np.nonzero(D0['t2m'][most_northern_point:,:])]),
          np.nanmax(D1['t2m'][most_northern_point:,:][np.nonzero(D1['t2m'][most_northern_point:,:])]),
          np.nanmax(D2['t2m'][most_northern_point:,:][np.nonzero(D2['t2m'][most_northern_point:,:])]),
          np.nanmax(D3['t2m'][most_northern_point:,:][np.nonzero(D3['t2m'][most_northern_point:,:])])
)

rounded_minimum = np.around(minimum/5, decimals=0)*5
rounded_maximum = np.around(maximum/5, decimals=0)*5

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

pcol0 = axes[0,0].pcolormesh(x, y, t2m0, cmap='viridis', vmin = rounded_minimum, vmax = rounded_maximum)
pcol1 = axes[0,1].pcolormesh(x, y, t2m1, cmap='viridis', vmin = rounded_minimum, vmax = rounded_maximum)
pcol2 = axes[1,0].pcolormesh(x, y, t2m2, cmap='viridis', vmin = rounded_minimum, vmax = rounded_maximum)
pcol3 = axes[1,1].pcolormesh(x, y, t2m3, cmap='viridis', vmin = rounded_minimum, vmax = rounded_maximum)

##producing a mask -- seems to only work with full coordinate limits
lons2 = np.linspace(-180,180,10000)
lats2 = np.linspace(-90,90,5000)
lon2, lat2 = np.meshgrid(lons2,lats2)
x2,y2 = m(lon2,lat2)
pseudo_data = np.ones_like(lon2)
masked = bm.maskoceans(lon2,lat2,pseudo_data)
masked.mask = ~masked.mask

##plotting the mask
cmap = colors.ListedColormap(['w'])
pcol0 = axes[0,0].pcolormesh(x2, y2, masked, cmap=cmap)
pcol1 = axes[0,1].pcolormesh(x2, y2, masked, cmap=cmap)
pcol2 = axes[1,0].pcolormesh(x2, y2, masked, cmap=cmap)
pcol3 = axes[1,1].pcolormesh(x2, y2, masked, cmap=cmap)

#fig.subplots_adjust(wspace=0.1, hspace=0.1)

Figures_paths = '/home/riqo/Figures/'

plt.savefig(Figures_paths + 'Figure7', bbox_inches='tight', pad_inches=0)

plt.show()


