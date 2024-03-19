import tsdate 
import tsinfer
import tskit

# Extract the index from the command line arguments
index = int(snakemake.wildcards["x"])

# Set the parameters for the simulation
mutation_rate = 2e-8

mts = tskit.load(f"results/simulated_ts/sim_50_{index}.trees")
sample_data = tsinfer.SampleData.from_tree_sequence(mts)
tsinfer_ts = tsinfer.infer(sample_data)
tsinfer_ts = tsinfer_ts.simplify()
tsdate_ts = tsdate.date(tsinfer_ts, Ne=1e4, mutation_rate=mutation_rate)

# Output file name based on the index
output_file = f"results/tsdate_tsinfer_ts/tsdate_tsinfer_50_{index}.trees"


# Save the tree sequence
tsdate_ts.dump(output_file)
