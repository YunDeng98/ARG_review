import msprime

index = int(snakemake.wildcards["x"])

num_individuals = 150 
sequence_length = 10e6  # 10 Mb
mutation_rate = 1.2e-8
recombination_rate = 1.2e-8

seed = index * 12345 + 67890 

ancestry = msprime.sim_ancestry(
    population_size=1e4,    
    samples=num_individuals,
    sequence_length=sequence_length,
    recombination_rate=recombination_rate,
    random_seed=seed
)

tree_sequence = msprime.sim_mutations(
    tree_sequence=ancestry,
    rate=mutation_rate,
    random_seed=seed
)

trees_output_file = f"results/simulated_ts/sim_300_{index}.trees"
vcf_output_file = f"results/simulated_vcf/sim_300_{index}.vcf"

tree_sequence.dump(trees_output_file)

with open(vcf_output_file, "w") as vcf_file:
    tree_sequence.write_vcf(vcf_file)

