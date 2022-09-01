#! /usr/bin/env python
# Usage: python E2.py <.eigenvec file (fields: '0', 'indv.', 'pc1', 'pc2', 'pc3')>

import matplotlib.pyplot as plt # import matplotlib.pyplot
import numpy as np # import numpy
import sys # import sys

vec_fn = sys.argv[1] # give file path of .eigenvec file by the first argument in command line after E2.py

vec_array = np.genfromtxt(vec_fn, dtype = None, encoding = None, names = ['0', 'indv.', 'pc1', 'pc2', 'pc3']) # generate a numpy array from the given .eigenvec file

figa, axa = plt.subplots() # create a fig for PC1-PC2
axa.set_title('PC1-PC2 PCA Plot for 1K Genome Project SNP') # set the title
axa.set_xlabel('PC1') # set the label of x axis
axa.set_ylabel('PC2') # set the label of y axis
axa.scatter(vec_array['pc1'],vec_array['pc2'], color = 'green') # draw the plot with x = pc1, y = pc2
plt.show() # have a preview of the figure before saving it

figa.savefig('ex2_a.png') # save the figure
plt.close(figa) # close figure


figb, axb = plt.subplots() # create a fig for PC1-PC3
axb.set_title('PC1-PC3 PCA Plot for 1K Genome Project SNP')
axb.set_xlabel('PC1') # set the label of x axis
axb.set_ylabel('PC3') # set the label of y axis
axb.scatter(vec_array['pc1'],vec_array['pc3'], color = 'green') # draw the plot with x = pc1, y = pc3
plt.show() # have a preview of the figure before saving it

figb.savefig('ex2_b.png') # save the figure
plt.close(figb) # close figure


# print(vec_array)