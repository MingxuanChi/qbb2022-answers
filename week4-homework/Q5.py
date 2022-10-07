#!/usr/bin/env python

# Usage: python Q5.py <TAB_delimited .assoc.linear.txt file> Total_Chr_Number Covariates_Number

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

assoc_fn = sys.argv[1]
# assoc_fn = 'gs451_ic50.assoc.linear.txt'
# assoc_fn = 'assoc_test.txt'
total_chr_number = int(sys.argv[2])
# total_chr_number = 22
cov_number = int(sys.argv[3])
# cov_number = 10

with open(assoc_fn) as assoc_f:
	first_line = assoc_f.readline()
	if '\t' not in first_line:
		print('ERROR: Not a TAB_delimited file. Read the Usage bro!')
		exit()

gwas_array_raw = np.genfromtxt(assoc_fn, dtype = None, names = True, delimiter = '\t')
ind = np.lexsort((gwas_array_raw['BP'], gwas_array_raw['CHR']))
gwas_array = gwas_array_raw[ind]
# print(gwas_array)

acc_bp_col_list = list()
chr_boundary_xtick = [0]
for line_index, line in enumerate(gwas_array):
	if line_index == 0:
		acc_bp = 0
	else:
		distance = gwas_array['BP'][line_index] - gwas_array['BP'][line_index-1]
		if distance >= 0:
			acc_bp = acc_bp_col_list[line_index-1] + distance
		else:
			acc_bp = acc_bp_col_list[line_index-1] + gwas_array['BP'][line_index]
			chr_boundary_xtick.append(int(acc_bp))
	acc_bp_col_list.append(int(acc_bp))
chr_boundary_xtick.append(acc_bp_col_list[-1])

xtick_posi = list()
for i in range(len(chr_boundary_xtick) - 1):
	posi = (chr_boundary_xtick[i + 1] + chr_boundary_xtick[i]) / 2
	xtick_posi.append(posi)

# print(acc_bp_col_list)
# acc_bp_col = np.array(acc_bp_col_list)
# acc_bp_col.dtype = {'names':['ACC_BP'], 'formats':[np.int64]}
# print(type(gwas_array))
# print(acc_bp_col_list)
# print(chr_boundary_xtick)
# print(type(acc_bp_col['ACC_BP'][0]))
# gwas_array = np.append((gwas_array, acc_bp_col), 1)
# print(gwas_array)

# print(gwas_array.dtype.names)
# print(gwas_array.dtype)
# print(len(gwas_array))

p_dict = dict()
for cov_index in range(0, cov_number + 1):
	cov_dict = dict()
	if cov_index == 0:
		COV = 'ADD'
	else:
		COV = 'COV' + str(cov_index)
	for chr_index in range(1, total_chr_number + 1):
		chr_dict = dict()
		CHR = 'CHR' + str(chr_index)
		cov_dict[CHR] = chr_dict
	p_dict[COV] = cov_dict
# print(p_dict)

MAX_P = [0]
MAX_line_index = 0
for line_index in range(len(gwas_array)):
	COV = str(gwas_array['TEST'][line_index]).split(r"'")[-2]
	CHR = 'CHR' + str(gwas_array['CHR'][line_index])
	# SNP = str(gwas_array['SNP'][line_index]).split(r"'")[-2]
	P_VAL = (math.log(float(gwas_array['P'][line_index]), 10)) * -1
	if COV == 'ADD' and P_VAL > MAX_P[0]:
		MAX_line_index = line_index
		MAX_P[0] = P_VAL
	ACC_BP = acc_bp_col_list[line_index]
	p_dict[COV][CHR][ACC_BP] = P_VAL
print('The top assocaiated SNP is ' + str(gwas_array['SNP'][MAX_line_index]).split(r"'")[-2] + ' on chromosome ' + str(gwas_array['CHR'][MAX_line_index]))
# print(p_dict)

subplot_position_dict = dict()
for cov_index, cov in enumerate(p_dict):
	if cov == 'ADD':
		subplot_position_dict[cov] = ((4, 4), (0, 0), 2, 3)
	elif cov_index < 3:
		subplot_position_dict[cov] = ((4, 4), (cov_index - 1, 3), 1, 1)
	elif cov_index < 7:
		subplot_position_dict[cov] = ((4, 4), (2, ((cov_index + 1) % 4)), 1, 1)
	else:
		subplot_position_dict[cov] = ((4, 4), (3, ((cov_index + 1) % 4)), 1, 1)		

fig = plt.figure(figsize=(30, 15))
for cov in p_dict:
	# print(subplot_position_dict[cov])
	ax = plt.subplot2grid(subplot_position_dict[cov][0], subplot_position_dict[cov][1], subplot_position_dict[cov][2], subplot_position_dict[cov][3])
	ax.set_xticks(xtick_posi, p_dict[cov].keys(), rotation = 45, fontsize = 4)
	ax.set_title(assoc_fn.split('.')[0] + 'GWAS Plot with ' + cov, fontsize = 5)
	ax.set_ylabel('-Log(P)', fontsize = 5)
	for CHR in p_dict[cov]:
		acc_bp_list = list()
		for acc_bp in p_dict[cov][CHR].keys():
			acc_bp_list.append(int(acc_bp))
			if p_dict[cov][CHR][acc_bp] >= 5:
				ax.plot(acc_bp, p_dict[cov][CHR][acc_bp], '.', color = 'k', markeredgecolor = 'r')
		ax.plot(acc_bp_list, p_dict[cov][CHR].values(), ls = '', marker = '.', alpha = 0.5, markersize = 2.0)
# plt.show()
fig.savefig('Q5_' + assoc_fn.split('.')[0] + '.png')
plt.close(fig)
print('Finished!')