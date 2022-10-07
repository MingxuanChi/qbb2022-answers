#! /usr/bin/env python
# Usage: python Q2.py <.eigenvec file (fields: '0', 'indv.', 'pc1', 'pc2', 'pc3', 'pc...')> number_of_pc

import matplotlib.pyplot as plt # import matplotlib.pyplot
import numpy as np # import numpy
import sys # import sys

vec_fn = sys.argv[1] # give file path of .eigenvec file by the first argument in command line after q2.py
pc_number = sys.argv[2]

names_list = ['0', 'indv.']
for i in range(1, int(pc_number)+1):
	names_list.append('pc' + str(i))

vec_array = np.genfromtxt(vec_fn, dtype = None, encoding = None, names = names_list) # generate a numpy array from the given .eigenvec file

figa, axa = plt.subplots() # create a fig for PC1-PC2
axa.set_title('PC1-PC2 PCA Plot for Genotypes') # set the title
axa.set_xlabel('PC1') # set the label of x axis
axa.set_ylabel('PC2') # set the label of y axis
axa.scatter(vec_array['pc1'],vec_array['pc2'], color = 'green') # draw the plot with x = pc1, y = pc2
plt.show() # have a preview of the figure before saving it

figa.savefig('Q2.png') # save the figure
plt.close(figa) # close figure
