rule singer_300_arg:
    input:
        sim_vcf = "results/simulated_vcf/sim_300_{x}.vcf"
    output:
        inferred_ts = "results/singer_ts/singer_300_{x}_99.trees",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/singer_300_arg.py"

rule singer_300_arg_done:
    input:
        inferred_ts_files = expand("results/singer_ts/singer_300_{x}_99.trees", x=range(10)),
    shell:
        """
        echo "SINGER ARG inference for 300 sequences are completed."
        """
