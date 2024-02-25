rule simulate_arg:
    input:
        script = "scripts/simulate_arg.py"
    output:
        50_ts = "results/simulated_ts/sim_50_{x}.trees",
        50_vcf = "results/simulated_vcf/standard_ts_{x}.vcf"
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/simulate_standard_ts.py"

rule trees_done:
    input:
        ts_files = expand("results/simulated_ts/standard_ts_{x}.trees", x=range(10)),
        vcf_files = expand("results/simulated_vcf/standard_ts_{x}.vcf", x=range(10))
    shell:
        """
        echo "All standard tree simulations and VCF generations completed."
        """
