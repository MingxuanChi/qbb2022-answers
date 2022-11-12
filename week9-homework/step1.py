#! /usr/bin/env python
# Usage: 

import numpy as np
import numpy.lib.recfunctions as rfn
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import seaborn

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
print(log_arr)

linkg_arr = linkage(log_arr, 'ward')
# print(linkg_arr)

leaves_list(linkg_arr)
print(linkg_arr)

# hmp_names = list()
# for i in filtered_names:
# 	hmp_names.append(i[0])

ax = seaborn.clustermap(log_arr, cmap = 'viridis', row_linkage = linkg_arr, xticklabels = col_names[0], dendrogram_ratio = (0.1,0.1))
plt.savefig('Heatmap.png')
# plt.show()

fig = plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Samples')
plt.ylabel('Distance')
dn = dendrogram(linkg_arr, leaf_rotation = 90, leaf_font_size = 0)
# plt.show()
fig.savefig('dendrogram.png')
plt.close(fig)
