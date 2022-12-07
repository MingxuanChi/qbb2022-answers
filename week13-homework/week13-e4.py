#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def wf_simulation(A1_freq, N_popn):
	A2_freq = 1 - A1_freq
	A1_count = 2 * N_popn * A1_freq
	A2_count = 2 * N_popn * A2_freq
	generation_number = 0
	title = 'Simulation for Starting_freq = (' + str(A1_freq) + ':' + str(A2_freq) + ')'

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
popn_size_list = list()
for i in range(0, 51, 2):
	N_popn = 100 * (10 ** (i * 0.1))
	title, generation_number = wf_simulation(0.5, N_popn)[2::]
	generation_list.append(generation_number)
	popn_size_list.append(2 + round(i * 0.1, 1))
	# print(N_popn)
	# print(i)
	# print(generation_number)

# print(A1_list)
# print(A2_list)
# print(generation_number)
# print(generation_list)
# print(popn_size_list)

fig4, ax4 = plt.subplots()
ax4.set_title(title) # set the title
ax4.set_xlabel('Lg Population Size') # set the label of x axis
ax4.set_ylabel('No. Generation') # set the label of y axis
plt.xticks(popn_size_list, popn_size_list, rotation = 45)
ax4.plot(popn_size_list, generation_list, color = 'blue', marker = 'o', markerfacecolor = 'white', markersize = 2)
plt.tight_layout()
# plt.show()
fig4.savefig('step4.png')