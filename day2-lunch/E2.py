#! /usr/bin/env python3
# Usage: python E2.py <.bed file to be analyzed>

import bed_parser as bp # import bed__parser
import sys # import sys
import math # import math for round up and down
import statistics as sss # import statistics for mean()

def takeBlocknumber(line): # define a function to look for the 10th element, used for restrict sort key
	return line[9] # output the 10th element

file_name = sys.argv[1] # give file path of .bed file by the first argument in command line after bed_parser.py
bed_list = bp.bed_parser(file_name) # use the function bed_parser to generate bed list
bed_list.sort(key=takeBlocknumber) # sort th bed list according to the 10th item in it, which is the block number

median_index_number = len(bed_list)/2 # calculate the index of the median 
if int(median_index_number) == median_index_number: # an even number of items
	median_index_1 = int(median_index_number) # the index above the median
	median_index_2 = int(median_index_number - 1) # the index below the median
	median_exon_number = sss.mean([bed_list[int(median_index_1)][9], bed_list[int(median_index_2)][9]]) # median equals to the mean of the two block numbers
else: # an odd number of items
	median_exon_number = bed_list[int(median_index_number)][9] # median is the median, block number locates at the 10th field

print('The median exon number is ' + str(median_exon_number) + '.') # print the median