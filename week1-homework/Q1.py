import random
import matplotlib.pyplot as plt
from math import factorial, exp

def coverage_sim(genome_size = int, coverage_x = int, figure_name = str):
	one_mbp_genome = [0] * genome_size
	# print(len(one_mbp_genome))
	read_number = genome_size * coverage_x /100

	for i in range(int(read_number)):
		read_start = random.randrange(len(one_mbp_genome)-100)
		for base_index in range(read_start,read_start+100):
			one_mbp_genome[base_index] += 1

	poisson_y = list()
	lmbd = coverage_x
	for k in range(0, max(one_mbp_genome) + 1):
		y = ((lmbd**k)/factorial(k)) * exp(-lmbd) * len(one_mbp_genome)
		poisson_y.append(y)

	fig, ax = plt.subplots()
	ax = plt.hist(one_mbp_genome, bins = range(0, max(one_mbp_genome) + 1), label = 'Frequence Count of Each Coverage', alpha = 0.5, color = 'green')
	ax = plt.plot(range(0,max(one_mbp_genome) + 1), poisson_y, label = 'Poisson Distribution')
	# print(type(ax))
	plt.title('The Distribution of Coverage')
	plt.xlabel('Coverage')
	plt.ylabel('Frequence Count')
	plt.legend(fontsize = 8)
	plt.yticks(fontsize = 8)
	plt.xticks(range(0, max(one_mbp_genome) + 1), fontsize = 8)
	# plt.show()
	fig.savefig(figure_name)
	plt.close()

	print(one_mbp_genome.count(0))

coverage_sim(1000000, 5, 'Q1-2.png')
coverage_sim(1000000, 15, 'Q1-4.png')
print((5.8 - exp(-15)*1000000)/(exp(-15)*1000000))