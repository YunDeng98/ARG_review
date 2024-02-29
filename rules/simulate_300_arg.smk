rule simulate_300_arg:
    input:
        script = "scripts/simulate_300_arg.py"
    output:
        ts = "results/simulated_ts/sim_300_{x}.trees",
        vcf = "results/simulated_vcf/sim_300_{x}.vcf"
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/simulate_300_arg.py"

rule sim_300_arg_done:
    input:
        ts_files = expand("results/simulated_ts/sim_300_{x}.trees", x=range(10)),
        vcf_files = expand("results/simulated_vcf/sim_300_{x}.vcf", x=range(10))
    shell:
        """
        echo "All ARG simulations and VCF generations with 300 sequences are completed."
        """
