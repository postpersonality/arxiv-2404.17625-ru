import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import rcParams
import brewer2mpl
from scipy.stats import norm

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

colors = ['#B85450', '#EA6B66', '#666666']

np.random.seed(1)

x = np.arange(-3, 3, 0.01)
y_relu = np.maximum(x, 0)
y_softplus = np.log(1 + np.exp(x))
y_leakyrelu = y_relu + 0.1*np.minimum(x, 0)
y_elu = (x >= 0.0) * x + (x < 0.0) * (np.exp(x) - 1.0)
y_gelu = norm.cdf(x)*x


def plot_af(x, y, name):
   plt.figure()
   plt.plot(x, y, label=name, color=colors[0])

   plt.xlim((-3, 2.5))
   plt.ylim((-1.5, 3+0.1))

   plt.grid(alpha=0.35, linewidth=1, zorder=0)
   plt.box(on=True)
   plt.tight_layout()
   plt.savefig(f'activation_function_{name}.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
   plt.show()

plot_af(x, y_relu, 'ReLU')
plot_af(x, y_softplus, 'Softplus')
plot_af(x, y_leakyrelu, 'LeakyReLU')
plot_af(x, y_elu, 'ELU')
plot_af(x, y_gelu, 'GELU')