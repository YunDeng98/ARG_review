import topology_utils
from topology_utils import *
import concurrent.futures

def process_file(i):
    print(f'Process ARG number {i}')
    ts = tskit.load(f'results/simulated_ts/sim_50_{i}.trees')
    inferred_ts_list = [tskit.load(f'results/singer_ts/singer_50_{i}_{j}.trees') for j in range(50, 100)]
    num_bins = 10000
    tc0 = get_all_bin_triplet_clade(ts, 1e3, triplets, num_bins)
    tc1 = get_all_bin_mode_triplet_clade(inferred_ts_list, 1e3, triplets, num_bins)
    qc0 = get_all_bin_quartet_clade(ts, 1e3, quartets, num_bins)
    qc1 = get_all_bin_mode_quartet_clade(inferred_ts_list, 1e3, quartets, num_bins)
    return tc0, tc1, qc0, qc1

triplets = generate_triplets(100, 50)
quartets = generate_quartets(100, 50) 

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
np.savetxt("results/singer_ts/triplet_singer_50.txt", triplet_comparison, fmt='%f', delimiter=',')
np.savetxt("results/singer_ts/quartet_singer_50.txt", quartet_comparison, fmt='%f', delimiter=',')

#plot_pairwise_heatmap(true_coalescence, inferred_coalescence, 2.5, 5.5, 5e4, "results/figures/pairwise_singer_50.png") 
