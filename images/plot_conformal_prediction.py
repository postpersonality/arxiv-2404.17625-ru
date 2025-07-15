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

colors = ['#DAE8FC', '#EA6B66', '#666666']

np.random.seed(1)

logits = np.asarray([0.05, 0.1, 0.4, 0.08, 0.3, 0.02, 0.05])
threshold = 0.2
idx = [2, 4]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_axisbelow(True)

plt.bar(range(len(logits)), logits, width=0.8, facecolor=colors[0], 
        edgecolor='black', linewidth=1.5, alpha=0.4)
plt.bar(np.arange(len(logits))[idx], logits[idx], width=0.8, facecolor=colors[1], 
        edgecolor='black', linewidth=1.5, label='Selected classes')
plt.hlines(threshold, 0, len(logits), color=colors[2], linestyles='dashed', label='Threshold')

plt.xlabel('Class')
plt.ylabel('Confidence')

leg = plt.legend(loc='upper right')
fr = leg.get_frame()
fr.set_lw(0.5)

plt.grid(alpha=0.35, linewidth=1, zorder=0)
plt.box(on=True)
plt.tight_layout()
plt.savefig('conformal_prediction.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()