#!/usr/bin/env python

# Usage: python Q1_STEP5.py _scaled_cropped.bdg

import sys
import matplotlib.pyplot as plt
import numpy as np
from bdg_loader import load_data
import glob

bdg_fn_list = glob.glob('*' + str(sys.argv[1]))
# bdg_fn_list = ['D0_H3K27ac_treat_scaled_cropped.bdg']
# bdg_fn_list = ['test.bdg']
bdg_fn_list.sort(reverse = True)
bdg_fn_list[2], bdg_fn_list[3] = bdg_fn_list[3], bdg_fn_list[2]
# print(bdg_fn_list)

fig = plt.figure(figsize=(10, 5))
fig.suptitle('chr17: 35,502,000-35,507,000')
for index, bdg_fn in enumerate(bdg_fn_list):
	data = load_data(bdg_fn)
	# print(data)
	ax = fig.add_subplot(4,1,index + 1)
	ax.bar(data['X'], data['Y'], width = 101.0)
	ax.set_xticks([])
	ax.set_ylabel(bdg_fn.split('_treat')[0])
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	if index in [2, 3]:
		ax.set_ylim([0, 20000])

# plt.show()
fig.savefig('Q1_STEP5.png')
fig.savefig('Q1_STEP5.pdf', format = 'pdf')
plt.close(fig)