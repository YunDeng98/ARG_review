import os
import numpy as np
import tskit 
import random
import math
import collections
from collections import Counter



def generate_triplets(num, sample_size, seed=1):
    random.seed(1)
    triplets = set()
    while len(triplets) < num:
        triplet = tuple(random.sample(range(sample_size), 3))
        triplets.add(triplet)
    triplets = list(triplets)
    return triplets
    
def generate_quartets(num, sample_size, seed=1):
    random.seed(1)
    quartets = set()
    while len(quartets) < num:
        quartet = tuple(random.sample(range(sample_size), 4))
        quartets.add(quartet)
    quartets = list(quartets)
    return quartets

def find_mode(lst):
    data = collections.Counter(lst)
    return data.most_common(1)[0][0]


def find_first_clade(tree):
    min_time = np.inf
    lowest_node = None
    for node in tree.nodes():
        if not tree.is_leaf(node):
            t = tree.time(node)
            if t < min_time:
               min_time = t
               lowest_node = node
    if lowest_node == None:
        return (0, 1)
    clade = tree.children(lowest_node)[0:2]
    clade = list(clade)
    clade.sort()
    return tuple(clade)
    

def find_triplet_clade(tree):
    triplet_clades = [(0, 1), (1, 2), (0, 2)]
    clade = find_first_clade(tree)
    return triplet_clades.index(clade)

def find_quartet_clade(tree):
    quartet_clades = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    clade = find_first_clade(tree)
    index = quartet_clades.index(clade)
    return min(index, 5 - index)

def get_bin_triplet_clade(ts, s, triplet, cutoff):
    l = ts.sequence_length
    sub_ts = ts.simplify(samples=list(triplet))
    pos = 0
    clades = []
    tree = sub_ts.first()
    while tree.total_branch_length == 0:
        tree.next()
    while (pos < l):
        while (pos > tree.interval[1]):
            tree.next()
        c = find_triplet_clade(tree)
        clades.append(c)
        pos += s
    return clades[0:cutoff]

def get_all_bin_triplet_clade(ts, s, triplet_set, cutoff):
    all_clades = []
    for tp in triplet_set:
        clades = get_bin_triplet_clade(ts, s, tp, cutoff)
        all_clades.extend(clades)
    return np.array(all_clades)

def get_bin_quartet_clade(ts, s, quartet, cutoff):
    l = ts.sequence_length
    sub_ts = ts.simplify(samples=list(quartet))
    pos = 0
    clades = []
    tree = sub_ts.first()
    while tree.total_branch_length == 0:
        tree.next()
    while (pos < l):
        while (pos > tree.interval[1]):
            tree.next()
        c = find_quartet_clade(tree)
        clades.append(c)
        pos += s
    return clades[0:cutoff]

def get_all_bin_quartet_clade(ts, s, quartet_set, cutoff):
    all_clades = []
    for tp in quartet_set:
        clades = get_bin_quartet_clade(ts, s, tp, cutoff)
        all_clades.extend(clades)
    return np.array(all_clades)


def get_bin_mode_triplet_clade(ts_list, s, triplet, cutoff):
    sub_ts_list = [ts.simplify(samples=list(triplet)) for ts in ts_list]
    l = math.ceil(ts_list[0].sequence_length)
    pos = 0
    clades = []
    tree_list = [s.first() for s in sub_ts_list]
    clade_list = []
    clades = []
    while (pos < l):
        clade_list = []
        for tree in tree_list:
            while (pos > tree.interval[1]):
                tree.next()
            c = find_triplet_clade(tree)
            clade_list.append(c)
        mc = find_mode(clade_list)
        clades.append(mc)
        pos += s
    return clades

def get_all_bin_mode_triplet_clade(ts_list, s, triplet_set, cutoff):
    all_clades = []
    for tp in triplet_set:
        clades = get_bin_mode_triplet_clade(ts_list, s, tp, cutoff)
        all_clades.extend(clades)
    return np.array(all_clades)

def get_bin_mode_quartet_clade(ts_list, s, quartet, cutoff):
    sub_ts_list = [ts.simplify(samples=list(quartet)) for ts in ts_list]
    l = math.ceil(ts_list[0].sequence_length)
    pos = 0
    clades = []
    tree_list = [s.first() for s in sub_ts_list]
    clade_list = []
    clades = []
    while (pos < l):
        clade_list = []
        for tree in tree_list:
            while (pos > tree.interval[1]):
                tree.next()
            c = find_quartet_clade(tree)
            clade_list.append(c)
        mc = find_mode(clade_list)
        clades.append(mc)
        pos += s
    return clades

def get_all_bin_mode_quartet_clade(ts_list, s, quartet_set, cutoff):
    all_clades = []
    for tp in quartet_set:
        clades = get_bin_mode_quartet_clade(ts_list, s, tp, cutoff)
        all_clades.extend(clades)
    return np.array(all_clades)


def hamming_distance(l1, l2):
    n = len(l1)
    d = 0
    for i in range(n):
        if l1[i] != l2[i]:
            d += 1
    return d

def error_proportion(l1, l2):
    n = len(l1)
    e = sum(l1 != l2)
    return e/n

def get_configuration(folder_path, prefix, s, triplet_set):
    output_file = os.path.join(folder_path, f"{prefix}_clades.txt")
    if os.path.exists(output_file):
        print(f"{output_file} exists, skipped...")
        return
    trees_file = os.path.join(folder_path, f"{prefix}.trees")
    ts = tskit.load(trees_file)
    d = get_all_bin_triplet_clade(ts, s, triplet_set)
    np.savetxt(output_file, d, delimiter='\t')

def get_sample_configuration(folder_path, prefix, indices, s, triplet_set):
    output_file = os.path.join(folder_path, f"{prefix}_clades.txt")
    if os.path.exists(output_file):
        print(f"{output_file} exists, skipped...")
        return
    trees_files = [os.path.join(folder_path, f"{prefix}_{index}.trees") for index in indices]
    ts_list = [tskit.load(tf) for tf in trees_files]
    d = get_all_bin_mode_triplet_clade(ts_list, s, triplet_set)
    np.savetxt(output_file, d, delimiter='\t')
    print(f"{output_file} saved")



