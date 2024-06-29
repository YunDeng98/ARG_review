rule write_allele_tsdate_tsinfer_50:
    input:
        tsdate_tsinfer_ts = expand("results/tsdate_tsinfer_ts/tsdate_tsinfer_50_{x}.trees", x=range(10))
    output:
        allele_file = "results/tsdate_tsinfer_ts/allele_tsdate_tsinfer_50.txt",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/write_allele_tsdate_tsinfer_50.py"

rule write_allele_tsdate_tsinfer_50_done:
    input:
        allele_file = "results/tsdate_tsinfer_ts/allele_tsdate_tsinfer_50.txt",
    shell:
        """
        echo "Allele ages for tsdate_tsinfer ARG inference for 50 sequences are completed."
        """
