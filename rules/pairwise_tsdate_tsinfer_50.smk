rule pairwise_tsdate_tsinfer_50:
    input:
        tsdate_tsinfer_ts = expand("results/tsdate_tsinfer_ts/tsdate_tsinfer_50_{x}.trees", x=range(10))
    output:
        pairwise_figure = "results/figures/pairwise_tsdate_tsinfer_50.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/pairwise_tsdate_tsinfer_50.py"

rule pairwise_tsdate_tsinfer_50_done:
    input:
        inferred_ts_files = expand("results/tsdate_tsinfer_ts/tsdate_tsinfer_50_{x}.trees", x=range(10)),
    shell:
        """
        echo "Pairwise plots for tsdate+tsinfer ARG inference for 50 sequences are completed."
        """
