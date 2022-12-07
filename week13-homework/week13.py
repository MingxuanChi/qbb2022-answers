#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import seaborn
import pandas

def wf_simulation(A1_freq, N_popn):
	A2_freq = 1 - A1_freq
	A1_count = 2 * N_popn * A1_freq
	A2_count = 2 * N_popn * A2_freq
	generation_number = 0
	# title = '1000x Simulation for N = 100, Starting_freq = (' + str(A1_freq) + ':' + str(A2_freq) + ')'

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

	return (A1_list, A2_list, generation_number)

# ------------------------------------------------------------------
# E2
# ------------------------------------------------------------------

A1_freq = 0.48
A2_freq = 1 - A1_freq
N_popn = 100
title = 'Simulation for N = ' + str(N_popn) + ', Starting_freq = (' + str(A1_freq) + ':' + str(A2_freq) + ')'
A1_list, A2_list = wf_simulation(A1_freq, N_popn)[slice(0, 2)]

fig2, ax2 = plt.subplots()
ax2.set_title(title) # set the title
ax2.set_xlabel('Generation') # set the label of x axis
ax2.set_ylabel('Allele frequency') # set the label of y axis
ax2.plot(A1_list, color = 'blue', marker = 'o', markerfacecolor = 'white', markersize = 2)
ax2.plot(A2_list, color = 'red', marker = 'o', markerfacecolor = 'white', markersize = 2) 
# plt.show()
fig2.savefig('step2.png')

# ------------------------------------------------------------------
# E3
# ------------------------------------------------------------------

generation_list = list()
A1_freq = 0.5
A2_freq = 1 - A1_freq
N_popn = 100
for i in range(1000):
	generation_number = wf_simulation(A1_freq, N_popn)[-1]
	generation_list.append(generation_number)

title = '1000x Simulation for N = 100, Starting_freq = (' + str(A1_freq) + ':' + str(A2_freq) + ')'

fig3, ax3 = plt.subplots()
ax3.set_title(title) # set the title
ax3.set_xlabel('Generation') # set the label of x axis
ax3.set_ylabel('Occurrence') # set the label of y axis
ax3.hist(generation_list) 
# plt.show()
fig3.savefig('step3.png')

# ------------------------------------------------------------------
# E4
# ------------------------------------------------------------------

generation_list = list()
popn_size_list = list()
A1_freq = 0.5
A2_freq = 1 - A1_freq
title = 'Simulation for Starting_freq = (' + str(A1_freq) + ':' + str(A2_freq) + ')'
for i in range(0, 51, 2):
	N_popn = 100 * (10 ** (i * 0.1))
	generation_number = wf_simulation(A1_freq, N_popn)[-1]
	generation_list.append(generation_number)
	popn_size_list.append(2 + round(i * 0.1, 1))

fig4, ax4 = plt.subplots()
ax4.set_title(title) # set the title
ax4.set_xlabel('Lg Population Size') # set the label of x axis
ax4.set_ylabel('No. Generation') # set the label of y axis
plt.xticks(popn_size_list, popn_size_list, rotation = 45)
ax4.plot(popn_size_list, generation_list, color = 'blue', marker = 'o', markerfacecolor = 'white', markersize = 2)
plt.tight_layout()
# plt.show()
fig4.savefig('step4.png')

# ------------------------------------------------------------------
# E5
# ------------------------------------------------------------------

title = '100x Simulations for Starting_freq = 0.05 + N * 0.10\nN = range(0, 10), Population size = 10,000'
af_list = list()
generation_list = list()
for af_x100 in range(5, 100, 10):
	for simulation in range(0, 100):
		A1_freq = round(af_x100 / 100, 2)
		af_list.append(str(A1_freq))
		generation_number = wf_simulation(A1_freq, 10000)[-1]
		generation_list.append(generation_number)
data_dict = dict()
data_dict['Allele frequency'] = af_list
data_dict['No. Generations'] = generation_list
# print(data_dict)
df = pandas.DataFrame(data_dict)
# print(df)

fig5, ax5 = plt.subplots()
ax5.set_title(title) # set the title
ax5 = seaborn.stripplot(data = df, x = 'Allele frequency', y = 'No. Generations', size = 2.0)
seaborn.boxplot(showmeans = True,
            meanline = True,
            meanprops = {'color': 'black', 'ls': '-', 'lw': 1},
            medianprops = {'visible': False},
            whiskerprops = {'visible': False},
            zorder = 10,
            x = 'Allele frequency',
            y = 'No. Generations',
            data = df,
            showfliers = False,
            showbox = False,
            showcaps = False,
            ax = ax5)
plt.tight_layout()
# plt.show()
fig5.savefig('step5.png')