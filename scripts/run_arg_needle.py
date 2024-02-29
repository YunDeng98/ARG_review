import subprocess
import os
import tskit
import arg_needle
import arg_needle_lib

def run_arg_needle(folder_name, prefix, indices):
    for index in indices:
        output_argn = f"{folder_name}/{prefix}_{index}.argn"

        # Check if the output file already exists
        if os.path.exists(output_argn):
            print(f"Output file {output_argn} already exists. Skipping index {index}.")
            continue

        hap_gz = f"{folder_name}/{prefix}_{index}.haps"
        map_file = f"{folder_name}/{prefix}_{index}.map"
        output = f"{folder_name}/{prefix}_{index}"

        command = [
            "arg_needle", 
            "--hap_gz", hap_gz, 
            "--map", map_file, 
            "--out", output, 
            "--mode", "sequence", 
            "--normalize", "0"
        ]

        try:
            subprocess.run(command, check=True)
            print(f"arg_needle run successfully for index: {index}")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running arg_needle for index {index}: {e}")

def generate_map_from_haps(haps_filename, map_filename, recomb_rate):
    if os.path.exists(map_filename):
        print(f"Map file {map_filename} already exists. Skipping.")
        return

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

def generate_plink_maps(folder_name, prefix, indices, recomb_rate):
    for index in indices:
        haps_filename = f"{folder_name}/{prefix}_{index}.haps"
        map_filename = f"{folder_name}/{prefix}_{index}.map"
        generate_map_from_haps(haps_filename, map_filename, recomb_rate)

def convert_arg_needle_to_tskit(folder_name, prefix, indices):
    for index in indices:
        argn_filename = f"{folder_name}/{prefix}_{index}.argn"
        trees_filename = f"{folder_name}/{prefix}_{index}.trees"

        # Check if the .trees file already exists
        if os.path.exists(trees_filename):
            print(f"Trees file {trees_filename} already exists. Skipping.")
            continue

        # Deserialize the .argn file
        arg = arg_needle_lib.deserialize_arg(argn_filename)

        # Convert the ARG object to a tskit TreeSequence
        ts = arg_needle_lib.arg_to_tskit(arg)

        # Dump the TreeSequence to a .trees file
        ts.dump(trees_filename)
        print(f"Converted {argn_filename} to {trees_filename}")


# Example usage
generate_plink_maps("arg_needle_ts", "500", range(0, 10), 2.0)
run_arg_needle("arg_needle_ts", "500", range(0, 10))
convert_arg_needle_to_tskit("arg_needle_ts", "500", range(0, 10))
