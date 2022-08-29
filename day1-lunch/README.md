1. I’m excited to learn <my_short_answer>.

2.
(base) [~/qbb2022-answers/day1-lunch $]cp ~/data/bed_files/genes.chr21.bed /Users/cmdb/qbb2022-answers/day1-lunch
(base) [~/qbb2022-answers/day1-lunch $]cp ~/data/bed_files/exons.chr21.bed /Users/cmdb/qbb2022-answers/day1-lunch
(base) [~/qbb2022-answers/day1-lunch $]wc -l exons.chr21.bed 
(base) [~/qbb2022-answers/day1-lunch $]wc -l genes.chr21.bed 
Average exon number: 13653/219 = 62.342

For median:
First, match each exon to a specific gene according to the position (base number). Calculate the exon_number for each gene and store the data. 
Second, sort the genes according to the exon_number.
Finally, use 219/2 as the index to obtain the gene name from the sorted genes.

3.
(base) [~/qbb2022-answers/day1-lunch $]cp ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed .
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort | uniq 
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
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 1 | wc -l 
     305
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 10 | wc -l 
      17
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 11 | wc -l 
      17
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 12 | wc -l 
      30
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 13 | wc -l 
      62
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 14 | wc -l 
     228
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 15 | wc -l 
     992
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 2 | wc -l 
     678
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 3 | wc -l 
      79
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 4 | wc -l 
     377
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 5 | wc -l 
     808
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 6 | wc -l 
     148
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 7 | wc -l 
    1050
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 8 | wc -l 
     156
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 9 | wc -l 
     654
(base) [~/qbb2022-answers/day1-lunch $]$((305+17+17+30+62+228+992+678+79+377+808+148+1050+156+654))
-bash: 5601: command not found
(base) [~/qbb2022-answers/day1-lunch $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | wc -l
    5601

For "the largest fraction of genome":
First, sort the regions according to state number.
Second, add all the `field_3` numbers to minus all the `field_2` numbers for each state. Thus, we will have a `total_base_number` for each state.
Third, sort the state according to their `total_base_number` and obtain the state with the largest `total_base_number`.
