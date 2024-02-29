rule argweaver_50_arg:
    input:
        sim_vcf = "results/simulated_vcf/sim_50_{x}.vcf"
    output:
        inferred_ts = "results/argweaver_ts/argweaver_50_{x}.trees",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/argweaver_50_arg.py"

rule argweaver_50_arg_done:
    input:
        inferred_ts_files = expand("results/argweaver_ts/argweaver_50_{x}.trees", x=range(10)),
    shell:
        """
        echo "ARGweaver ARG inference for 50 sequences are completed."
        """
