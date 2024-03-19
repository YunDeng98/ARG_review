import subprocess
import os
import tskit
import arg_needle
import arg_needle_lib

def run_arg_needle(folder_name, input_prefix, output_prefix):
    hap_gz = f"{folder_name}/{input_prefix}.haps"
    map_file = f"{folder_name}/{input_prefix}.map"
    output = f"{folder_name}/{output_prefix}"

    command = [
        "arg_needle", 
        "--hap_gz", hap_gz, 
        "--map", map_file, 
        "--out", output, 
        "--mode", "sequence", 
        "--normalize", "0"
    ]

    subprocess.run(command, check=True)

def generate_map_from_haps(haps_filename, map_filename, recomb_rate):
    with open(haps_filename, 'r') as haps_file, open(map_filename, 'w') as map_file:
        previous_pos = 0
        cumulative_genetic_distance = 0

        for line in haps_file:
            fields = line.strip().split()
            chrom, rsid, pos = fields[0], fields[1], int(fields[2])

            # Calculate genetic distance from the previous variant
            interval_genetic_distance = recomb_rate * (pos - previous_pos) / 1e6  # Convert bp to Mbp
            cumulative_genetic_distance += interval_genetic_distance

            map_file.write(f'{chrom}\t{rsid}\t{cumulative_genetic_distance}\t{pos}\n')
            previous_pos = pos

def generate_plink_maps(folder_name, prefix, recomb_rate):
    haps_filename = f"{folder_name}/{prefix}.haps"
    map_filename = f"{folder_name}/{prefix}.map"
    generate_map_from_haps(haps_filename, map_filename, recomb_rate)

def convert_arg_needle_to_tskit(folder_name, prefix):
    argn_filename = f"{folder_name}/{prefix}.argn"
    trees_filename = f"{folder_name}/{prefix}.trees"


    # Deserialize the .argn file
    arg = arg_needle_lib.deserialize_arg(argn_filename)

    # Convert the ARG object to a tskit TreeSequence
    ts = arg_needle_lib.arg_to_tskit(arg)

    # Dump the TreeSequence to a .trees file
    ts.dump(trees_filename)
    print(f"Converted {argn_filename} to {trees_filename}")


index = int(snakemake.wildcards["x"])
subprocess.run(f"cp results/relate_ts/sim_300_{index}.haps results/arg_needle_ts/sim_300_{index}.haps", shell=True)
subprocess.run(f"cp results/relate_ts/sim_300_{index}.sample results/arg_needle_ts/sim_300_{index}.sample", shell=True)
generate_plink_maps("results/arg_needle_ts", f"sim_300_{index}", 2)
run_arg_needle("results/arg_needle_ts", f"sim_300_{index}", f"arg_needle_300_{index}")
convert_arg_needle_to_tskit("results/arg_needle_ts", f"arg_needle_300_{index}")
