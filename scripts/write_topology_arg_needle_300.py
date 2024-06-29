import topology_utils
from topology_utils import *
import concurrent.futures

def process_file(i):
    print(f'Process ARG number {i}')
    ts = tskit.load(f'results/simulated_ts/sim_300_{i}.trees')
    inferred_ts = tskit.load(f'results/arg_needle_ts/arg_needle_300_{i}.trees')
    num_bins = min(round(inferred_ts.sequence_length/1e3), 10000)
    tc0 = get_all_bin_triplet_clade(ts, 1e3, triplets, num_bins)
    tc1 = get_all_bin_triplet_clade(inferred_ts, 1e3, triplets, num_bins)
    qc0 = get_all_bin_quartet_clade(ts, 1e3, quartets, num_bins)
    qc1 = get_all_bin_quartet_clade(inferred_ts, 1e3, quartets, num_bins)
    return tc0, tc1, qc0, qc1

triplets = generate_triplets(100, 300)
quartets = generate_quartets(100, 300) 

true_triplet_topology = []
inferred_triplet_topology = []

true_quartet_topology = []
inferred_quartet_topology = []


with concurrent.futures.ProcessPoolExecutor() as executor:
    # Map process_file function to an iterator over your range
    results = executor.map(process_file, range(10))
    
    # Process results and extend your lists accordingly
    for tc0, tc1, qc0, qc1 in results:
        true_triplet_topology.extend(tc0)
        inferred_triplet_topology.extend(tc1)
        true_quartet_topology.extend(qc0)
        inferred_quartet_topology.extend(qc1)

triplet_comparison = np.column_stack([true_triplet_topology, inferred_triplet_topology])
quartet_comparison = np.column_stack([true_quartet_topology, inferred_quartet_topology])
np.savetxt("results/arg_needle_ts/triplet_arg_needle_300.txt", triplet_comparison, fmt='%f', delimiter=',')
np.savetxt("results/arg_needle_ts/quartet_arg_needle_300.txt", quartet_comparison, fmt='%f', delimiter=',')

#plot_pairwise_heatmap(true_coalescence, inferred_coalescence, 2.5, 5.5, 5e4, "results/figures/pairwise_arg_needle_300.png") 
