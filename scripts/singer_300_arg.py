import os
import tskit
import subprocess


# Extract the index from the command line arguments
index = int(snakemake.wildcards["x"])

# Set the parameters for SINGER inference
mutation_rate = 2e-8
recombination_rate = 2e-8
pop_size = 1e4

parallel_singer_cmd = f"singer-0.1.7-beta-linux-x86_64/parallel_singer -Ne {pop_size} -m {mutation_rate} -ratio 0.5 -L 2000000 -n 100 -thin 50 -polar 0.99 -vcf results/simulated_vcf/sim_300_{index} -output results/singer_ts/singer_300_{index}"

subprocess.run(parallel_singer_cmd, shell=True)
