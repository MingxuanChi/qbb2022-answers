#!/usr/bin/env python

# Usage: python Q6.py interested_SNP genotype_file phenotype_file

import sys
import matplotlib.pyplot as plt
import numpy as np

vcf_fn = sys.argv[2]
# vcf_fn = 'gwas_data/genotypes.vcf'
SNP = sys.argv[1]
# SNP = 'rs10876043'
pheno_fn = sys.argv[3]
# pheno_fn = 'gwas_data/CB1908_IC50.txt'

intersted_SNP_info_list = list()
for line in open(vcf_fn):
	if line.startswith('#') and line[1] != '#':
		header = line.strip('\n').split('\t')[9::]
	if SNP in line:
		# print(line)
		for item in line.strip('\n').split('\t'):
			if item != '':
				intersted_SNP_info_list.append(item)
# print(intersted_SNP_info_list)
# print(header)

pheno_dict = dict()
for line in open(pheno_fn):
	if line.startswith('FID'):
		pass
	else:
		FID = line.strip('\n').split('\t')[0]
		IID = line.strip('\n').split('\t')[1]
		key = str(FID) + '_' + str(IID)
		if line.strip('\n').split('\t')[2] == 'NA':
			pheno = 'NA'
		else:
			pheno = float(line.strip('\n').split('\t')[2])
		pheno_dict[key] = pheno


count_dict = dict()
gt_0_list = list()
gt_1_list = list()
gt_2_list = list()
for gt_index, gt in enumerate(intersted_SNP_info_list[9::]):
	if gt.count('0') == 2:
		if pheno_dict[header[gt_index]] != 'NA':
			gt_0_list.append(pheno_dict[header[gt_index]])
	elif gt.count('1') == 1:
		if pheno_dict[header[gt_index]] != 'NA':
			gt_1_list.append(pheno_dict[header[gt_index]])
	elif gt.count('1') == 2:
		if pheno_dict[header[gt_index]] != 'NA':
			gt_2_list.append(pheno_dict[header[gt_index]])
count_dict['AA(0)'] = gt_0_list
count_dict['AG(1)'] = gt_1_list
count_dict['GG(2)'] = gt_2_list
# print(count_dict)

fig = plt.figure()
ax = fig.add_subplot(111)
ax_dict = ax.boxplot([count_dict['AA(0)'], count_dict['AG(1)'], count_dict['GG(2)']], showfliers = False, labels = count_dict.keys(), showmeans = True)
ax.set_xticks([1, 2, 3], count_dict.keys())
ax.set_ylabel('Phenotype IC50')
ax.set_xlabel('Genotypes')
ax.set_title('IC50 of Different Genotypes')
# plt.show()
fig.savefig('Q6.png')
plt.close(fig)

# print(ax_dict['means'])