import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import rcParams
from scipy.special import softmax

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

logits = np.array([2.5, -3.0, 0.6])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_axisbelow(True)

plt.grid(alpha=0.35, linewidth=1, zorder=0)
plt.bar(np.arange(3), logits, color='#EA6B66', edgecolor='black', linewidth=2)

#plt.xlabel(r'Index')
#plt.ylabel(r'Softmax inputs $a_i$')

plt.box(on=True)
plt.tight_layout()
plt.savefig('softmax_1.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_axisbelow(True)

plt.grid(alpha=0.35, linewidth=1, zorder=0)
plt.bar(np.arange(3), softmax(logits), color='#7EA6E0', edgecolor='black', linewidth=2)

plt.ylim([0, 1.0])

#plt.xlabel(r'Output index $i$')
#plt.ylabel(r'Softmax outputs (temperature=1)')

plt.box(on=True)
plt.tight_layout()
plt.savefig('softmax_2.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_axisbelow(True)

plt.grid(alpha=0.35, linewidth=1, zorder=0)
plt.bar(np.arange(3), softmax(logits/10), color='#7EA6E0', edgecolor='black', linewidth=2)

plt.ylim([0, 1.0])

#plt.xlabel(r'Output index $i$')
#plt.ylabel(r'Softmax outputs (temperature=10)')

plt.box(on=True)
plt.tight_layout()
plt.savefig('softmax_3.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_axisbelow(True)

plt.bar(np.arange(3), softmax(logits/100), color='#7EA6E0', edgecolor='black', linewidth=2)
plt.grid(alpha=0.35, linewidth=1, zorder=0)

plt.ylim([0, 1.0])

#plt.xlabel(r'Output index $i$')
#plt.ylabel(r'Softmax outputs (temperature=100)')

plt.box(on=True)
plt.tight_layout()
plt.savefig('softmax_4.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()