rule arg_needle_300_arg:
    input:
        sim_vcf = "results/simulated_vcf/sim_300_{x}.vcf"
    output:
        inferred_ts = "results/arg_needle_ts/arg_needle_300_{x}.trees",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/arg_needle_300_arg.py"

rule arg_needle_300_arg_done:
    input:
        inferred_ts_files = expand("results/arg_needle_ts/arg_needle_300_{x}.trees", x=range(10)),
    shell:
        """
        echo "ARG-Needle ARG inference for 300 sequences are completed."
        """
