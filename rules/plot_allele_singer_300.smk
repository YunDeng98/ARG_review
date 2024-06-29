rule plot_allele_singer_300:
    input:
        singer_ts = "results/singer_ts/allele_singer_300.txt"
    output:
        allele_plot = "results/figures/allele_singer_300.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/plot_allele_singer_300.py"

rule plot_allele_singer_300_done:
    input:
        allele_plot = "results/figures/allele_singer_300.png",
    shell:
        """
        echo "Allele plot for singer ARG inference for 300 sequences are completed."
        """
