#!/usr/bin/env python
# Usage: python step3.py

import sys
import os
import matplotlib.pyplot as plt

def generate_reads_list(file = str):
	fs = open(file, 'r')
	content_list = fs.readlines()
	reads_list = list()
	for line in content_list:
		# print(line)
		if '>' in line:
			line_str = line.strip('>\n')
			reads_list.append(line_str)
	fs.close()
	return reads_list

bin_file_list = os.listdir('./bins_dir')
assembly_file_path = './metagenomics_data/step0_givendata/KRAKEN/assembly.kraken'

with open(assembly_file_path) as fs_ass:
	assembly_reads_list = fs_ass.readlines()
# print(assembly_reads_list)
assembly_dict = dict()
for read in assembly_reads_list:
	key = read.split('\t')[0]
	phylo = read.split('\t')[1].strip('\n')
	assembly_dict[key] = phylo
# print(assembly_dict)


for bin_file in bin_file_list:
	reads_list = generate_reads_list('./bins_dir/' + bin_file)
	genus_list = list()
	species_list = list()
	for read in reads_list:
		try:
			genus = assembly_dict[read].split(';')[8]
			species = assembly_dict[read].split(';')[9]
			genus_list.append(genus)
			species_list.append(species)
		except IndexError:
			print('Warning: Found one node with missing phylogenetic info when processing file: \n[' + bin_file + ']\nNode ID: ' + read + '.')
			print('Node Info: ' + assembly_dict[read])
			pass
	fig = plt.figure(figsize = (5, 8))
	ax_genus = plt.subplot(2,1,1)
	ax_genus.hist(genus_list)
	ax_genus.set_xlabel('Genus')
	ax_genus.set_ylabel('Read Occurrence')
	ax_genus.set_title('[' + bin_file + '] Distribution of genus identification')
	ax_species = plt.subplot(2,1,2)
	ax_species.hist(species_list)
	ax_species.set_xlabel('Species')
	ax_species.set_ylabel('Read Occurrence')
	ax_species.set_title('[' + bin_file + '] Distribution of species identification')
	plt.xticks(rotation = 45)
	plt.tight_layout()
	# plt.show()
	fig.savefig(bin_file + '.png')
	plt.close(fig)