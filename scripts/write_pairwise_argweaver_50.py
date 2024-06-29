import pairwise_utils
from pairwise_utils import *
import concurrent.futures

def process_inferred_ts(args):
    i, j, pairs, cutoff = args  # Unpack arguments
    print(i, j)
    inferred_ts_path = f'results/argweaver_ts/argweaver_50_{i}.{j}.trees'
    inferred_ts = tskit.load(inferred_ts_path)
    t1 = get_all_pairwise_times(inferred_ts, 1e3, pairs, cutoff)
    return t1

pairs = generate_pairs(100, 50) 

true_coalescence = []
inferred_coalescence = []

for i in range(10):
    print(f'Process ARG number {i}')
    ts = tskit.load(f'results/simulated_ts/sim_50_{i}.trees')
    t0 = get_all_pairwise_times(ts, 1e3, pairs, 10000)
    args_list = [(i, j, pairs, 10000) for j in range(1000, 3000, 40)]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        inferred_coalescence_list = list(executor.map(process_inferred_ts, args_list))
    true_coalescence.extend(t0)
    inferred_coalescence.extend(np.mean(inferred_coalescence_list, axis=0))

comparison = np.column_stack([true_coalescence, inferred_coalescence])
np.savetxt("results/argweaver_ts/pairwise_argweaver_50.txt", comparison, fmt='%f', delimiter=',')

#plot_pairwise_heatmap(true_coalescence, inferred_coalescence, 2.5, 5.5, 5e4, "results/figures/pairwise_argweaver_50.png") 
