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
include: "rules/write_pairwise_relate_50.smk"
include: "rules/write_pairwise_relate_300.smk"
include: "rules/write_pairwise_tsdate_tsinfer_50.smk"
include: "rules/write_pairwise_tsdate_tsinfer_300.smk"
include: "rules/write_pairwise_argweaver_50.smk"
include: "rules/write_pairwise_arg_needle_300.smk"
include: "rules/write_pairwise_singer_50.smk"
include: "rules/write_pairwise_singer_300.smk"
include: "rules/plot_pairwise_relate_50.smk"
include: "rules/plot_pairwise_relate_300.smk"
include: "rules/plot_pairwise_tsdate_tsinfer_50.smk"
include: "rules/plot_pairwise_tsdate_tsinfer_300.smk"
include: "rules/plot_pairwise_argweaver_50.smk"
include: "rules/plot_pairwise_arg_needle_300.smk"
include: "rules/plot_pairwise_singer_50.smk"
include: "rules/plot_pairwise_singer_300.smk"
include: "rules/write_allele_relate_50.smk"
include: "rules/write_allele_relate_300.smk"
include: "rules/write_allele_tsdate_tsinfer_50.smk"
include: "rules/write_allele_tsdate_tsinfer_300.smk"
include: "rules/write_allele_singer_50.smk"
include: "rules/write_allele_singer_300.smk"
include: "rules/plot_allele_relate_50.smk"
include: "rules/plot_allele_relate_300.smk"
include: "rules/plot_allele_tsdate_tsinfer_50.smk"
include: "rules/plot_allele_tsdate_tsinfer_300.smk"
include: "rules/plot_allele_singer_50.smk"
include: "rules/plot_allele_singer_300.smk"



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
        pairwise_relate_50 = "results/relate_ts/pairwise_relate_50.txt",
        pairwise_relate_300 = "results/relate_ts/pairwise_relate_300.txt",
        pairwise_tsdate_tsinfer_50 = "results/tsdate_tsinfer_ts/pairwise_tsdate_tsinfer_50.txt",
        pairwise_tsdate_tsinfer_300 = "results/tsdate_tsinfer_ts/pairwise_tsdate_tsinfer_300.txt",
        pairwise_argweaver_50 = "results/argweaver_ts/pairwise_argweaver_50.txt",
        pairwise_arg_needle_300 = "results/arg_needle_ts/pairwise_arg_needle_300.txt",
        pairwise_singer_50 = "results/singer_ts/pairwise_singer_50.txt",
        pairwise_singer_300 = "results/singer_ts/pairwise_singer_300.txt",
        plot_relate_50 = "results/figures/pairwise_relate_50.png",
        plot_relate_300 = "results/figures/pairwise_relate_300.png",
        plot_tsdate_tsinfer_50 = "results/figures/pairwise_tsdate_tsinfer_50.png",
        plot_tsdate_tsinfer_300 = "results/figures/pairwise_tsdate_tsinfer_300.png",
        plot_argweaver_50 = "results/figures/pairwise_argweaver_50.png",
        plot_arg_needle_300 = "results/figures/pairwise_arg_needle_300.png",
        plot_singer_50 = "results/figures/pairwise_singer_50.png",
        plot_singer_300 = "results/figures/pairwise_singer_300.png",
        allele_relate_50 = "results/relate_ts/allele_relate_50.txt",
        allele_relate_300 = "results/relate_ts/allele_relate_300.txt",
        allele_tsdate_tsinfer_50 = "results/tsdate_tsinfer_ts/allele_tsdate_tsinfer_50.txt",
        allele_tsdate_tsinfer_300 = "results/tsdate_tsinfer_ts/allele_tsdate_tsinfer_300.txt",
        allele_singer_50 = "results/singer_ts/allele_singer_50.txt",
        allele_singer_300 = "results/singer_ts/allele_singer_300.txt",
        plot_allele_relate_50 = "results/figures/allele_relate_50.png",
        plot_allele_relate_300 = "results/figures/allele_relate_300.png",
        plot_allele_tsdate_tsinfer_50 = "results/figures/allele_tsdate_tsinfer_50.png",
        plot_allele_tsdate_tsinfer_300 = "results/figures/allele_tsdate_tsinfer_300.png",
        plot_allele_singer_50 = "results/figures/allele_singer_50.png",
        plot_allele_singer_300 = "results/figures/allele_singer_300.png"
