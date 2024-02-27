rule simulate_50_arg:
    input:
        script = "scripts/simulate_50_arg.py"
    output:
        ts = "results/simulated_ts/sim_50_{x}.trees",
        vcf = "results/simulated_vcf/sim_50_{x}.vcf"
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/simulate_50_arg.py"

rule trees_done:
    input:
        ts_files = expand("results/simulated_ts/sim_50_{x}.trees", x=range(10)),
        vcf_files = expand("results/simulated_vcf/sim_50_{x}.vcf", x=range(10))
    shell:
        """
        echo "All ARG simulations and VCF generations with 50 sequences are completed."
        """
