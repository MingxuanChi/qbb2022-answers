# QBB2022 - Day 1 - Homework Exercises Submission

1.
Error: Instead of a variable in the given data source file, the variable 'nuc' is a variable defined in the script. When `awk` wants to use it, we need to add `nuc` into `awk` expression as an external variable. Thus, we can use option `-v`, and remove the $ before `nuc` in `if` expression. The corrected expression should be like: `awk -v nuc=$nuc '/^#/{next} {if ($4 == nuc) {print $5}}' $1 | sort | uniq -c`

Result: 
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G

This data makes sense. Because, normally, transition possibility should be higher than transvertion's due to the chemical structure similarity. 


2.
Promoter: Not clearly and objectively defined. Because the promoter-like regions are defined according to position around TSS, which can also be enhancer or other cis elements.

First, use `awk` to extract all the promoter-like regions. TssA, TssAFlnk, TxFlnk, TssBiv and BivFlnk are defined as targets according to `Roadmap Epigenomics Consortium., Kundaje, A., Meuleman, W. et al. Integrative analysis of 111 reference human epigenomes. Nature 518, 317–330 (2015). https://doi.org/10.1038/nature14248`
Then, use bedtools intersect to obtain all the candidate SNPs that appear in promoter-like regions, where `a` is `random_snippet.vcf`, `b` is a `.bed` file of promoter-like regions.
Then, usw `awk` to obtain all the SNPs whose reference base are "C".
Finally, `sort` and `uniq -c` the result to have the number.

code:
`# Usage: bash bash exercise2.sh [regions_and_states_file.bed] [SNP_file.vcf]`
`promoter_file=promoters.bed`
`awk '{if ($4 == "1" || $4 == "2" || $4 == "3" || $4 == "10" || $4 == "11") {print}}' $1 > $promoter_file`
`intersect_file=intersect.vcf`
`bedtools intersect -a $2 -b $promoter_file > $intersect_file`
`snps_file=snps.vcf`
`awk '/^#/{next} {if ($4 == "C"){print $5}}' $intersect_file > $snps_file`
`sort $snps_file | uniq -c`

result:
  12 A
  11 G
  41 T