
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

f = lambda x: x**2 - 1.5*x
df = lambda x: 2*x - 1.5

x = 0.5
f_linearized = lambda h: f(x) + df(x)*(h - x)

print(f(x + 0.01))
print(f_linearized(x + 0.01))

xrange = np.linspace(-1, 1, 100)

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(xrange, f(xrange), color=colors[1], label='f(x)')
plt.plot(xrange, f_linearized(xrange), '--', color=colors[0], label='Linearized at 0.5')

ax.fill_between(xrange, f(xrange), f_linearized(xrange), facecolor='gray', alpha=0.1, interpolate=True)

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')

leg = plt.legend(loc='upper right')
fr = leg.get_frame()
fr.set_lw(0.5)

plt.grid(alpha=0.35, linewidth=1)
plt.box(on=True)
plt.tight_layout()
plt.savefig('taylor_approximation.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()