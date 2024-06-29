import pairwise_utils
from pairwise_utils import *

pairs = generate_pairs(100, 300) 

true_coalescence = []
inferred_coalescence = []

for i in range(10):
    print(f'Process ARG number {i}')
    ts = tskit.load(f'results/simulated_ts/sim_300_{i}.trees')
    inferred_ts = tskit.load(f'results/relate_ts/relate_300_{i}.trees')
    num_bins = min(round(inferred_ts.sequence_length/1e3), 10000)
    t0 = get_all_pairwise_times(ts, 1e3, pairs, num_bins)
    t1 = get_all_pairwise_times(inferred_ts, 1e3, pairs, num_bins)    
    true_coalescence.extend(t0)
    inferred_coalescence.extend(t1)     

comparison = np.column_stack([true_coalescence, inferred_coalescence])
np.savetxt("results/relate_ts/pairwise_relate_300.txt", comparison, fmt='%f', delimiter=',')

#plot_pairwise_heatmap(true_coalescence, inferred_coalescence, 2.5, 5.5, 5e4, "results/figures/pairwise_relate_300.png") 