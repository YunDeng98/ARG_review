import bar_plot_utils
from bar_plot_utils import *
import pairwise_utils
from pairwise_utils import * 


comparison_singer_50 = np.loadtxt("results/singer_ts/pairwise_singer_50.txt", delimiter=',')
comparison_argweaver_50 = np.loadtxt("results/argweaver_ts/pairwise_argweaver_50.txt", delimiter=',')
comparison_relate_50 = np.loadtxt("results/relate_ts/pairwise_relate_50.txt", delimiter=',')
comparison_tsdate_tsinfer_50 = np.loadtxt("results/tsdate_tsinfer_ts/pairwise_tsdate_tsinfer_50.txt", delimiter=',')
comparison_singer_300 = np.loadtxt("results/singer_ts/pairwise_singer_300.txt", delimiter=',')
comparison_arg_needle_300 = np.loadtxt("results/arg_needle_ts/pairwise_arg_needle_300.txt", delimiter=',')
comparison_relate_300 = np.loadtxt("results/relate_ts/pairwise_relate_300.txt", delimiter=',')
comparison_tsdate_tsinfer_300 = np.loadtxt("results/tsdate_tsinfer_ts/pairwise_tsdate_tsinfer_300.txt", delimiter=',')
mse_singer_50 = mse(comparison_singer_50[:, 0], comparison_singer_50[:, 1])/4e8
mse_argweaver_50 = mse(comparison_argweaver_50[:, 0], comparison_argweaver_50[:, 1])/4e8
mse_relate_50 = mse(comparison_relate_50[:, 0], comparison_relate_50[:, 1])/4e8
mse_tsdate_tsinfer_50 = mse(comparison_tsdate_tsinfer_50[:, 0], comparison_tsdate_tsinfer_50[:, 1])/4e8
mse_singer_300 = mse(comparison_singer_300[:, 0], comparison_singer_300[:, 1])/4e8
mse_arg_needle_300 = mse(comparison_arg_needle_300[:, 0], comparison_arg_needle_300[:, 1])/4e8
mse_relate_300 = mse(comparison_relate_300[:, 0], comparison_relate_300[:, 1])/4e8
mse_tsdate_tsinfer_300 = mse(comparison_tsdate_tsinfer_300[:, 0], comparison_tsdate_tsinfer_300[:, 1])/4e8
mse_50 = [mse_singer_50, mse_argweaver_50, mse_relate_50, mse_tsdate_tsinfer_50]
mse_300 = [mse_singer_300, mse_arg_needle_300, mse_relate_300, mse_tsdate_tsinfer_300]
methods_50 = ["SINGER", "ARGweaver", "Relate", "tsinfer+tsdate"]
methods_300 = ["SINGER", "ARG-Needle", "Relate", "tsinfer+tsdate"]
colors_50 = ["red", "purple", "green", "blue"]
colors_300 = ["red", "brown", "green", "blue"]
plot_bar_plot(mse_50, mse_300, methods_50, methods_300, colors_50, colors_300, 1.2, "results/figures/pairwise_mse.png") 
