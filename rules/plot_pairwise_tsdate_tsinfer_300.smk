rule plot_pairwise_tsdate_tsinfer_300:
    input:
        tsdate_tsinfer_ts = "results/tsdate_tsinfer_ts/pairwise_tsdate_tsinfer_300.txt"
    output:
        pairwise_plot = "results/figures/pairwise_tsdate_tsinfer_300.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/plot_pairwise_tsdate_tsinfer_300.py"

rule plot_pairwise_tsdate_tsinfer_300_done:
    input:
        pairwise_plot = "results/figures/pairwise_tsdate_tsinfer_300.png",
    shell:
        """
        echo "Pairwise plot for tsdate_tsinfer ARG inference for 300 sequences are completed."
        """
