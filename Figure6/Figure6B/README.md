# Guide to Reproducing Figure 6B (Relate analysis)

This analysis requires [vcftools](https://vcftools.github.io/man_latest.html) and [Relate](https://myersgroup.github.io/relate/).

1) Download 1000 Genomes Project chromosome 1 (file ALL.chr1.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz) from [http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/](http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/). We will call the resulting unzipped vcf file Chr1.vcf.
2) Run 

```
vcftools --vcf Chr1.vcf --keep RelevantIDs.txt --recode --recode-INFO-all --out temp

vcftools --vcf temp.recode.vcf --mac 1 --recode --recode-INFO-all --out final

PATHTORELATE/bin/RelateFileFormats --mode ConvertFromVcf --haps Input.haps --sample Input.sample -i final.recode
```
This filters the full dataset for our relevant subset of IDs and converts the format to the input format for Relate


3) Obtain the chromosome 1 human ancestral sequence "human_ancestor_1.fa" from [https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase1/analysis_results/supporting/ancestral_alignments/](https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase1/analysis_results/supporting/ancestral_alignments/). We provide thr strict genomic mask "20140520.chr1.strict_mask.fasta" from [https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/supporting/accessible_genome_masks/StrictMask/](https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/supporting/accessible_genome_masks/StrictMask/)  and the genetic map "genetic_map_chr1_combined_b37.txt" which has been converted to the file format required by Relate.

4) Run

```
PATHTORELATE/scripts/PrepareInputFiles/PrepareInputFiles.sh  --haps Input.haps  --sample Input.sample  --ancestor human_ancestor_1.fa   --mask  20140520.chr1.strict_mask.fasta -o Step2 --poplabels poplabels.txt

PATHTORELATE/bin/Relate      --mode All   -m 1.25e-8     -N 30000  \
      --haps Step2.haps.gz \
      --sample Step2.sample.gz \
      --map  genetic_map_chr1_combined_b37.txt\
      --seed 50 \
      -o Chrom1 \
      --annot Step2.annot \
      --dist Step2.dist.gz 

PATHTORELATE/scripts/EstimatePopulationSize/EstimatePopulationSize.sh    -i Chrom1 -m 1.25e-8 --years_per_gen 28 --threads 2  --seed 60 --output InferenceNew --poplabels  poplabels.txt  --pop_of_interest CHB,FIN,GBR,YRI

Rscript PlotCoals.R
```
This will produce the Relate-estimated historic population sizes for each of the 4 populations, as shown in Figure 6B.


Feel free to contact [Andrew Vaughn](ahv36@berkeley.edu) if you have questions about this analysis.