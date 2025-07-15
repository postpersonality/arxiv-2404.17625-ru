import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import rcParams
from scipy.special import expit

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

# First plot: sigmoid with several slopes
x_plot = np.linspace(-10, 5, 1000)

fig, ax = plt.subplots(1,1)

plt.plot(x_plot, 0.6*expit(0.1*(x_plot + 3.0)), label='w=0.1', color=colors[0])
plt.plot(x_plot, 0.6*expit(x_plot + 3.0), label='w=1', color=colors[1])
plt.plot(x_plot, 0.6*expit(5.0*(x_plot + 3.0)), label='w=5', color=colors[2])
plt.vlines(-3.0, 0, 0.7, '0.6', linestyles='dashed', linewidth=0.5)
plt.hlines(0.6, -10, 5, 'black', linestyles='dashed', linewidth=0.5)

plt.xlabel('$x$')
plt.ylabel('$a\sigma(w(x - s))$')

# Add ticks
ax.set_xticks([-9, -6, -3.0, 0, 3])
ax.set_xticklabels(["", "", "$s$", "", ""])
ax.set_yticks([0.2,0.4,0.6])
ax.set_yticklabels(["", "", "$a$"])

leg = plt.legend(loc='upper center', ncol=3)
fr = leg.get_frame()
fr.set_lw(0.5)

plt.grid(alpha=0.35, linewidth=1, zorder=0)
plt.box(on=True)
plt.tight_layout()
plt.savefig('tunable_sigmoid.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()

x_plot = np.linspace(0, 1, 1000)

w = 1000

def get_bin(bin_center, bin_width, bin_amplitude):
    
   h1 = expit(w*x_plot - w*(bin_center-bin_width/2))
   h2 = expit(w*x_plot - w*(bin_center + bin_width/2))
   y = bin_amplitude*h1 - bin_amplitude*h2
   return h1, h2, y

h11, h12, y1 = get_bin(0.3, 0.1, 0.8)
h21, h22, y2 = get_bin(0.7, 0.2, -0.4)

# Second plot: step function

plt.figure()

plt.plot(x_plot, h11, color=colors[0])

plt.xlabel('$x$')
plt.ylabel('Output')

plt.grid(alpha=0.35, linewidth=1, zorder=0)
plt.box(on=True)
plt.tight_layout()
plt.savefig('step_function.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()

plt.figure()

plt.plot(x_plot, y1, color=colors[0])

plt.xlabel('$x$')
plt.ylabel('Output')

plt.grid(alpha=0.35, linewidth=1, zorder=0)
plt.box(on=True)
plt.tight_layout()
plt.savefig('bin.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()

plt.plot(x_plot, y1+y2, color=colors[0])

plt.xlabel('$x$')
plt.ylabel('Output')

plt.grid(alpha=0.35, linewidth=1, zorder=0)
plt.box(on=True)
plt.tight_layout()
plt.savefig('bin_2.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()


x_plot = np.linspace(0, 10, 1000)
y_true = np.sin(x_plot)/x_plot

bins = 15
x_bin = np.linspace(0, 10, bins)
width = x_bin[1] - x_bin[0]

y = np.zeros(1000)

for i in range(bins - 1):
   _, _, y_bin = get_bin((x_bin[i+1] + x_bin[i])/2, width, 
                         (y_true[(x_plot > x_bin[i]) & (x_plot < x_bin[i+1])].mean()))
   y = y + y_bin

# Plot fix
y[0] = y_true[0]
y[-1] = y_true[-1]

plt.figure()

plt.plot(x_plot, y_true, color=colors[0])
plt.plot(x_plot, y, color=colors[1])

plt.xlabel('$x$')
plt.ylabel('Output')

plt.grid(alpha=0.35, linewidth=1, zorder=0)
plt.box(on=True)
plt.tight_layout()
plt.savefig(f'sin_approximation_{bins}.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()

print(f'MSE: {((y_true[1:] - y[1:])**2).mean()}')
