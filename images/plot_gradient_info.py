
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

colors_draw = ['#B85450', '#82B366', '#6C8EBF']

np.random.seed(1)

x = np.arange(-4, 10, 0.01)
y = x**2 - 1.5*x

dy = 2*x - 1.5

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(x, y, color=colors_draw[0])
plt.plot((-2, 4), (7, 10), 'o', color=colors_draw[0])

ax.annotate(r'$\displaystyle\partial f(x) < 0$', xy=(-2, 7), xytext=(0, 30),
    arrowprops=dict(facecolor='black', width=1, headwidth=8, headlength=5, shrink=0.15),
)

y_tan = -5.5 * (x + 2.0) + 7
plt.plot(x, y_tan, '--r', alpha=0.9, color=colors_draw[1], zorder=-1)

ax.annotate(r'$\displaystyle\partial f(x) > 0$', xy=(4, 10), xytext=(6, -2),
    arrowprops=dict(facecolor='black', width=1, headwidth=8, headlength=5, shrink=0.15),
)

y_tan = 6.5 * (x - 4.0) + 10
plt.plot(x, y_tan, '--', alpha=0.9, color=colors_draw[1], zorder=-1)

plt.xlim([-4, 10])
plt.ylim([-15, 85])

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')

#leg = plt.legend(loc='upper right')
#fr = leg.get_frame()
#fr.set_lw(0.5)

plt.grid(alpha=0.35, linewidth=1)
plt.box(on=True)
plt.tight_layout()
plt.savefig('gradient_info.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()