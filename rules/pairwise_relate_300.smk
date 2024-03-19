rule pairwise_relate_300:
    input:
        relate_ts = expand("results/relate_ts/relate_300_{x}.trees", x=range(10))
    output:
        pairwise_figure = "results/figures/pairwise_relate_300.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/pairwise_relate_300.py"

rule pairwise_relate_300_done:
    input:
        inferred_ts_files = expand("results/relate_ts/relate_300_{x}.trees", x=range(10)),
    shell:
        """
        echo "Pairwise plots for relate ARG inference for 300 sequences are completed."
        """
