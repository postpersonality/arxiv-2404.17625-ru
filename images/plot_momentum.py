
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

x = np.linspace(0.5, 3, 1000)
f = lambda x: x*np.sin(2*x)
y = f(x)

dy = lambda x: 2*x*np.cos(2*x) + np.sin(2*x)

x_gd = [1.1]
for i in range(10):
    x_gd.append(x_gd[-1] - 0.05*dy(x_gd[-1]))

x_mgd = [1.1]
m = 0
for i in range(10):
    m = - 0.05*dy(x_mgd[-1]) + 0.3*m
    x_mgd.append(x_mgd[-1] + m)

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(x, y, color=colors[0])
for i, x in enumerate(x_gd):
    if i== 9:
        plt.plot(x, f(x), 'o', markersize=8, markeredgecolor='black', 
                color=colors[1], alpha=np.minimum(1, 0.09*(i+1)), label='Standard GD')
    else:
        plt.plot(x, f(x), 'o', markersize=8, markeredgecolor='black', 
                color=colors[1], alpha=np.minimum(1, 0.09*(i+1)))
for i, x in enumerate(x_mgd):
    if i== 9:
        plt.plot(x, f(x), 'd', markersize=8, markeredgecolor='black', 
                color=colors[2], alpha=np.minimum(1, 0.09*(i+1)), label='Momentum GD')
    else:
        plt.plot(x, f(x), 'd', markersize=8, markeredgecolor='black', 
            color=colors[2], alpha=np.minimum(1, 0.09*(i+1)))
    
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')

leg = plt.legend(loc='upper right', markerscale=0.6)
fr = leg.get_frame()
fr.set_lw(0.5)

plt.grid(alpha=0.35, linewidth=1)
plt.box(on=True)
plt.tight_layout()
plt.savefig('momentum.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()