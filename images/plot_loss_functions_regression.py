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

# Error sampling
e = np.arange(-2, 2.1, 0.1)

huber_loss = np.zeros_like(e)
huber_loss[np.abs(e) <= 1.5] = 0.5*e[np.abs(e) <= 1.5]**2
huber_loss[np.abs(e) > 1.5] = 1.5*(np.abs(e[np.abs(e) > 1.5]) - 0.5*1.5)

plt.figure()

plt.plot(e, e**2, '-*', color=colors[0], label='Squared loss', 
         markersize=6, markevery=5)
plt.plot(e, np.abs(e), '-o', color=colors[1], label='Absolute loss', 
         markersize=6, markevery=5)
#plt.plot(e, np.maximum(0, np.abs(e) - 0.5), color=colors[2], label='0.5-insensitive loss')
plt.plot(e, huber_loss, '-d', color=colors[2], label='Huber loss ($\delta=1.5$)', 
         markersize=6, markevery=5)

plt.xlabel('$e$')
plt.ylabel('$L(e)$')

leg = plt.legend(loc='upper center')
fr = leg.get_frame()
fr.set_lw(0.5)

plt.grid(alpha=0.35, linewidth=1)
plt.box(on=True)
plt.tight_layout()
plt.savefig('loss_functions_regression.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()