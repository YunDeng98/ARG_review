rule write_pairwise_tsdate_tsinfer_50:
    input:
        tsdate_tsinfer_ts = expand("results/tsdate_tsinfer_ts/tsdate_tsinfer_50_{x}.trees", x=range(10))
    output:
        pairwise_file = "results/tsdate_tsinfer_ts/pairwise_tsdate_tsinfer_50.txt",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/write_pairwise_tsdate_tsinfer_50.py"

rule write_pairwise_tsdate_tsinfer_50_done:
    input:
        pairwise_file = "results/tsdate_tsinfer_ts/pairwise_tsdate_tsinfer_50.txt"
    shell:
        """
        echo "Pairwise coalescence for tsdate+tsinfer ARG inference for 50 sequences are completed."
        """
