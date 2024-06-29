import pairwise_utils
from pairwise_utils import *

comparison = np.loadtxt("results/relate_ts/pairwise_relate_50.txt", delimiter=',')
plot_hexbin_plot(comparison[:, 0], comparison[:, 1], 2.5, 5.5, 5e4, "results/figures/pairwise_relate_50.png") 
