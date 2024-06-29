rule write_allele_singer_300:
    input:
        singer_ts = expand("results/singer_ts/singer_300_{x}_99.trees", x=range(10))
    output:
        allele_file = "results/singer_ts/allele_singer_300.txt",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/write_allele_singer_300.py"

rule write_allele_singer_300_done:
    input:
        allele_file = "results/singer_ts/allele_singer_300.txt",
    shell:
        """
        echo "Allele ages for singer ARG inference for 300 sequences are completed."
        """
