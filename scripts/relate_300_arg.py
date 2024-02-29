import os
import tskit
import subprocess


def generate_map_file(r, map_file_path="map_file.txt"):
    with open(map_file_path, "w") as f:
        f.write("pos COMBINED_rate Genetic_Map\n")
        f.write(f"0 {r * 1e8} 0\n")
        f.write(f"{1e8} {r * 1e8} {r * 1e8 * 100}\n")


# Extract the index from the command line arguments
index = int(snakemake.wildcards["x"])

generate_map_file(1.2e-8, f"results/relate_ts/300_{index}_map_file.txt")

# Set the parameters for Relate inference
mutation_rate = 1.2e-8
recombination_rate = 1.2e-8
pop_size = 1e4

relate_convert_vcf = f"relate_v1.2.1_x86_64_static/bin/RelateFileFormats --mode ConvertFromVcf --haps results/relate_ts/sim_300_{index}.haps --sample results/relate_ts/sim_300_{index}.sample -i results/simulated_vcf/sim_300_{index}"

subprocess.run(relate_convert_vcf, shell=True)

os.chdir("results/relate_ts/")

relate_main_cmd = f"../../relate_v1.2.1_x86_64_static/bin/Relate --mode All -m {mutation_rate} -N {2*pop_size} --haps sim_300_{index}.haps --sample sim_300_{index}.sample --map 300_{index}_map_file.txt --seed 1 -o relate_300_{index}"

subprocess.run(relate_main_cmd, shell=True)

relate_convert_ts = f"../../relate_v1.2.1_x86_64_static/bin/RelateFileFormats --mode ConvertToTreeSequence -i relate_300_{index} -o relate_300_{index}"

subprocess.run(relate_convert_ts, shell=True)

clean_cmd = f"../../relate_v1.2.1_x86_64_static/bin/RelateFileFormats/bin/Relate --mode Clean -o relate_300_{index}"

subprocess.run(clean_cmd, shell=True)
