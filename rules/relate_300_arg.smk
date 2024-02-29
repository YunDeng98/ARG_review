rule relate_300_arg:
    input:
        sim_vcf = "results/simulated_vcf/sim_300_{x}.vcf"
    output:
        inferred_ts = "results/relate_ts/relate_300_{x}.trees",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/relate_300_arg.py"

rule relate_300_arg_done:
    input:
        inferred_ts_files = expand("results/relate_ts/relate_300_{x}.trees", x=range(10)),
    shell:
        """
        echo "Relate ARG inference for 300 sequences are completed."
        """
