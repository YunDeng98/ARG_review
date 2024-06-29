import allele_age_utils
from allele_age_utils import *
import concurrent.futures

def process_inferred_ts(args):
    ts0, ts1, t = args  # Unpack arguments
    pos, ref_ages, test_ages = get_age_comparison(ts0, ts1, t)
    return test_ages

all_positions = []
all_ref_ages = []
all_test_ages = []

for i in range(10):
    print(f'Process ARG number {i}')
    ts = tskit.load(f'results/simulated_ts/sim_50_{i}.trees')
    inferred_ts_list = [tskit.load(f"results/singer_ts/singer_50_{i}_{j}.trees") for j in range(50, 100)]
    ref_ages, positions = get_reference_ages_and_positions(ts)
    args_list = [(ts, inferred_ts_list[j], 5e3) for j in range(50)]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        test_ages_list = list(executor.map(process_inferred_ts, args_list))
    all_positions.extend(positions)
    all_ref_ages.extend(ref_ages)
    all_test_ages.extend(np.mean(test_ages_list, axis=0))

comparison = np.column_stack([all_positions, all_ref_ages, all_test_ages])
np.savetxt("results/singer_ts/allele_singer_50.txt", comparison, fmt='%f', delimiter=',')

#plot_pairwise_heatmap(true_coalescence, inferred_coalescence, 2.5, 5.5, 5e4, "results/figures/pairwise_singer_50.png") 
