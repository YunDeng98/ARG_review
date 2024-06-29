rule write_pairwise_relate_50:
    input:
        relate_ts = expand("results/relate_ts/relate_50_{x}.trees", x=range(10))
    output:
        pairwise_file = "results/relate_ts/pairwise_relate_50.txt",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/write_pairwise_relate_50.py"

rule write_pairwise_relate_50_done:
    input:
        pairwise_file = "results/relate_ts/pairwise_relate_50.txt",
    shell:
        """
        echo "Pairwise coalescence for relate ARG inference for 50 sequences are completed."
        """
