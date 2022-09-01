# QBB2022 - Day 3 - Homework Exercises Submission
E1.  
`$ cp /Users/cmdb/data/vcf_files/ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz .`  
`$ plink --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --out plink --const-fid --allow-extra-chr --pca 3`  
  
E2.  
Answer:  
Obvious incontinuity exists in both figure. The individuals can be divided into several subgroups. And these subgroups have quite distinct genotype patterns from each other. This is possibly because the different subgroups have been facing quite different natural selection conditions, which can lead to divergent genotype landscapes. And different natural selection can be caused by geological isolation, assortative mating, ect..
  
E3.  
`$ cp /Users/cmdb/data/metadata_and_txt_files/integrated_call_samples.panel .`  
`$ wc -l integrated_call_samples.panel`  
`3584`  
`$ sort -k 1 integrated_call_samples.panel | head -n 3583 > integrated_call_samples_sorted.txt`  
`$ sort -k 2 plink.eigenvec > plink_sorted.txt`  
`$ cat -t plink_sorted.txt | head -n 5`  
`0 HG00096 -0.0109316 -0.0249319 0.00534958`  
`0 HG00097 -0.0121359 -0.0290234 0.0192942`  
`0 HG00099 -0.0127633 -0.0249592 0.00975894`  
`0 HG00100 -0.0121159 -0.0242888 0.0161956`  
`0 HG00101 -0.013234 -0.0269284 0.0143007`  
`$ cat -t integrated_call_samples_sorted.txt | head -n 5`  
`HG00096^IGBR^IEUR^Imale`  
`HG00097^IGBR^IEUR^Ifemale`  
`HG00098^IGBR^IEUR^Imale`  
`HG00099^IGBR^IEUR^Ifemale`  
`HG00100^IGBR^IEUR^Ifemale`  
`$ awk -v OFS="\t" '{$1=$1;print}' plink_sorted.txt > plink_sorted_TAB.txt`  
`$ join -1 2 -2 1 plink_sorted_TAB.txt integrated_call_samples_sorted.txt > joined.txt`  
