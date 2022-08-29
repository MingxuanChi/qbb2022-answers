1. I’m excited to learn <my_short_answer>.


2.
a.
`cp ~/data/bed_files/genes.chr21.bed /Users/cmdb/qbb2022-answers/day1-lunch`
`cp ~/data/bed_files/exons.chr21.bed /Users/cmdb/qbb2022-answers/day1-lunch`

b.
`wc -l exons.chr21.bed `
`wc -l genes.chr21.bed `
Average exon number: 13653/219 = 62.342

c.
For median:
First, match each exon to a specific gene according to the position (base number). Calculate the exon_number for each gene and store the data. 
Second, sort the genes according to the exon_number.
Finally, use 219/2 as the index to obtain the gene name from the sorted genes.


3.
a.
`cp ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed .`

b.
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

Using sort and uniq -cf is another way to solve this.

c.
For "the largest fraction of genome":
First, sort the regions according to state number.
Second, add all the `field_3` numbers to minus all the `field_2` numbers for each state. Thus, we will have a `total_base_number` for each state.
Third, sort the state according to their `total_base_number` and obtain the state with the largest `total_base_number`.


4.
a.
`cp ~/data/metadata_and_txt_files/integrated_call_samples.panel .`

b.
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
     
Using sort and uniq -cf is another way to solve this.

c.
For all other super populations, we can simply replace AFR with other super populations.

5.
a.
`cp  ~/data/vcf_files/random_snippet.vcf .`

b.
`cut -f 1,2,3,4,5,6,7,8,9,13 random_snippet.vcf > HG00100.vcf`

c.
`sort -k 10 HG00100.vcf | uniq -cf 9 | less -S`
0|0: 9514 chr21      10005999        .       C       A       .       PASS    AC=91;AN=5096;DP=31568;AF=0.02;EAS_AF=0;EUR_AF=0;AFR_AF=0.06;AMR_AF=0;SAS_AF=0;VT=SNP;NS=2548   GT     >
0|1: 127 chr21      10715575        .       C       G       .       PASS    AC=87;AN=5096;DP=80079;AF=0.02;EAS_AF=0;EUR_AF=0.04;AFR_AF=0;AMR_AF=0.02;SAS_AF=0.03;VT=SNP;NS=2548    >
1|0: 178 chr21      13232002        .       A       G       .       PASS    AC=3309;AN=5096;DP=20115;AF=0.65;EAS_AF=0.77;EUR_AF=0.55;AFR_AF=0.7;AMR_AF=0.67;SAS_AF=0.55;VT=SNP;NS=2>
1|1: 181 chr21      10674966        .       G       A       .       PASS    AC=4962;AN=5096;DP=59204;AF=0.97;EAS_AF=0.9;EUR_AF=1;AFR_AF=0.98;AMR_AF=1;SAS_AF=0.99;VT=SNP;NS=2548   >

d.
`grep -w 'AF=1' HG00100.vcf | wc -l`
15

e.
1

f.
For AFR_AF values:
`cut -d ";" -f 7 HG00100.vcf`
The "AFR_AF" value is in a row with other AFs, so we need to split the row to extract AFR_AF. Using `cut -d` is one way to solve this. By this option, we can split every line by a specific delimiter ";". Then obtain "AFR_AF" at field 7.
