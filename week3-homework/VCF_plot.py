#!/usr/bin/env python

# Usage: python VCF_plot.py <annotated vcf file.vcf>

import sys
import matplotlib.pyplot as plt
import numpy as np

def find_info(target = str, info_str = str):
	target_index = info_str.find(target + '=') + len(target) + 1
	# print(info_str[target_index])
	target_score = str()
	while info_str[target_index] != ';':
		target_score += info_str[target_index]
		target_index += 1
	return float(target_score)

def find_effect(info_str):
	effect_str = info_str.split('EFF=')[1]
	effect_impact_raw = effect_str.split('|')[0]
	effect_impact = effect_impact_raw.split('(')[1]
	return effect_impact

vcf_name = sys.argv[1]
# vcf_name = 'OUTPUT_filtered_decomposed_annotated.vcf'

effect_dict = dict()
depth_list = list()
qual_list = list()
af_list = list()
for line in open(vcf_name):

	if line.startswith('#'):
		continue

	line_list = line.strip('\n').split('\t')
	# print(line_list)
	snp_name = line_list[0] + '_' + line_list[1]
	snp_qual = float(line_list[5])
	qual_list.append(snp_qual)
	snp_depth = find_info('DPB', line_list[7])
	depth_list.append(snp_depth)
	snp_af = find_info('AF', line_list[7])
	af_list.append(snp_af)

	snp_effect = find_effect(line_list[7])
	if snp_effect in effect_dict:
		effect_dict[snp_effect] += 1
	else:
		effect_dict[snp_effect] = 1

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))
ax1 = plt.subplot(2,2,1)
ax1.hist(depth_list)
ax1.set_xlabel('SNP Read Depth', fontsize = 8)
ax1.set_ylabel('Occurence', fontsize = 8)
ax1.set_title('Distribution of SNP Read Depth', fontsize = 8)
# print(ax1)
ax2 = plt.subplot(2,2,2)
ax2.hist(qual_list)
ax2.set_xlabel('SNP Quality Score', fontsize = 8)
ax2.set_ylabel('Occurence', fontsize = 8)
ax2.set_title('Distribution of SNP Quality Score', fontsize = 8)
ax3 = plt.subplot(2,2,3)
ax3.hist(af_list)
ax3.set_xlabel('SNP Allele Frequency', fontsize = 8)
ax3.set_ylabel('Occurence', fontsize = 8)
ax3.set_title('Distribution of SNP Allele Frequency', fontsize = 8)
ax4 = plt.subplot(2,2,4)
ax4.bar(effect_dict.keys(), effect_dict.values())
ax4.set_xlabel('Variant Effects', fontsize = 8)
ax4.set_ylabel('Occurence', fontsize = 8)
ax4.set_title('Effect Number', fontsize = 8)
# plt.show()
fig.savefig('week3-homework.png')
plt.close(fig)