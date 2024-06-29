import allele_age_utils
from allele_age_utils import *

all_positions = []
all_ref_ages = []
all_test_ages = []

for i in range(10):
    print(f'Process ARG number {i}')
    ts = tskit.load(f'results/simulated_ts/sim_50_{i}.trees')
    inferred_ts = tskit.load(f'results/tsdate_tsinfer_ts/tsdate_tsinfer_50_{i}.trees')
    pos, ref_ages, test_ages = get_age_comparison(ts, inferred_ts, 5e3) 
    all_positions.extend(pos)
    all_ref_ages.extend(ref_ages)
    all_test_ages.extend(test_ages)     

comparison = np.column_stack([all_positions, all_ref_ages, all_test_ages])
np.savetxt("results/tsdate_tsinfer_ts/allele_tsdate_tsinfer_50.txt", comparison, fmt='%f', delimiter=',')

