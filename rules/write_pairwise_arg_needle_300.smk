rule write_pairwise_arg_needle_300:
    input:
        arg_needle_ts = expand("results/arg_needle_ts/arg_needle_300_{x}.trees", x=range(10))
    output:
        pairwise_file = "results/arg_needle_ts/pairwise_arg_needle_300.txt",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/write_pairwise_arg_needle_300.py"

rule pairwise_arg_needle_300_done:
    input:
        pairwise_file = "results/arg_needle_ts/pairwise_arg_needle_300.txt",
    shell:
        """
        echo "Pairwise coalescence for arg_needle ARG inference for 300 sequences are completed."
        """
