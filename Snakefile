include: "rules/simulate_50_arg.smk"
include: "rules/simulate_300_arg.smk"
include: "rules/tsdate_tsinfer_50_arg.smk"
include: "rules/tsdate_tsinfer_300_arg.smk"
include: "rules/relate_50_arg.smk"
include: "rules/relate_300_arg.smk"
include: "rules/argweaver_50_arg.smk"
include: "rules/singer_50_arg.smk"
include: "rules/singer_300_arg.smk"
include: "rules/arg_needle_300_arg.smk"
include: "rules/pairwise_relate_50.smk"
include: "rules/pairwise_relate_300.smk"
include: "rules/pairwise_tsdate_tsinfer_50.smk"
include: "rules/pairwise_tsdate_tsinfer_300.smk"
include: "rules/pairwise_argweaver_50.smk"
include: "rules/pairwise_arg_needle_300.smk"

rule all:
    input:
        sim_50_arg = expand("results/simulated_ts/sim_50_{x}.trees", x=range(10)),
        sim_50_vcf = expand("results/simulated_vcf/sim_50_{x}.vcf", x=range(10)),
        sim_300_arg = expand("results/simulated_ts/sim_300_{x}.trees", x=range(10)),
        sim_300_vcf = expand("results/simulated_vcf/sim_300_{x}.vcf", x=range(10)),
        tsdate_tsinfer_50_arg = expand("results/tsdate_tsinfer_ts/tsdate_tsinfer_50_{x}.trees", x=range(10)),
        tsdate_tsinfer_300_arg = expand("results/tsdate_tsinfer_ts/tsdate_tsinfer_300_{x}.trees", x=range(10)),
        relate_50_arg = expand("results/relate_ts/relate_50_{x}.trees", x=range(10)),
        relate_300_arg = expand("results/relate_ts/relate_300_{x}.trees", x=range(10)),
        argweaver_50_arg = expand("results/argweaver_ts/argweaver_50_{x}.2960.trees", x=range(10)),
        arg_needle_300_arg = expand("results/arg_needle_ts/arg_needle_300_{x}.trees", x=range(10)),
        singer_50_arg = expand("results/singer_ts/singer_50_{x}_99.trees", x=range(10)),
        singer_300_arg = expand("results/singer_ts/singer_300_{x}_99.trees", x=range(10)),
        pairwise_relate_50 = "results/figures/pairwise_relate_50.png",
        pairwise_relate_300 = "results/figures/pairwise_relate_300.png",
        pairwise_tsdate_tsinfer_50 = "results/figures/pairwise_tsdate_tsinfer_50.png",
        pairwise_tsdate_tsinfer_300 = "results/figures/pairwise_tsdate_tsinfer_300.png",
        pairwise_argweaver_50 = "results/figures/pairwise_argweaver_50.png",
        pairwise_arg_needle_300 = "results/figures/pairwise_arg_needle_300.png"
