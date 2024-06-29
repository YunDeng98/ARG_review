rule plot_allele_relate_300:
    input:
        relate_ts = "results/relate_ts/allele_relate_300.txt"
    output:
        allele_plot = "results/figures/allele_relate_300.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/plot_allele_relate_300.py"

rule plot_allele_relate_300_done:
    input:
        allele_plot = "results/figures/allele_relate_300.png",
    shell:
        """
        echo "Allele plot for relate ARG inference for 300 sequences are completed."
        """
