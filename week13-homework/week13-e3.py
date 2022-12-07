#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def wf_simulation(A1_freq, N_popn):
	A2_freq = 1 - A1_freq
	A1_count = 2 * N_popn * A1_freq
	A2_count = 2 * N_popn * A2_freq
	generation_number = 0
	title = '1000x Simulation for N = 100, Starting_freq = (' + str(A1_freq) + ':' + str(A2_freq) + ')'

	A1_list = [A1_freq]
	A2_list = [A2_freq]
	while A1_freq != 1 and A1_freq != 0:
		n, p = 2 * N_popn, A1_freq  # number of trials, probability of each trial
		A1_count = np.random.binomial(n, p)
		A1_freq = A1_count / (2 * N_popn)
		A2_freq = 1 - A1_freq
		A1_list.append(A1_freq)
		A2_list.append(A2_freq)
		generation_number += 1

	return (A1_list, A2_list, title, generation_number)

generation_list = list()
for i in range(1000):
	title, generation_number = wf_simulation(0.5, 100)[2::]
	generation_list.append(generation_number)

# print(A1_list)
# print(A2_list)
# print(generation_number)
# print(generation_list)

fig3, ax3 = plt.subplots()
ax3.set_title(title) # set the title
ax3.set_xlabel('Generation') # set the label of x axis
ax3.set_ylabel('Occurrence') # set the label of y axis
ax3.hist(generation_list) 
# plt.show()
fig3.savefig('step3.png')