rule relate_50_arg:
    input:
        sim_vcf = "results/simulated_vcf/sim_50_{x}.vcf"
    output:
        inferred_ts = "results/relate_ts/relate_50_{x}.trees",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/relate_50_arg.py"

rule relate_50_arg_done:
    input:
        inferred_ts_files = expand("results/relate_ts/relate_50_{x}.trees", x=range(10)),
    shell:
        """
        echo "Relate ARG inference for 50 sequences are completed."
        """
