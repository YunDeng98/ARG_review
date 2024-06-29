import os
import matplotlib.pyplot as plt
import numpy as np
import math
import tskit
import random
from scipy.stats import spearmanr
import pandas as pd
from IPython.display import SVG, Image, display
import pysam
import seaborn as sns

def calculate_windowed_tmrca(ts, window_size):
    grid = np.arange(0, ts.sequence_length, window_size)
    grid = np.append(grid, ts.sequence_length)
    window_index = 0
    m = len(grid) - 1
    arg_tmrca = np.zeros(m)
    tree = ts.first()
    while tree.interval[1] != ts.sequence_length and window_index <= m:
        y = min(tree.interval[1], grid[window_index + 1])
        x = max(tree.interval[0], grid[window_index])
        if len(tree.roots) == 1:
            arg_tmrca[window_index] += tree.time(tree.root)*(y-x)/window_size
        if tree.interval[1] > grid[window_index + 1]:
            window_index += 1
        else:
            tree.next()
    return arg_tmrca

def find_variant_carriers(vcf_path, chrom, position):
    vcf = pysam.VariantFile(vcf_path)
    allele_indices = []

    for rec in vcf.fetch(chrom, position-1, position):
        sample_index = 0
        for sample in rec.samples:
            genotype = rec.samples[sample]['GT']
            allele_index = 0
            for allele in genotype:
                if allele > 0:  # Allele > 0 indicates a variant allele
                    allele_indices.append(2 * sample_index + allele_index)
                allele_index +=1
            sample_index += 1
    
    return allele_indices


ceu_chr9_ts_list = []
for i in range(50, 100, 10):
    ceu_chr9_ts = tskit.load(f"inferred_ts/ceu_chr9_{i}.trees")
    ceu_chr9_ts_list.append(ceu_chr9_ts)

ceu_tmrca_list = []
for ceu_chr9_ts in ceu_chr9_ts_list: 
    y = calculate_windowed_tmrca(ceu_chr9_ts, 1e3)
    ceu_tmrca_list.append(y)

ceu_mean_tmrca = np.mean(ceu_tmrca_list, axis=0)

plt.figure(figsize = [12, 3])
plt.plot([0.001*i for i in range(len(ceu_mean_tmrca))], ceu_mean_tmrca*28/1e6, color='purple', label="Inferred TMRCA")
plt.xlim([132.8, 133.8]);
plt.fill_between([132.7+0.533, 132.7+0.576], y1=0, y2=9e6, color='gray', alpha=0.5, label='ABO');
plt.ylim([0, 10]);
plt.axhline(y=6, color='black', linestyle='-');
plt.axhline(y=np.mean(ceu_median_tmrca)*28/1e6, color='brown', linestyle='--', label='Chr9 median TMRCA');
plt.legend(fontsize = 10);
plt.savefig("results/figures/ABO.png", dpi=300);

lct_windows = np.arange(0, 1e6+1e3, 1e3)

gbr_carriers = find_variant_carriers('inferred_ts/gbr_cleaned_chr2.vcf.gz', 'chr2', 135851076)

gbr_carrier_ts_list = []
for i in range(50, 100):
    gbr_lct_ts = tskit.load(f"inferred_ts/singer_lct/gbr_mcm6_{i}.trees")
    gbr_carrier_ts = gbr_lct_ts.simplify(gbr_carriers)
    gbr_carrier_ts_list.append(gbr_carrier_ts)

gbr_carrier_branch_div_list = []
for gbr_carrier_ts in gbr_carrier_ts_list:
    gbr_carrier_branch_div_list.append(gbr_carrier_ts.diversity(mode='branch', windows=lct_windows))

plt.figure(figsize = [12, 3]);
plt.plot(lct_windows[0:-1]/1e6 + 135.3, mean_gbr_lct_branch_div*1.2e-8, color='red', label='All samples');
plt.plot(lct_windows[0:-1]/1e6 + 135.3, mean_gbr_carrier_branch_div*1.2e-8, color='blue', label="Haplotypes with rs4988235 derived allele");
plt.fill_between([135.83, 135.88], y1=0, y2=0.01, color='gray', alpha=0.5, label='MCM6 gene');
plt.xlim([135.4, 136.2]);
plt.ylim([-0, 0.002]);
plt.legend(fontsize=10);
plt.savefig("results/figures/MCM6.png", dpi=300);
