rule singer_50_arg:
    input:
        sim_vcf = "results/simulated_vcf/sim_50_{x}.vcf"
    output:
        inferred_ts = "results/singer_ts/singer_50_{x}_99.trees",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/singer_50_arg.py"

rule singer_50_arg_done:
    input:
        inferred_ts_files = expand("results/singer_ts/singer_50_{x}_99.trees", x=range(10)),
    shell:
        """
        echo "SINGER ARG inference for 50 sequences are completed."
        """
