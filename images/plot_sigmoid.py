import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib.patheffects as pe

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
y = 1.0/(1.0+np.exp(-x))
     
y_derivative = y * (1 - y)

plt.figure()

plt.plot(x, y, color=colors[0])

plt.xlabel('$s$')
plt.ylabel('Sigmoid $\sigma(s)$')

plt.ylim((0-0.1, 1+0.1))

#leg = plt.legend(loc='upper right')
#fr = leg.get_frame()
#fr.set_lw(0.5)

plt.grid(alpha=0.35, linewidth=1)
plt.box(on=True)
plt.tight_layout()
plt.savefig('sigmoid.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()

plt.figure()

plt.plot(x, y, color=colors[0], label='$\sigma(s)$')
plt.plot(x, y_derivative, '--', color=colors[1], label='$\sigma\'(s)$')
plt.xlabel('$s$')
plt.ylabel('Sigmoid and its derivative')

plt.ylim((0-0.1, 1+0.1))

leg = plt.legend(loc='upper left')
fr = leg.get_frame()
fr.set_lw(0.5)

plt.grid(alpha=0.35, linewidth=1)
plt.box(on=True)
plt.tight_layout()
plt.savefig('sigmoid_and_derivative.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()