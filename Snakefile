include: "rules/simulate_50_arg.smk"

rule all:
    input:
        sim_50_arg = expand("results/simulated_ts/sim_50_{x}.trees", x=range(10)),
        sim_50_vcf = expand("results/simulated_vcf/sim_50_{x}.vcf", x=range(10))
