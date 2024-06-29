rule plot_pairwise_tsdate_tsinfer_50:
    input:
        tsdate_tsinfer_ts = "results/tsdate_tsinfer_ts/pairwise_tsdate_tsinfer_50.txt"
    output:
        pairwise_plot = "results/figures/pairwise_tsdate_tsinfer_50.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/plot_pairwise_tsdate_tsinfer_50.py"

rule plot_pairwise_tsdate_tsinfer_50_done:
    input:
        pairwise_plot = "results/figures/pairwise_tsdate_tsinfer_50.png",
    shell:
        """
        echo "Pairwise plot for tsdate_tsinfer ARG inference for 50 sequences are completed."
        """
