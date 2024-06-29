rule write_allele_relate_50:
    input:
        relate_ts = expand("results/relate_ts/relate_50_{x}.trees", x=range(10))
    output:
        allele_file = "results/relate_ts/allele_relate_50.txt",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/write_allele_relate_50.py"

rule write_allele_relate_50_done:
    input:
        allele_file = "results/relate_ts/allele_relate_50.txt",
    shell:
        """
        echo "Allele ages for relate ARG inference for 50 sequences are completed."
        """
