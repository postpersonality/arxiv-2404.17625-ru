
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
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

colors = ['#B85450', '#82B366', '#6C8EBF']

np.random.seed(1)

x = np.arange(-10, 10, 0.01)
y = x**3

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(x, y, color=colors[0])
plt.plot((0), (0), 'o', color=colors[0], markersize=8)

ax.annotate('Saddle point \n (neither minimum \n nor maximum)', xy=(0.3, -50), xytext=(2, -700),
    arrowprops=dict(facecolor='black', width=1, headwidth=8, headlength=5, shrink=0.15),
)

#plt.xlim([1, 8])

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')

ax.get_xaxis().set_ticklabels([])
ax.get_yaxis().set_ticklabels([])
#leg = plt.legend(loc='upper right')
#fr = leg.get_frame()
#fr.set_lw(0.5)

plt.grid(alpha=0.35, linewidth=1)
plt.box(on=True)
plt.tight_layout()
plt.savefig('saddle_point.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()