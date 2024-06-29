import allele_age_utils
from allele_age_utils import *

comparison = np.loadtxt("results/singer_ts/allele_singer_300.txt", delimiter=',')
plot_hexbin_plot(comparison[:, 1], comparison[:, 2], 0.5, 5.5, 3e3, "results/figures/allele_singer_300.png") 
