import msprime
import tszip
import json
import numpy

path_to_chroms = "./5495535"
Spacing = 1e5

LISTOFFILES = [path_to_chroms + "/hgdp_tgp_sgdp_chr10_p.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr20_q.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr10_q.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr21_q.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr11_p.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr22_q.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr11_q.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr2_p.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr12_p.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr2_q.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr12_q.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr3_p.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr13_q.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr3_q.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr14_q.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr4_p.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr15_q.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr4_q.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr16_p.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr5_p.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr16_q.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr5_q.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr17_p.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr6_p.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr17_q.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr6_q.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr18_p.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr7_p.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr18_q.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr7_q.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr19_p.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr8_p.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr19_q.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr8_q.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr1_p.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr9_p.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr1_q.dated.trees.tsz",	path_to_chroms + "/hgdp_tgp_sgdp_chr9_q.dated.trees.tsz",
path_to_chroms + "/hgdp_tgp_sgdp_chr20_p.dated.trees.tsz"]

for pop in ["CHB", "YRI", "Quechua", "GBR"]:
    LISTOFTIMES = [-1] * (int(10 * 3000000000/Spacing)) # changed this
    timesindex = 0
    for tsname in LISTOFFILES:
        print(tsname)
        ts = tszip.decompress(tsname)
        relevantids = []
        #modern individuals are numbered 0 through 3753
        pop_metadata = [json.loads(pop.metadata) for pop in ts.populations()]

        TentativeSpaces = numpy.arange(0, 300000000, step = Spacing)
        treeindex = -1
        TREEINDICES = []
        for polytree in ts.trees():
            treeindex = treeindex + 1
            if (polytree.num_roots == 1):
                left = polytree.interval[0]
                right = polytree.interval[1]
                treecount = 0
                for i in TentativeSpaces:
                    if i >= left and i < right:
                        treecount = treecount + 1
                TREEINDICES.append(treecount)
            else:
                TREEINDICES.append(0)
        
        treeindex = -1
        for polytree in ts.trees():
            treeindex = treeindex + 1

            if TREEINDICES[treeindex] > 0:
                inddivindex = 0
                for i in range(3753+1):
                    ind = ts.individual(i)
                    ind_node0 = ts.node(ind.nodes[0])
                    ind_node1 = ts.node(ind.nodes[1])

                    if ( pop_metadata[ind_node0.population]["name"]) != ( pop_metadata[ind_node1.population]["name"]):
                        print("PROBLEM")
                    if pop_metadata[ind_node0.population]["name"] == pop:
                        relevantids = [ind_node0.id, ind_node1.id]
                        inddivindex = inddivindex + 1
                        if inddivindex == 4: break
                        for iii in range(TREEINDICES[treeindex]):
                            LISTOFTIMES[timesindex] = polytree.tmrca(relevantids[0],relevantids[1])
                            timesindex = timesindex + 1

    numpy.savetxt("./" + pop  +  ".csv", LISTOFTIMES, delimiter=",")
