1. I’m excited to learn <my_short_answer>.

2.
`cp ~/data/bed_files/genes.chr21.bed /Users/cmdb/qbb2022-answers/day1-lunch`
`cp ~/data/bed_files/exons.chr21.bed /Users/cmdb/qbb2022-answers/day1-lunch`
`wc -l exons.chr21.bed `
`wc -l genes.chr21.bed `
Average exon number: 13653/219 = 62.342

For median:
First, match each exon to a specific gene according to the position (base number). Calculate the exon_number for each gene and store the data. 
Second, sort the genes according to the exon_number.
Finally, use 219/2 as the index to obtain the gene name from the sorted genes.

3.
`cp ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed .`
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort | uniq `
1
10
11
12
13
14
15
2
3
4
5
6
7
8
9
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 1 | wc -l `
     305
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 10 | wc -l `
      17
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 11 | wc -l `
      17
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 12 | wc -l `
      30
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 13 | wc -l `
      62
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 14 | wc -l `
     228
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 15 | wc -l `
     992
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 2 | wc -l `
     678
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 3 | wc -l `
      79
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 4 | wc -l `
     377
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 5 | wc -l `
     808
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 6 | wc -l `
     148
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 7 | wc -l `
    1050
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 8 | wc -l `
     156
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 9 | wc -l `
     654
`$((305+17+17+30+62+228+992+678+79+377+808+148+1050+156+654))`
-bash: 5601: command not found
`cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | wc -l`
    5601

For "the largest fraction of genome":
First, sort the regions according to state number.
Second, add all the `field_3` numbers to minus all the `field_2` numbers for each state. Thus, we will have a `total_base_number` for each state.
Third, sort the state according to their `total_base_number` and obtain the state with the largest `total_base_number`.

4.
`cut -f 2,3 integrated_call_samples.panel | grep AFR | sort -k 1 | uniq`
ACB	AFR
ASW	AFR
ESN	AFR
GWD AFR
LWK	AFR
MSL	AFR
YRI	AFR
`cut -f 2,3 integrated_call_samples.panel | grep AFR | grep ACB | wc -l`
     123
`cut -f 2,3 integrated_call_samples.panel | grep AFR | grep ASW | wc -l`
     112
`cut -f 2,3 integrated_call_samples.panel | grep AFR | grep ESN | wc -l`
     173
`cut -f 2,3 integrated_call_samples.panel | grep AFR | grep GWD | wc -l`
     180
`cut -f 2,3 integrated_call_samples.panel | grep AFR | grep LWK | wc -l`
     122
`cut -f 2,3 integrated_call_samples.panel | grep AFR | grep MSL | wc -l`
     128
`cut -f 2,3 integrated_call_samples.panel | grep AFR | grep YRI | wc -l`
     206

