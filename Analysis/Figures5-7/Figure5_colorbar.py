# This file was used to produce the colorbar for Figure 5

# The colorbar was produced separately due to formatting problems

# An edited version of the same file was used to produce the colorbars for Figures 6, 7 and 10


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

fig, axs = plt.subplots(nrows=2, ncols=2, figsize = (6,6))

cm = ['viridis', 'viridis']
for col in range(2):
    for row in range(2):
        ax = axs[row, col]
        ax.set_title('A')
        pcm = ax.pcolormesh(np.random.random((20, 20)) * (col + 1),
                            cmap=cm[col], vmin = 0.0001, vmax = 0.1)
    x = fig.colorbar(pcm, ax=axs[:, col])
    x.set_label(label='\u03B4$^{18}$O of surface snow (\u2030 vs VSMOW)', size='16')

Figures_paths = '/home/riqo/Figures'

plt.savefig(Figures_paths + 'Figure5_colorbar', bbox_inches='tight', pad_inches=0)

plt.show()