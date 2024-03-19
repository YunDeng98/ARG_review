import pairwise_utils
from pairwise_utils import *

pairs = generate_pairs(100, 300) 

true_coalescence = []
inferred_coalescence = []

for i in range(10):
    print(f'Process ARG number {i}')
    ts = tskit.load(f'results/simulated_ts/sim_300_{i}.trees')
    t0 = get_all_pairwise_times(ts, 1e3, pairs)
    inferred_ts = tskit.load(f'results/arg_needle_ts/arg_needle_300_{i}.trees')
    t1 = get_all_pairwise_times(inferred_ts, 1e3, pairs)
    n = min(len(t0), len(t1))
    true_coalescence.extend(t0[0:n])
    inferred_coalescence.extend(t1[0:n])

r = np.mean(true_coalescence)/np.mean(inferred_coalescence)
inferred_coalescence = np.multiply(r, inferred_coalescence)

plot_pairwise_heatmap(true_coalescence, inferred_coalescence, 2.5, 5.5, 5e4, "results/figures/pairwise_arg_needle_300.png") 
