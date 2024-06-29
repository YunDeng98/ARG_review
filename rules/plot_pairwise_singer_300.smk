rule plot_pairwise_singer_300:
    input:
        singer_ts = "results/relate_ts/pairwise_relate_300.txt"
    output:
        pairwise_plot = "results/figures/pairwise_singer_300.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/plot_pairwise_singer_300.py"

rule plot_pairwise_singer_300_done:
    input:
        pairwise_plot = "results/figures/pairwise_singer_300.png",
    shell:
        """
        echo "Pairwise plot for singer ARG inference for 300 sequences are completed."
        """
