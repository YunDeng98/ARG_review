import tskit
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from scipy.stats import spearmanr
import random

def get_reference_ages_and_positions(reference_ts):
    ages = []
    positions = []

    for tree in reference_ts.trees():
        for site in tree.sites():
            if len(site.mutations) > 0:
                first_mutation = site.mutations[0]
                node = first_mutation.node
                node_time = tree.time(node)
                parent_time = tree.time(tree.parent(node))
                ages.append(0.5*(node_time + parent_time))
                positions.append(site.position)

    return np.array(ages), np.array(positions)

def get_test_ages(test_ts, ref_positions, ref_ages, fixed_age):
    test_ages = np.full_like(ref_ages, fixed_age)  # Initialize with fixed values
    next_ref_idx = 0  # Index to keep track of the next reference position to check

    for tree in test_ts.trees():
        if next_ref_idx >= len(ref_positions):
            break  # All reference positions processed

        for site in tree.sites():
            
            assert(site.position >= ref_positions[next_ref_idx])
            while site.position > ref_positions[next_ref_idx]:
                next_ref_idx += 1
            
            if len(site.mutations) > 0:
                mutation = site.mutations[0]
                node = mutation.node
                node_time = tree.time(node)
                branch_length = tree.branch_length(node)                
 
                random_age = 0.5*branch_length + node_time 
                test_ages[next_ref_idx] = random_age
            next_ref_idx += 1

    return test_ages

def get_age_comparison(reference_ts, test_ts, fixed_age):
        
    ref_ages, positions = get_reference_ages_and_positions(reference_ts)
        
    test_ages = get_test_ages(test_ts, positions, ref_ages, fixed_age)
       
    return positions, ref_ages, test_ages 

def mse(x, y):
    x = np.array(x)
    y = np.array(y)
    return np.mean((x - y)**2)

def corr(x, y):
    x = np.array(x)
    y = np.array(y)
    return spearmanr(x, y)[0]


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
    plt.xticks(ticks=np.log10([10**1, 10**2, 10**3, 10**4, 10**5]), labels=[r'$10^1$', r'$10^2$', r'$10^3$', r'$10^4$', r'$10^5$'])
    plt.yticks(ticks=np.log10([10**1, 10**2, 10**3, 10**4, 10**5]), labels=[r'$10^1$', r'$10^2$', r'$10^3$', r'$10^4$', r'$10^5$'])
    plt.xticks(fontsize = 15)
    plt.yticks(fontsize = 15)
    plt.savefig(filename, dpi=300)  # Ensure the saved figure has a white background
