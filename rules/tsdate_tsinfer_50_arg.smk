rule tsdate_tsinfer_50_arg:
    input:
        sim_ts = "results/simulated_ts/sim_50_{x}.trees"
    output:
        inferred_ts = "results/tsdate_tsinfer_ts/tsdate_tsinfer_50_{x}.trees",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/tsdate_tsinfer_50_arg.py"

rule tsdate_tsinfer_50_arg_done:
    input:
        inferred_ts_files = expand("results/tsdate_tsinfer_ts/tsdate_tsinfer_50_{x}.trees", x=range(10)),
    shell:
        """
        echo "Tsdate+tsinfer ARG inference for 50 sequences are completed."
        """
