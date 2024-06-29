import pairwise_utils
from pairwise_utils import *

comparison = np.loadtxt("results/argweaver_ts/pairwise_argweaver_50.txt", delimiter=',')
plot_hexbin_plot(comparison[:, 0], comparison[:, 1], 2.5, 5.5, 5e4, "results/figures/pairwise_argweaver_50.png") 
