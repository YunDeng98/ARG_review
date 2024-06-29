import bar_plot_utils
from bar_plot_utils import *
import topology_utils
from topology_utils import * 


comparison_singer_50 = np.loadtxt("results/singer_ts/triplet_singer_50.txt", delimiter=',')
comparison_argweaver_50 = np.loadtxt("results/argweaver_ts/triplet_argweaver_50.txt", delimiter=',')
comparison_relate_50 = np.loadtxt("results/relate_ts/triplet_relate_50.txt", delimiter=',')
comparison_tsdate_tsinfer_50 = np.loadtxt("results/tsdate_tsinfer_ts/triplet_tsdate_tsinfer_50.txt", delimiter=',')
comparison_singer_300 = np.loadtxt("results/singer_ts/triplet_singer_300.txt", delimiter=',')
comparison_arg_needle_300 = np.loadtxt("results/arg_needle_ts/triplet_arg_needle_300.txt", delimiter=',')
comparison_relate_300 = np.loadtxt("results/relate_ts/triplet_relate_300.txt", delimiter=',')
comparison_tsdate_tsinfer_300 = np.loadtxt("results/tsdate_tsinfer_ts/triplet_tsdate_tsinfer_300.txt", delimiter=',')
error_singer_50 = error_proportion(comparison_singer_50[:, 0], comparison_singer_50[:, 1])
error_argweaver_50 = error_proportion(comparison_argweaver_50[:, 0], comparison_argweaver_50[:, 1])
error_relate_50 = error_proportion(comparison_relate_50[:, 0], comparison_relate_50[:, 1])
error_tsdate_tsinfer_50 = error_proportion(comparison_tsdate_tsinfer_50[:, 0], comparison_tsdate_tsinfer_50[:, 1])
error_singer_300 = error_proportion(comparison_singer_300[:, 0], comparison_singer_300[:, 1])
error_arg_needle_300 = error_proportion(comparison_arg_needle_300[:, 0], comparison_arg_needle_300[:, 1])
error_relate_300 = error_proportion(comparison_relate_300[:, 0], comparison_relate_300[:, 1])
error_tsdate_tsinfer_300 = error_proportion(comparison_tsdate_tsinfer_300[:, 0], comparison_tsdate_tsinfer_300[:, 1])
error_50 = [error_singer_50, error_argweaver_50, error_relate_50, error_tsdate_tsinfer_50]
error_300 = [error_singer_300, error_arg_needle_300, error_relate_300, error_tsdate_tsinfer_300]
methods_50 = ["SINGER", "ARGweaver", "Relate", "tsinfer+tsdate"]
methods_300 = ["SINGER", "ARG-Needle", "Relate", "tsinfer+tsdate"]
colors_50 = ["red", "purple", "green", "blue"]
colors_300 = ["red", "brown", "green", "blue"]
plot_bar_plot(error_50, error_300, methods_50, methods_300, colors_50, colors_300, 0.8, "results/figures/triplet_error.png") 
