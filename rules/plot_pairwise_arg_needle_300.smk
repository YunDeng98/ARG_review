rule plot_pairwise_arg_needle_300:
    input:
        arg_needle_ts = "results/arg_needle_ts/pairwise_arg_needle_300.txt"
    output:
        pairwise_plot = "results/figures/pairwise_arg_needle_300.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/plot_pairwise_arg_needle_300.py"

rule plot_pairwise_arg_needle_300_done:
    input:
        pairwise_plot = "results/figures/pairwise_arg_needle_300.png",
    shell:
        """
        echo "Pairwise plot for arg_needle ARG inference for 300 sequences are completed."
        """
