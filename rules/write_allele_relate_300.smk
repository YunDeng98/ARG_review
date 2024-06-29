rule write_allele_relate_300:
    input:
        relate_ts = expand("results/relate_ts/relate_300_{x}.trees", x=range(10))
    output:
        allele_file = "results/relate_ts/allele_relate_300.txt",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/write_allele_relate_300.py"

rule write_allele_relate_300_done:
    input:
        allele_file = "results/relate_ts/allele_relate_300.txt",
    shell:
        """
        echo "Allele ages for relate ARG inference for 300 sequences are completed."
        """
