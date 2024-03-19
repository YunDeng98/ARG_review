import pairwise_utils
from pairwise_utils import *

pairs = generate_pairs(100, 300) 

true_coalescence = []
inferred_coalescence = []

for i in range(10):
    print(f'Process ARG number {i}')
    ts = tskit.load(f'results/simulated_ts/sim_300_{i}.trees')
    true_coalescence.extend(get_all_pairwise_times(ts, 1e3, pairs))
    inferred_ts = tskit.load(f'results/tsdate_tsinfer_ts/tsdate_tsinfer_300_{i}.trees')
    inferred_coalescence.extend(get_all_pairwise_times(inferred_ts, 1e3, pairs))

plot_pairwise_heatmap(true_coalescence, inferred_coalescence, 2.5, 5.5, 5e4, "results/figures/pairwise_tsdate_tsinfer_300.png") 
