import pairwise_utils
from pairwise_utils import *

comparison = np.loadtxt("results/tsdate_tsinfer_ts/pairwise_tsdate_tsinfer_300.txt", delimiter=',')
plot_hexbin_plot(comparison[:, 0], comparison[:, 1], 2.5, 5.5, 5e4, "results/figures/pairwise_tsdate_tsinfer_300.png") 
