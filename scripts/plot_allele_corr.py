import bar_plot_utils
from bar_plot_utils import *
import pairwise_utils
from pairwise_utils import * 


comparison_singer_50 = np.loadtxt("results/singer_ts/allele_singer_50.txt", delimiter=',')
comparison_relate_50 = np.loadtxt("results/relate_ts/allele_relate_50.txt", delimiter=',')
comparison_tsdate_tsinfer_50 = np.loadtxt("results/tsdate_tsinfer_ts/allele_tsdate_tsinfer_50.txt", delimiter=',')
comparison_singer_300 = np.loadtxt("results/singer_ts/allele_singer_300.txt", delimiter=',')
comparison_relate_300 = np.loadtxt("results/relate_ts/allele_relate_300.txt", delimiter=',')
comparison_tsdate_tsinfer_300 = np.loadtxt("results/tsdate_tsinfer_ts/allele_tsdate_tsinfer_300.txt", delimiter=',')
corr_singer_50 = corr(comparison_singer_50[:, 1], comparison_singer_50[:, 2])
corr_relate_50 = corr(comparison_relate_50[:, 1], comparison_relate_50[:, 2])
corr_tsdate_tsinfer_50 = corr(comparison_tsdate_tsinfer_50[:, 1], comparison_tsdate_tsinfer_50[:, 2])
corr_singer_300 = corr(comparison_singer_300[:, 1], comparison_singer_300[:, 2])
corr_relate_300 = corr(comparison_relate_300[:, 1], comparison_relate_300[:, 2])
corr_tsdate_tsinfer_300 = corr(comparison_tsdate_tsinfer_300[:, 1], comparison_tsdate_tsinfer_300[:, 2])
corr_50 = [corr_singer_50, corr_relate_50, corr_tsdate_tsinfer_50]
corr_300 = [corr_singer_300, corr_relate_300, corr_tsdate_tsinfer_300]
methods_50 = ["SINGER", "Relate", "tsinfer+tsdate"]
methods_300 = ["SINGER", "Relate", "tsinfer+tsdate"]
colors_50 = ["red", "green", "blue"]
colors_300 = ["red", "green", "blue"]
plot_bar_plot(corr_50, corr_300, methods_50, methods_300, colors_50, colors_300, 2, "results/figures/allele_corr.png") 
