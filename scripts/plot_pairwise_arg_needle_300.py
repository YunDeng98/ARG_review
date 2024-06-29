import pairwise_utils
from pairwise_utils import *

comparison = np.loadtxt("results/arg_needle_ts/pairwise_arg_needle_300.txt", delimiter=',')
plot_hexbin_plot(comparison[:, 0], comparison[:, 1], 2.5, 5.5, 5e4, "results/figures/pairwise_arg_needle_300.png") 
