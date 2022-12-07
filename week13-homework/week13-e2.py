#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def wf_simulation(A1_freq, N_popn):
	A2_freq = 1 - A1_freq
	A1_count = 2 * N_popn * A1_freq
	A2_count = 2 * N_popn * A2_freq
	generation_number = 0
	title = 'Simulation for N = ' + str(N_popn) + ', Starting_freq = (' + str(A1_freq) + ':' + str(A2_freq) + ')'

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

	return (A1_list, A2_list, title)

# print(A1_list)
# print(A2_list)
# print(generation_number)

A1_list, A2_list, title = wf_simulation(0.48, 100)

fig2, ax2 = plt.subplots()
ax2.set_title(title) # set the title
ax2.set_xlabel('Generation') # set the label of x axis
ax2.set_ylabel('Allele frequency') # set the label of y axis
ax2.plot(A1_list, color = 'blue', marker = 'o', markerfacecolor = 'white', markersize = 2)
ax2.plot(A2_list, color = 'red', marker = 'o', markerfacecolor = 'white', markersize = 2) 
# plt.show()
fig2.savefig('step2.png')