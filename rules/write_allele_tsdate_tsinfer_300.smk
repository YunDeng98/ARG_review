rule write_allele_tsdate_tsinfer_300:
    input:
        tsdate_tsinfer_ts = expand("results/tsdate_tsinfer_ts/tsdate_tsinfer_300_{x}.trees", x=range(10))
    output:
        allele_file = "results/tsdate_tsinfer_ts/allele_tsdate_tsinfer_300.txt",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/write_allele_tsdate_tsinfer_300.py"

rule write_allele_tsdate_tsinfer_300_done:
    input:
        allele_file = "results/tsdate_tsinfer_ts/allele_tsdate_tsinfer_300.txt",
    shell:
        """
        echo "Allele ages for tsdate_tsinfer ARG inference for 300 sequences are completed."
        """
