rule write_pairwise_argweaver_50:
    input:
        argweaver_ts = expand("results/argweaver_ts/argweaver_50_{x}.2960.trees", x=range(10))
    output:
        pairwise_file = "results/argweaver_ts/pairwise_argweaver_50.txt",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/write_pairwise_argweaver_50.py"

rule write_pairwise_argweaver_50_done:
    input:
        pairwise_file = "results/argweaver_ts/pairwise_argweaver_50.txt",
    shell:
        """
        echo "Pairwise coalescence for argweaver ARG inference for 50 sequences are completed."
        """
