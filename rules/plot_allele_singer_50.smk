rule plot_allele_singer_50:
    input:
        singer_ts = "results/singer_ts/allele_singer_50.txt"
    output:
        allele_plot = "results/figures/allele_singer_50.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/plot_allele_singer_50.py"

rule plot_allele_singer_50_done:
    input:
        allele_plot = "results/figures/allele_singer_50.png",
    shell:
        """
        echo "Allele plot for singer ARG inference for 50 sequences are completed."
        """
