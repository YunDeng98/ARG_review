rule plot_pairwise_relate_50:
    input:
        relate_ts = "results/relate_ts/pairwise_relate_50.txt"
    output:
        pairwise_plot = "results/figures/pairwise_relate_50.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/plot_pairwise_relate_50.py"

rule plot_pairwise_relate_50_done:
    input:
        pairwise_plot = "results/figures/pairwise_relate_50.png",
    shell:
        """
        echo "Pairwise plot for relate ARG inference for 50 sequences are completed."
        """
