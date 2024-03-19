import pairwise_utils
from pairwise_utils import *

pairs = generate_pairs(100, 50) 

true_coalescence = []
inferred_coalescence = []

for i in range(10):
    print(f'Process ARG number {i}')
    ts = tskit.load(f'results/simulated_ts/sim_50_{i}.trees')
    t0 = get_all_pairwise_times(ts, 1e3, pairs)
    true_coalescence.extend(get_all_pairwise_times(ts, 1e3, pairs))
    inferred_coalescence_list = []
    for j in range(1000, 3000, 40):
        print(j)
        inferred_ts = tskit.load(f'results/argweaver_ts/argweaver_50_{i}.{j}.trees')
        t1 = get_all_pairwise_times(inferred_ts, 1e3, pairs)
        n = min(len(t0), len(t1))
        inferred_coalescence_list.append(t1[0:n])
    true_coalescence.extend(t0[0:n])
    inferred_coalescence.extend(np.mean(inferred_coalescence_list, axis=0))

plot_pairwise_heatmap(true_coalescence, inferred_coalescence, 2.5, 5.5, 5e4, "results/figures/pairwise_argweaver_50.png") 
