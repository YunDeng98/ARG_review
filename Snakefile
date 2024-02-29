include: "rules/simulate_50_arg.smk"
include: "rules/simulate_300_arg.smk"
include: "rules/tsdate_tsinfer_50_arg.smk"
include: "rules/tsdate_tsinfer_300_arg.smk"
include: "rules/relate_50_arg.smk"
include: "rules/relate_300_arg.smk"


rule all:
    input:
        sim_50_arg = expand("results/simulated_ts/sim_50_{x}.trees", x=range(10)),
        sim_50_vcf = expand("results/simulated_vcf/sim_50_{x}.vcf", x=range(10)),
        sim_300_arg = expand("results/simulated_ts/sim_300_{x}.trees", x=range(10)),
        sim_300_vcf = expand("results/simulated_vcf/sim_300_{x}.vcf", x=range(10)),
        tsdate_tsinfer_50_arg = expand("results/tsdate_tsinfer_ts/tsdate_tsinfer_50_{x}.trees", x=range(10)),
        tsdate_tsinfer_300_arg = expand("results/tsdate_tsinfer_ts/tsdate_tsinfer_300_{x}.trees", x=range(10)),
        relate_50_arg = expand("results/relate_ts/relate_50_{x}.trees", x=range(10)),
        relate_300_arg = expand("results/relate_ts/relate_300_{x}.trees", x=range(10))
