rule write_pairwise_relate_300:
    input:
        relate_ts = expand("results/relate_ts/relate_300_{x}.trees", x=range(10))
    output:
        pairwise_file = "results/relate_ts/pairwise_relate_300.txt",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/write_pairwise_relate_300.py"

rule pairwise_relate_300_done:
    input:
        pairwise_file = "results/relate_ts/pairwise_relate_300.txt",
    shell:
        """
        echo "Pairwise coalescence for relate ARG inference for 300 sequences are completed."
        """
