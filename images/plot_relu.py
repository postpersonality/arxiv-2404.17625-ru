
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
import brewer2mpl

np.random.seed(1)

font_size = 9

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

x = np.arange(-3, 3, 0.01)
y = np.maximum(0, x)
     
y_derivative = y > 0

plt.figure()

plt.plot(x, y, color=colors[0], label='ReLU(s)')
plt.plot(x, y_derivative, '--', color=colors[1], label='Derivative of ReLU(s)')
plt.xlabel('$s$')
plt.ylabel('ReLU and its derivative')

plt.ylim((0-0.1, 3+0.1))

plt.legend(loc=0)
plt.grid(color="0.9", linestyle='--', linewidth=1)
plt.box(on=True)
plt.tight_layout()

plt.savefig('relu_and_derivative.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()