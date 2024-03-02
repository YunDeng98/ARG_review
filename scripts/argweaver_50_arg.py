import os
import tskit
import subprocess
import pandas as pd
import ete3
from ete3 import Tree

def get_site_info(v):
    x = int(v.position)
    states = 'ATCG'
    site = ''
    for i in range(len(v.genotypes)):
        site += states[v.genotypes[i]]
    return str(x) + '\t' + site + '\n'

def write_sites_file(mts, filename):
    n = mts.num_samples
    l = int(mts.sequence_length)
    with open(filename, 'w') as file:
        file.write('NAMES\t')
        for i in range(n):
            file.write('n' + str(i))
            if (i < n - 1):
                file.write('\t')
        file.write('\n')
        file.write('REGION\tchr\t1\t' + str(l) + '\n')
        for v in mts.variants():
            site_info = get_site_info(v)  # Assuming this function is defined elsewhere
            file.write(site_info)

# Function to convert .trees files to .sites files for ARGweaver
def convert_tree_sequences_to_sites(trees_file_path, sites_file_path):
    # Load tree sequence from .trees file
    mts = tskit.load(trees_file_path)        
    # Write .sites file
    write_sites_file(mts, sites_file_path)
    print(f"Saved: {sites_file_path}")


# Function to run ARGweaver on .sites files
def run_argweaver_on_sites(sites_file_path, output_prefix, m, r):
    command = f"./argweaver --overwrite -s {sites_file_path} -o {output_prefix} -N 1e4 -m {m} -r {r} --sample-step 40 -n 3000 -c 10 --resample-window-iters 1 --no-compress-output"
    print(f"Start run: {output_prefix}")
    subprocess.run(command, shell=True)             

def get_time_map(tree):
    time_map = {}
    time_map[tree.name] = 0
    get_time_map_helper(tree, time_map)
    min_time = 0
    for n in time_map:
        min_time = min(min_time, time_map[n])
    for n in time_map:
        time_map[n] = time_map[n] - min_time
    return time_map

def get_time_map_helper(tree, time_map):
    for c in tree.children:
        time_map[c.name] = time_map[tree.name] - c.dist
        get_time_map_helper(c, time_map)

def get_sample_nodes(tree):
    sample_nodes = {}
    #count = 0
    for n in tree.traverse('preorder'):
        if n.is_leaf():
            sample_nodes[n.name] = int(n.name)
    return sample_nodes

def write_sample_nodes(tree, tables):
    time_map = get_time_map(tree)
    sample_nodes = get_sample_nodes(tree)
    n = len(sample_nodes)
    for i in range(n):
        node_name = str(i)
        tables.nodes.add_row(flags=tskit.NODE_IS_SAMPLE, time = time_map[node_name])
    return

def get_perturbed_time_map(tree):
    time_map = get_time_map(tree)
    sort = []
    for n in tree.traverse('preorder'):
        sort.append(n)
    m = len(sort)
    for i in range(len(sort)):
        n = sort[i]
        if len(n.children) > 0:
            time_map[n.name] = time_map[n.name] + (m-i)*0.1
    return time_map

def update_table(tables, tree, sample_nodes, left, right):
    index_map = {}
    time_map = get_perturbed_time_map(tree)
    for x in tree.traverse():
        if x.name not in sample_nodes:
            index_map[x.name] = tables.nodes.num_rows
            tables.nodes.add_row(time = time_map[x.name])
        else:
            index_map[x.name] = sample_nodes[x.name]
    for x in tree.traverse():
        for y in x.children:
            assert time_map[y.name] < time_map[x.name]
            tables.edges.add_row(left, right, index_map[x.name], index_map[y.name])
    return

def read_smc(filename):
    permute_map = get_permute_map(filename)
    df = pd.read_csv(filename, skiprows=lambda x: x%2 == 1 or x == 0, delimiter='\t', header = None)
    sl = df.iloc[-1, 2]
    tables = tables = tskit.TableCollection(sequence_length=sl)
    init_tree = Tree(df.iloc[0, 3], format=1)
    sample_nodes = get_sample_nodes(init_tree)
    write_sample_nodes(init_tree, tables)
    n = df.shape[0]
    for i in range(n):
        tree = Tree(df.iloc[i, 3], format=1)
        left = df.iloc[i, 1] - df.iloc[0, 1]
        right = df.iloc[i, 2] - df.iloc[0, 1] + 1
        update_table(tables, tree, sample_nodes, left, right)
    tables.sort()
    ts = tables.tree_sequence()
    #new_tables = permute_tables(tables, permute_map)
    #ts = new_tables.tree_sequence()
    order = get_new_order(filename)
    new_ts = ts.simplify(order)
    return new_ts

def permute_tables(tables, permute_map):
    n = len(permute_map)
    sl = tables.sequence_length
    new_tables = tskit.TableCollection(sequence_length=sl)
    l = len(tables.nodes)
    for i in range(l):
        t = tables.nodes.time[i]
        if i < n:
            new_tables.nodes.add_row(flags=tskit.NODE_IS_SAMPLE, time = t)
        else:
            new_tables.nodes.add_row(time = t)
    m = len(tables.edges)
    for i in range(m):
        c = tables.edges.child[i]
        p = tables.edges.parent[i]
        l = tables.edges.left[i]
        r = tables.edges.right[i]
        if (c in permute_map):
            new_tables.edges.add_row(l, r, p, permute_map[c])
        else:
            new_tables.edges.add_row(l, r, p, c)
    new_tables.sort()
    return new_tables

def get_permute_map(filename):
    permute_map = {}
    df = pd.read_csv(filename, nrows = 1, header=None, delimiter='\t')
    for i in range(df.shape[1] - 1):
        permute_map[i] = int(df.iloc[0, i+1][1])
    return permute_map

def get_new_order(filename):
    order_map = {}
    order = []
    df = pd.read_csv(filename, nrows = 1, header=None, delimiter='\t')
    for i in range(df.shape[1] - 1):
        num = int(df.iloc[0, i+1][1:])
        order_map[num] = i
    for i in range(df.shape[1] - 1):
        order.append(order_map[i])
    return order

def convert_smc_to_trees(prefix, indices):
    for index in indices:
        # Construct the paths for the .smc and .trees files
        smc_path = f"{prefix}.{index}.smc"
        trees_path = f"{prefix}.{index}.trees"
        
        # Read the .smc file and get a tskit object
        ts = read_smc(smc_path)
                
        # Save the tskit object as a .trees file
        ts.dump(trees_path)

index = int(snakemake.wildcards["x"])
convert_tree_sequences_to_sites(f"results/simulated_ts/sim_50_{index}.trees", f"results/argweaver_ts/sim_50_{index}.sites")
run_argweaver_on_sites(f"results/argweaver_ts/sim_50_{index}.sites", f"results/argweaver_ts/argweaver_50_{index}", m=1.2e-8, r=1.2e-8)
convert_smc_to_trees(f"results/argweaver_ts/argweaver_50_{index}", range(1000, 3000, 40))
