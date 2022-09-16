Q1.  
1.1  
1 Mbp * 5 / 100 bp = 50,000 reads  
1 Mbp * 15 / 100 bp= 150,000 reads  
  
1.3  
`print(1Mbp_coverage_list.count(0))`  
After multiple runnings:  
results = 6676, 6418, 7098, 7571, 6350  
Avg. = 6822.6  
Poisson Frequence Count (k=0) = 1M * P(k=0) = 1E6 * (1/1) * exp(-5) = 6737.95  
Relative Difference = 1.26%  
Student T-test t = 0.374  
According to table, P > 0.2,  
so there is no significant difference between simulation and Poisson distribution at coverage = 0  
And the overall histogram can align with the poisson curve well.  
  
1.4  
`print(1Mbp_coverage_list.count(0))`  
After multiple runnings:  
results = 5, 3, 8, 10, 3  
Avg. = 5.8  
Poisson Frequence Count (k=0) = 1M * P(k=0) = 1E6 * (1/1) * exp(-15) = 0.306  
Relative Difference = 1796.0%  
Student T-test t = 3.94  
According to table, P < 0.01,  
so there is significant difference between simulation and Poisson distribution at coverage = 0.  
And the overall histogram can align with the poisson curve well.  
  

Q2.  
`~/SPAdes-3.15.5-Darwin/bin/spades.py --pe1-1 frag180.1.fq --pe1-2 frag180.2.fq --mp1-1 jump2k.1.fq --mp1-2 jump2k.2.fq -o asm -t 4 -k 31`  
2.1  
`cd asm/`  
`grep -c ">" contigs.fasta`  
Output: `4`  
So there are 4 contigs in total.  
  
2.2  
`samtools faidx contigs.fasta -o OUTPUT.fasta`  
`less -S OUTPUT.fasta`  
Output:  
`NODE_1_length_105830_cov_20.649193      105830  36      60      61`  
`NODE_2_length_47860_cov_20.367392       47860   107665  60      61`  
`NODE_3_length_41351_cov_20.528098       41351   156358  60      61`  
`NODE_4_length_39426_cov_20.336388       39426   198434  60      61`  
105830+47860+41351+39426 = 234467  
So the total length is 234467  
  
2.3
`sort -k 2 -n OUTPUT.fasta | tail -1 | cut -f 1`  
Output: `NODE_1_length_105830_cov_20.649193`  
So the longest one is `NODE_1_length_105830_cov_20.649193`.  
  
2.4  
N50 = 47860  
Script for this question is also uploaded. Thanks!  
  
  
Q3.  
3.1  
`dnadiff ref.fa asm/contigs.fasta`  
`grep "AvgIdentity" out.report | less -S`  
Output:  
`AvgIdentity                   100.00               100.00`  
`AvgIdentity                   100.00               100.00`  
So the average identity is 100.00, for both many to many and 1 to 1 alignment (subset of many to many).  
  
3.2  
`nucmer ref.fa asm/contigs.fasta`  
`show-coords out.delta`  
Output is a table, in which the longest length is 105830.  
  
3.3  
`grep "Insertions" out.report | less -S`  
Output:  
`Insertions                         5                    1`  
So there are 5 insertions and 1 deletions.  
  

Q4.  
4.1  
`show-coords out.delta`  
Output is a table. Try to find the contig that occured two times, in whose line the S and E positions of ref sequence are continuous.  
So we got the insertion happens between 26789 and 26790.  
  
4.2  
27500 - 26787 - 1 = 712 bp  
  
4.3  
The contig ID is `NODE_3_length_41351_cov_20.528098`.  
`samtools faidx asm/contigs.fasta NODE_3_length_41351_cov_20.528098:26788-27499 > insertion.fasta`  
`tail -n+2 insertion.fasta`  
Output:  
`CGCCCATGCGTAGGGGCTTCTTTAATTACTTGATTGACGCATGCCCCTCGTTCTACATGT`
`CTAGCTTCGTAACTGCCCCGATTTATACAGGAGCATATGCGTTTCGTAGTGCCGGGAATG`
`CATACCAAAGGGCTCACGGCGGGTACGCCACAATGGCTCAAGTCGAAAATGAATCGAAGA`
`CAACAAGGAATACCGTACCCAATTACTCAAGGACCTCATACACCATCCCATGCTACTTAT`
`CTACAGACATACACGCCAGCACCCAGCAACCAAAGCACACCGACGATAAGACTACAATCG`
`CGATAAGCACAACTTACATTAGGAGGCCCGGCAAATCTTGACGGCGTTAAGTCCGACACG`
`AATACCCCCCGACAAAAGCCTCGTATTCCGAGAGTACGAGAGTGCACAAAGCACCAAGGC`
`GGGGCTTCGGTACATCCACCAGTAGTCCCGTCGTGGCGGATTTTCGTCGCGGATGATCCG`
`AGGATTTCCTGCCTTGCCGAACACCTTACGTCATTCGGGGATGTCATAAAGCCAAACTTA`
`GGCAAGTAGAAGATGGAGCACGGTCTAAAGGATTAAAGTCCTCGAATAACAAAGGACTGG`
`AGTGCCTCAGGCATCTCTGCCGATCTGATTGCAAGAAAAAATGACAATATTAGTAAATTA`
`GCCTATGAATAGCGGCTTTAAGTTAATGCCGAGGTCAATATTGACATCGGTA`
This is the insertion sequence.  
  
4.4  
`python dna-decode.py --decode --input insertion.fasta`  
The message is:  
`Congratulations to the 2021 CMDB @ JHU class!  Keep on looking for little green aliens...`
