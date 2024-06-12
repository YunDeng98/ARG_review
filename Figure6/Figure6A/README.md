# Guide to Reproducing Figure 6A (tsinfer+tsdate analysis)

1) Download tsinfer+tsdate inferred tree sequences from [https://zenodo.org/records/5495535](https://zenodo.org/records/5495535).
2) Change file path on line 6 of getTMRCA.py (path_to_chroms = "./5495535") to refer to the file path on your machine to the directory of inferred tree sequences. It is "./5495535" by default as "5495535" is the default name of the folder of tree sequences.
3) Run 

```
python getTMRCA.py 
```
This will generate 4 files. "Quechua.csv", "GBR.csv", "YRI.csv", and "CHB.csv". Each file lists the pairwise TMRCAs for a set of individuals from that population, taken every 10 kilobases across the genome. Some extra values of "-1" are appended to each list of times (for code-specific reasons).
4) Run

```
Rscript makePlot.R
```
This will produce a set of histograms of pairwise TMRCAs for each population (identical to Figure 6A). It assumes the files produced in the previous step are in the current working directory. The values of -1 in the lists are stripped out.

Feel free to contact [Andrew Vaughn](ahv36@berkeley.edu) if you have questions about this analysis.