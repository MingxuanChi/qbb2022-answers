#!/usr/bin/env python

# Usage: python VCF_plot.py <annotated vcf file.vcf>

import sys
import matplotlib.pyplot as plt
import numpy as np
from vcfParser import parse_vcf

# def find_info(target = str, info_str = str):
# 	target_index = info_str.find(target + '=') + len(target) + 1
# 	# print(info_str[target_index])
# 	target_score_raw = str()
# 	while info_str[target_index] != ';':
# 		target_score_raw += info_str[target_index]
# 		target_index += 1
# 	target_score_raw_list = target_score_raw.split(',')
# 	target_score = float()
# 	if target == 'AF':
# 		for score in target_score_raw_list:
# 			target_score += float(score)
# 	elif target == 'DPB':
# 		target_score = float(target_score_raw_list[0])
# 	return float(target_score)

def find_effect(eff_str):
	effect_impact_list = list()
	info_str_list = eff_str.split(',')
	for info_str in info_str_list:
		effect_impact_raw_list = info_str.split('|')
		for i in effect_impact_raw_list:
			if '(' in i:
				effect_impact = i.split('(')[0]
				effect_impact_list.append(effect_impact)
	return effect_impact_list

# vcf_name = sys.argv[1]
vcf_name = 'OUTPUT_filtered_decomposed_annotated.vcf'

vcf = parse_vcf(vcf_name)
print(vcf[1])

DP_list = list()
AF_list = list()
QUAL_list = list()
eff_dict = dict()
for line_index in range(1, len(vcf)):

	AF = vcf[line_index][7]['AF']
	if AF != '.':
		AF_list.append(AF)

	QUAL = vcf[line_index][5]
	if QUAL != '.':
		QUAL_list.append(QUAL)

	for FORMAT_index in range(9, len(vcf[line_index])):
		DP = vcf[line_index][FORMAT_index][2]
		if DP != '.':
			DP_list.append(int(DP))

	EFF_str = vcf[line_index][7]['EFF']
	EFF_list = find_effect(EFF_str)
	for effect in EFF_list:
		if effect in eff_dict:
			eff_dict[effect] += 1
		else:
			eff_dict[effect] = 1


# print(DP_list)
# print(AF_list)
# print(QUAL_list)
print(eff_dict)



# effect_dict = dict()
# depth_list = list()
# qual_list = list()
# af_list = list()
# for line in open(vcf_name):

# 	if line.startswith('#'):
# 		continue

# 	line_list = line.strip('\n').split('\t')
# 	print(line_list)
# 	snp_name = line_list[0] + '_' + line_list[1]
# 	snp_qual = float(line_list[5])
# 	qual_list.append(snp_qual)
# 	snp_depth = find_info('DPB', line_list[7])
# 	depth_list.append(snp_depth)
# 	snp_af = find_info('AF', line_list[7])
# 	af_list.append(snp_af)

# 	snp_effect_list = find_effect(line_list[7])
# 	for effect in snp_effect_list:
# 		if effect in effect_dict:
# 			effect_dict[effect] += 1
# 		else:
# 			effect_dict[effect] = 1

fig = plt.figure(figsize=(20, 30))
ax1 = plt.subplot(3,2,1)
ax1.hist(DP_list, log = True)
ax1.set_xlabel('SNP Read Depth', fontsize = 8)
ax1.set_ylabel('Occurence (Log10)', fontsize = 8)
ax1.set_title('Distribution of SNP Read Depth', fontsize = 8)
# print(ax1)
ax2 = plt.subplot(3,2,3)
ax2.hist(QUAL_list, log = True)
ax2.set_xlabel('SNP Quality Score', fontsize = 8)
ax2.set_ylabel('Occurence (Log10)', fontsize = 8)
ax2.set_title('Distribution of SNP Quality Score', fontsize = 8)
ax3 = plt.subplot(3,2,5)
ax3.hist(AF_list)
ax3.set_xlabel('SNP Allele Frequency', fontsize = 8)
ax3.set_ylabel('Occurence', fontsize = 8)
ax3.set_title('Distribution of SNP Allele Frequency', fontsize = 8)
ax4 = plt.subplot(1,2,2)
ax4.bar(eff_dict.keys(), eff_dict.values(), log = True)
# ax4.bar_label
ax4.set_xlabel('Variant Effects', fontsize = 8)
ax4.set_ylabel('Counts of Effects (Log10)', fontsize = 8)
ax4.set_title('Effect Number', fontsize = 8)
ax4.set_xticklabels(eff_dict.keys(), rotation=50, ha='right')
# fig.subplots_adjust(bottom = 0.3, top = 0.95)
# plt.show()
fig.savefig('week3-homework.png')
plt.close(fig)