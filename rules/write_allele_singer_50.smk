rule write_allele_singer_50:
    input:
        singer_ts = expand("results/singer_ts/singer_50_{x}_99.trees", x=range(10))
    output:
        allele_file = "results/singer_ts/allele_singer_50.txt",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/write_allele_singer_50.py"

rule write_allele_singer_50_done:
    input:
        allele_file = "results/singer_ts/allele_singer_50.txt",
    shell:
        """
        echo "Allele ages for singer ARG inference for 50 sequences are completed."
        """
