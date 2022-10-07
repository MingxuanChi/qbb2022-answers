#! /usr/bin/env python
# Usage: python Q2.py <.frq file>

import matplotlib.pyplot as plt # import matplotlib.pyplot
import numpy as np # import numpy
import sys # import sys

vec_fn = sys.argv[1]
# vec_fn = 'af.frq'

names_list = ['CHR', 'SNP', 'A1', 'A2', 'AF', 'NCHROBS']
vec_array = np.genfromtxt(vec_fn, dtype = None, encoding = None, names = names_list)
# print(vec_array['AF'])

af_list = list()
for i in range(1, len(vec_array['AF'])):
	# print(vec_array['AF'][i])
	af_list.append(float(vec_array['AF'][i]))
	# af_list.append(vec_array['AF'][i])

figa, axa = plt.subplots()
axa.hist(af_list)
axa.set_title('Distribution of Allele Frequency') # set the title
axa.set_ylabel('Occurence') # set the label of x axis
axa.set_xlabel('Allele Frequency') # set the label of y axis
plt.xticks(rotation = 45)

plt.show()

figa.savefig('Q3.png') # save the figure
plt.close(figa) # close figure
