#! /usr/bin/env python
# Usage: 

import numpy as np
import numpy.lib.recfunctions as rfn
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import scipy
import seaborn
from statsmodels.formula.api import ols
from statsmodels.api import qqplot
from statsmodels.stats.multitest import multipletests

def unstructure_1D_arr(arr):
	structred_list = list()
	for line in arr:
		line_list = list(line)
		structured_line = tuple(line_list[1::])
		structred_list.append(structured_line)
		# print(type(line))
		# print(line[0])
		# line.remove(0)
	# print(structred_list)
	unstructured_arr = np.array(structred_list)
	return unstructured_arr


input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')
col_names = [input_arr.dtype.names]
row_names = input_arr['t_name']
sexes = list()
stages = list()
for index in range(1, len(col_names[0])):
	sex = list(col_names[0])[index].split('_')[0]
	stage = list(col_names[0])[index].split('_')[1]
	sexes.append(sex)
	stages.append(stage)
# print(sexes)
# print(stages)
# print(input_arr.ndim)
# print(col_names)
# print(row_names)

unstructured_arr = unstructure_1D_arr(input_arr)
# print(structured_arr.ndim)

# fpkm_values_2d = rfn.structured_to_unstructured(structured_arr, dtype=np.float)
# print(fpkm_values_2d)

filtered_arr = np.zeros((1, len(unstructured_arr[0])))
filtered_names = np.zeros((1,1))
for line_index, line in enumerate(unstructured_arr):
	if np.median(line) > 0:
		# print(np.median(line))
		# print(line)
		filtered_arr = np.concatenate((filtered_arr, [line]), axis = 0)
		filtered_names = np.concatenate((filtered_names, [[row_names[line_index]]]))
filtered_arr = np.delete(filtered_arr, (0), axis = 0)
filtered_names = np.delete(filtered_names, (0), axis = 0)
# print(filtered_arr)
# print(filtered_names)
# print(len(filtered_arr)==len(filtered_names))

log_arr = np.log2(filtered_arr + 0.1)
# print(log_arr)

linkg_arr = linkage(log_arr, 'ward')
# print(linkg_arr)

leaves_list(linkg_arr)
# print(linkg_arr)

pval_list = list()
beta_list = list()
de_list = list()
de_list_w_sex = list()
pval_list_w_sex = list()
beta_list_w_sex = list()
for i in range(log_arr.shape[0]):
	list_of_tuples = []
	for j in range(len(col_names[0])-1):
		list_of_tuples.append((row_names[i],log_arr[i,j], sexes[j], stages[j]))
		longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
	# print(longdf)
	# print(len(longdf))
	result = ols(formula = 'fpkm ~ stage', data = longdf).fit()
	beta = result.params['stage']
	pval = result.pvalues['stage']
	pval_list.append(pval)
	beta_list.append(beta)

	mt_result = multipletests(np.array(pval_list), alpha=0.1, method='sidak', is_sorted=False, returnsorted=False)
	if True in mt_result[0]:
		de_list.append(row_names[i])

	result_w_sex = ols(formula = 'fpkm ~ stage + sex', data = longdf).fit()
	beta_w_sex = result_w_sex.params['stage']
	pval_w_sex = result_w_sex.pvalues['stage']
	pval_list_w_sex.append(pval_w_sex)
	beta_list_w_sex.append(beta_w_sex)

	mt_result_w_sex = multipletests(np.array(pval_list_w_sex), alpha=0.1, method='sidak', is_sorted=False, returnsorted=False)
	if True in mt_result_w_sex[0]:
		de_list_w_sex.append(row_names[i])

f1 = open('DE-nosex.txt', 'w')
for transcript in de_list:
	f1.write(transcript+'\n')
# f1.save()
f1.close()

f1_w_sex = open('DE-sex.txt', 'w')
for transcript in de_list_w_sex:
	f1_w_sex.write(transcript+'\n')
# f1.save()
f1_w_sex.close()

# print(de_list)
# print(len(de_list))
# print(len(row_names))
# print(de_list_w_sex)
# print(len(de_list_w_sex))
# print(pval_list)
# print(beta_list)

ovlp_number = 0
for i in de_list_w_sex:
	if i in de_list:
		ovlp_number += 1
percentage = ovlp_number/len(de_list)
f2 = open('percentage.txt', 'w')
f2.write('The overlapping percentage is ' + str(round(percentage*100, 2)) + '%.')

fig = plt.figure()
ax = plt.subplot(1,1,1)
nega_lg_pval_w_sex_arr = -np.log10(np.array(pval_list_w_sex))
for indx, i in enumerate(nega_lg_pval_w_sex_arr):
	if i >= 3:
		ax.scatter(beta_list_w_sex[indx], i, color = 'maroon')
	else:
		ax.scatter(beta_list_w_sex[indx], i, color = 'blue')
plt.show()
plt.savefig('volcano.png')

qqplot(np.array(pval_list), dist = scipy.stats.uniform, line = '45', fit = True)
# plt.show()
plt.savefig('qqplot.png')
