rule plot_allele_relate_50:
    input:
        relate_ts = "results/relate_ts/allele_relate_50.txt"
    output:
        allele_plot = "results/figures/allele_relate_50.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/plot_allele_relate_50.py"

rule plot_allele_relate_50_done:
    input:
        allele_plot = "results/figures/allele_relate_50.png",
    shell:
        """
        echo "Allele plot for relate ARG inference for 50 sequences are completed."
        """
