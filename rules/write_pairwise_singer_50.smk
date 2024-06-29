rule write_pairwise_singer_50:
    input:
        singer_ts = expand("results/singer_ts/singer_50_{x}_99.trees", x=range(10))
    output:
        pairwise_file = "results/singer_ts/pairwise_singer_50.txt",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/write_pairwise_singer_50.py"

rule write_pairwise_singer_50_done:
    input:
        pairwise_file = "results/singer_ts/pairwise_singer_50.txt",
    shell:
        """
        echo "Pairwise coalescence for singer ARG inference for 50 sequences are completed."
        """
