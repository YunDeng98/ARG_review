rule plot_allele_tsdate_tsinfer_300:
    input:
        tsdate_tsinfer_ts = "results/tsdate_tsinfer_ts/allele_tsdate_tsinfer_300.txt"
    output:
        allele_plot = "results/figures/allele_tsdate_tsinfer_300.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/plot_allele_tsdate_tsinfer_300.py"

rule plot_allele_tsdate_tsinfer_300_done:
    input:
        allele_plot = "results/figures/allele_tsdate_tsinfer_300.png",
    shell:
        """
        echo "Allele plot for tsdate_tsinfer ARG inference for 300 sequences are completed."
        """
