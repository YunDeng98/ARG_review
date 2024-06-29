rule plot_allele_tsdate_tsinfer_50:
    input:
        tsdate_tsinfer_ts = "results/tsdate_tsinfer_ts/allele_tsdate_tsinfer_50.txt"
    output:
        allele_plot = "results/figures/allele_tsdate_tsinfer_50.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/plot_allele_tsdate_tsinfer_50.py"

rule plot_allele_tsdate_tsinfer_50_done:
    input:
        allele_plot = "results/figures/allele_tsdate_tsinfer_50.png",
    shell:
        """
        echo "Allele plot for tsdate_tsinfer ARG inference for 50 sequences are completed."
        """
