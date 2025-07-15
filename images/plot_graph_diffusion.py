import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
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

import numpy as np

colors = ['white', colors[0]]
cm = LinearSegmentedColormap.from_list(
        "Custom", colors, N=10)

np.random.seed(1)

n = 15

node_features = np.random.rand(n)

G = nx.erdos_renyi_graph(n, 0.2, seed=1, directed=False)
A = nx.laplacian_matrix(G)

nx.draw(G, node_size=300, node_color=node_features, linewidths=1, edgecolors='black', cmap=cm, 
               pos=nx.spring_layout(G, seed=1))

plt.tight_layout()
plt.savefig('graph_diffusion_0.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
plt.show()

for i in range(50):

       node_features = node_features @ A

       if i % 10 == 0:

              nx.draw(G, node_size=300, node_color=node_features, linewidths=1, edgecolors='black', cmap=cm, 
                     pos=nx.spring_layout(G, seed=1))

              plt.tight_layout()
              plt.savefig(f'graph_diffusion_{i}.pdf', format='pdf',bbox_inches='tight', pad_inches=0.01)
              plt.show()