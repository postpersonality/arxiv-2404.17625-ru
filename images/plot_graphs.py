import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import rcParams
from scipy.stats import norm
import networkx as nx

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

colors = ['#B85450', '#EA6B66', '#DAE8FC']

np.random.seed(1)

G1 = nx.erdos_renyi_graph(50, 0.1, seed=5, directed=False)
nx.draw(G1, node_size=50, node_color=colors[2], linewidths=1, edgecolors='black')

plt.tight_layout()
plt.savefig('graph_1.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()

degree_sequence = sorted((d for n, d in G1.degree()), reverse=True)
dmax = max(degree_sequence)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.bar(*np.unique(degree_sequence, return_counts=True), 
       width=0.5, facecolor=colors[1], edgecolor='black', linewidth=1.5)
ax.set_xlabel("Degree")
ax.set_ylabel("Nodes")

plt.grid(alpha=0.35, linewidth=1, zorder=0)
plt.box(on=True)
plt.tight_layout()
plt.savefig('graph_1_degree.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()

G2 = nx.barabasi_albert_graph(50, 3, seed=5)
nx.draw(G2, node_size=50, node_color=colors[2], linewidths=1, edgecolors='black')

plt.tight_layout()
plt.savefig('graph_2.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()

degree_sequence = sorted((d for n, d in G2.degree()), reverse=True)
dmax = max(degree_sequence)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.bar(*np.unique(degree_sequence, return_counts=True), 
       width=0.5, facecolor=colors[1], edgecolor='black', linewidth=1.5)
ax.set_xlabel("Degree")
ax.set_ylabel("Nodes")

plt.grid(alpha=0.35, linewidth=1, zorder=0)
plt.box(on=True)
plt.tight_layout()
plt.savefig('graph_2_degree.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()