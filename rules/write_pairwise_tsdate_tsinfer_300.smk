rule write_pairwise_tsdate_tsinfer_300:
    input:
        tsdate_tsinfer_ts = expand("results/tsdate_tsinfer_ts/tsdate_tsinfer_300_{x}.trees", x=range(10))
    output:
        pairwise_file = "results/tsdate_tsinfer_ts/pairwise_tsdate_tsinfer_300.txt",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/write_pairwise_tsdate_tsinfer_300.py"

rule write_pairwise_tsdate_tsinfer_300_done:
    input:
        pairwise_file = "results/tsdate_tsinfer_ts/pairwise_tsdate_tsinfer_300.txt",
    shell:
        """
        echo "Pairwise coalescence for tsdate+tsinfer ARG inference for 300 sequences are completed."
        """
