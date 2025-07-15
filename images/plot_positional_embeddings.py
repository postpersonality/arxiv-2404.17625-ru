
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
from pylab import rcParams

np.random.seed(1)

font_size = 9

matplotlib.use('Qt5Agg')

# Set parameters for plotting
params = {
   'axes.labelsize': font_size,
   'axes.linewidth': 1,
   'font.size': font_size,
   'legend.fontsize': font_size-2,
   'xtick.labelsize': font_size,
   'xtick.major.size': 2,
   'ytick.labelsize': font_size,
   'ytick.major.size': 2,
   'text.usetex': True,
   'figure.figsize': [4*0.9,3*0.9],
}
rcParams.update(params)

colors_draw = ['#B85450', '#82B366', '#6C8EBF']

np.random.seed(1)

fig = plt.figure()

x = np.linspace(0, 10, 1000)
omega = [0.1, 1, 10]

y = [np.sin(w*x) for w in omega]

fig, ax = plt.subplots(3, 1,sharex=True, sharey=True)

ax[0].plot(x, y[0], color='gray', alpha=0.5)
ax[1].plot(x, y[1], color='gray', alpha=0.5)
ax[2].plot(x, y[2], color='gray', alpha=0.5)

x_i = 6

con = ConnectionPatch(xyA = (x_i, -1), xyB=(x_i, 1), coordsA="data", coordsB="data",
                      axesA=ax[2], axesB=ax[0], color=colors_draw[0], linewidth=2, linestyle='dashed', 
                      zorder=10, alpha=0.7)
ax[2].add_artist(con)

ax[0].plot(x_i, np.sin(omega[0]*x_i), 'o', color=colors_draw[0], markeredgecolor='black', markersize=6)
ax[1].plot(x_i, np.sin(omega[1]*x_i), 'o', color=colors_draw[0], markeredgecolor='black', markersize=6)
ax[2].plot(x_i, np.sin(omega[2]*x_i), 'o', color=colors_draw[0], markeredgecolor='black', markersize=6)

plt.box(on=True)
ax[0].grid(alpha=0.35, linewidth=1, zorder=0)
ax[1].grid(alpha=0.35, linewidth=1, zorder=0)
ax[2].grid(alpha=0.35, linewidth=1, zorder=0)

ax[0].set_ylabel('$\sin(0.1x)$')
ax[1].set_ylabel('$\sin(1x)$')
ax[2].set_ylabel('$\sin(10x)$')

plt.tight_layout()

plt.savefig('positional_embeddings.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()
