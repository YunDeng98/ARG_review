import tskit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from scipy.stats import spearmanr

def get_pairwise_times(ts, s, k1, k2, cutoff_length):
    l = ts.sequence_length
    windows = np.arange(0, l, s)
    windows = np.append(windows, l)
    n = ts.num_samples
    times = ts.divergence(sample_sets=[[k1], [k2]], windows=windows, mode='branch')
    return 0.5*times[0:cutoff_length]

def get_all_pairwise_times(ts, s, pairs, cutoff_length):
    times = []
    for p in pairs:
        times.extend(get_pairwise_times(ts, s, p[0], p[1], cutoff_length))
    return times

def generate_pairs(num_pairs, sample_size, seed=1):
    random.seed(seed)
    pairs = set()
    while len(pairs) < num_pairs:
        a = random.randint(0, sample_size-1)
        b = random.randint(0, sample_size-1)
        if a < b:
            pair = (a, b)
            pairs.add(pair)
    return pairs

def mse(x, y):
    x = np.array(x)
    y = np.array(y)
    return np.mean((x - y)**2)

def corr(x, y):
    x = np.array(x)
    y = np.array(y)
    return spearmanr(x, y)[0]

def plot_pairwise_heatmap(tx, ty, l, u, v, filename):
    error = mse(tx, ty)/4e8
    rho = corr(tx, ty)
    text_str = f'MSE={error:.3f}, $\\rho$={rho:.3f}'
    plt.figure(figsize = [6, 6])
    plt.hist2d(np.log10(tx), np.log10(ty), bins=50, cmap='magma', range=[[l, u], [l, u]], vmax=v);
    plt.plot([l, u], [l, u], color='white');
    plt.xticks(fontsize=15);
    plt.yticks(fontsize=15);
    plt.annotate(text_str, xy=(0.05, 0.95), xycoords='axes fraction', fontsize=15, ha='left', va='top', color='white')
    plt.savefig(filename, dpi=300);
    return 

def plot_hexbin_plot(tx, ty, l, u, v, filename):
    error = mse(tx, ty) / 4e8
    rho = corr(tx, ty)
    text_str = f'MSE={error:.3f}, $\\rho$={rho:.3f}'

    plt.figure(figsize=(6, 6))  # No need to specify facecolor='white' as it's the default
    plt.hexbin(np.log10(tx), np.log10(ty), gridsize=50, cmap='viridis', extent=(l, u, l, u), vmin=0, vmax=v)
    plt.plot([l, u], [l, u], color='red')
    plt.annotate(text_str, xy=(0.05, 0.95), xycoords='axes fraction', fontsize=15, ha='left', va='top', color='white')
    plt.xlim([l, u])
    plt.ylim([l, u])
    plt.xticks(ticks=np.log10([10**3, 10**4, 10**5]), labels=[r'$10^3$', r'$10^4$', r'$10^5$'])
    plt.yticks(ticks=np.log10([10**3, 10**4, 10**5]), labels=[r'$10^3$', r'$10^4$', r'$10^5$'])
    plt.xticks(fontsize = 15)
    plt.yticks(fontsize = 15)
    plt.savefig(filename, dpi=300)  # Ensure the saved figure has a white background
