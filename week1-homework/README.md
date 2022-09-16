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
`fn = 'OUTPUT.fasta'`  
`output_list = list()`  
`for i in open(fn):`  
	`output_list.append(int(i.split('\t')[1]))`  
`total_base = sum(output_list)`  
`add_up = 0`  
`while add_up < total_base*0.5:`  
	`longest = max(output_list)`  
	`add_up += longest`  
	`output_list.remove(longest)`  
`n50 = longest`  
`print(n50)`  

