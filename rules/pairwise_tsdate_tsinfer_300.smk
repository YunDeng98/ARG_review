rule pairwise_tsdate_tsinfer_300:
    input:
        tsdate_tsinfer_ts = expand("results/tsdate_tsinfer_ts/tsdate_tsinfer_300_{x}.trees", x=range(10))
    output:
        pairwise_figure = "results/figures/pairwise_tsdate_tsinfer_300.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/pairwise_tsdate_tsinfer_300.py"

rule pairwise_tsdate_tsinfer_300_done:
    input:
        inferred_ts_files = expand("results/tsdate_tsinfer_ts/tsdate_tsinfer_300_{x}.trees", x=range(10)),
    shell:
        """
        echo "Pairwise plots for tsdate+tsinfer ARG inference for 300 sequences are completed."
        """
