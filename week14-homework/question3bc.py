#!/usr/bin/env python
# Usage: python question3bc.py

import sys
import os

# def reads_count(file = str):
# 	fs = open(file, 'r')
# 	content = fs.read()
# 	count = content.count('>')
# 	fs.close()
# 	return count

def reads_size(file = str):
	fs = open(file, 'r')
	content_list = fs.readlines()
	genome_str = str()
	for line in content_list:
		line_str = line.strip('\n')
		if '>' not in line_str:
			genome_str += line_str
	size = len(genome_str)
	fs.close()
	return size

bin_file_list = os.listdir('./bins_dir')
assembly_file_path = './metagenomics_data/step0_givendata/assembly.fasta'

# -----------------------------------------------------------------
# Q 3B
# -----------------------------------------------------------------

total_assembly_size = reads_size(assembly_file_path)
total_bin_size = 0

for bin_file in bin_file_list:
	size = reads_size('./bins_dir/' + bin_file)
	bin_name_parts = bin_file.split('.')
	bin_name = '_'.join(bin_name_parts[0:2])
	percentage = str(round(size * 100 / total_assembly_size, 2)) + '%'
	print('The represented percentage in ' + bin_name + ' is: ' + percentage + '.')
	total_bin_size += size

percentage = str(round(total_bin_size * 100 / total_assembly_size, 2)) + '%'
print('The percentage of reads represented by all bins is: ' + percentage + '.')

# -----------------------------------------------------------------
# Q 3C
print('\n-----------------------------------------------------------------\n')
# -----------------------------------------------------------------

for bin_file in bin_file_list:
	size = reads_size('./bins_dir/' + bin_file)
	bin_name_parts = bin_file.split('.')
	bin_name = '_'.join(bin_name_parts[0:2])
	print('The assembled size in ' + bin_name + ' is: ' + str(size) + '.')
