rule write_pairwise_singer_300:
    input:
        singer_ts = expand("results/singer_ts/singer_300_{x}_99.trees", x=range(10))
    output:
        pairwise_file = "results/singer_ts/pairwise_singer_300.txt",
    conda:"../envs/tskit.yaml"
    script:
        "../scripts/write_pairwise_singer_300.py"

rule write_pairwise_singer_300_done:
    input:
        pairwise_file = "results/singer_ts/pairwise_singer_300.txt",
    shell:
        """
        echo "Pairwise coalescence for singer ARG inference for 300 sequences are completed."
        """
