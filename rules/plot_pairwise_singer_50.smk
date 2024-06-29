rule plot_pairwise_singer_50:
    input:
        singer_ts = "results/relate_ts/pairwise_relate_50.txt"
    output:
        pairwise_plot = "results/figures/pairwise_singer_50.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/plot_pairwise_singer_50.py"

rule plot_pairwise_singer_50_done:
    input:
        pairwise_plot = "results/figures/pairwise_singer_50.png",
    shell:
        """
        echo "Pairwise plot for singer ARG inference for 50 sequences are completed."
        """
