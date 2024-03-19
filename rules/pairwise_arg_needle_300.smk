rule pairwise_arg_needle_300:
    input:
        arg_needle_ts = expand("results/arg_needle_ts/arg_needle_300_{x}.trees", x=range(10))
    output:
        pairwise_figure = "results/figures/pairwise_arg_needle_300.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/pairwise_arg_needle_300.py"

rule pairwise_arg_needle_300_done:
    input:
        inferred_ts_files = expand("results/arg_needle_ts/arg_needle_300_{x}.trees", x=range(10)),
    shell:
        """
        echo "Pairwise plots for arg_needle ARG inference for 300 sequences are completed."
        """
