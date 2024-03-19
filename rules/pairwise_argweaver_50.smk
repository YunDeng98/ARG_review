rule pairwise_argweaver_50:
    input:
        argweaver_ts = expand("results/argweaver_ts/argweaver_50_{x}.2960.trees", x=range(10))
    output:
        pairwise_figure = "results/figures/pairwise_argweaver_50.png",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/pairwise_argweaver_50.py"

rule pairwise_argweaver_50_done:
    input:
        inferred_ts_files = expand("results/argweaver_ts/argweaver_50_{x}.trees", x=range(10)),
    shell:
        """
        echo "Pairwise plots for argweaver ARG inference for 50 sequences are completed."
        """
