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

X = np.random.randn(10, 5)
y = X @ np.random.randn(5, 1) # Linear model with unknown coefficients

w = np.random.randn(5, 1)
yhat = X @ w # (10, 1)

loss = []
for i in range(1000):
  loss.append(((y - X @ w)**2).mean())
  w = w + 0.001 * X.T @ (y - X @ w)

plt.figure()

plt.plot(loss, color=colors[0])

plt.xlabel('Iteration')
plt.ylabel('Loss')

#leg = plt.legend(loc='upper right')
#fr = leg.get_frame()
#fr.set_lw(0.5)

plt.grid(alpha=0.35, linewidth=1)
plt.box(on=True)
plt.tight_layout()
plt.savefig('least_squares_example.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()