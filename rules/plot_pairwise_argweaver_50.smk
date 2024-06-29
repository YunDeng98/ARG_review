rule plot_pairwise_argweaver_50:
    input:
        argweaver_ts = "results/argweaver_ts/pairwise_argweaver_50.txt"
    output:
        pairwise_plot = "results/figures/pairwise_argweaver_50.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/plot_pairwise_argweaver_50.py"

rule plot_pairwise_argweaver_50_done:
    input:
        pairwise_plot = "results/figures/pairwise_argweaver_50.png",
    shell:
        """
        echo "Pairwise plot for argweaver ARG inference for 50 sequences are completed."
        """
