#!/usr/bin/env python3
# Usage: python E2.py <.vcf file need annotation> <reference .vcf file>

import vcfParser as vp # import vcfParser
import sys # import sys

def annote(work_name, ref_name): # define function annote to do annotation, two arguments: first comes the one needs to be annoted (work), second comes the reference (ref)
	work_vcf = vp.parse_vcf(work_name) # use the function in vcfParse to build vcf list for work file
	ref_vcf = vp.parse_vcf(ref_name) # use the function in vcfParse to build vcf list for ref file

	ref_dict = dict() # create a dictionary for ref {(chr#, position):'ID'}
	for line in ref_vcf: # go through every line in ref vcf list
		if line[0] != 'CHROM': # the first item can not be 'CHROM', to exclude the header line
			ref_dict[(line[0],line[1])] = line[2] # use tuple (chr#, position) as the key of ref_dict, give ID as the value

	for work_line in work_vcf: # go through every line in work vcf list
		if work_line[0] != 'CHROM': # the first item can not be 'CHROM', to exclude the header line
			if (work_line[0], work_line[1]) in ref_dict: # if (chr#, position) from work vcf list can match the tuple keys in ref_dict, it means that the two SNP are the same
				work_line[2] = ref_dict[(work_line[0], work_line[1])] # replace the ID in work vcf list with the value of the specific tuple key, annotation

	return work_vcf # output annoted work vcf list 


if __name__ == '__main__': # if we are running this script

	oneKGP_file_name = sys.argv[1] # give file path of 1KGP vcf file by the first argument in command line after E2.py
	dbSNP_file_name = sys.argv[2]# give file path of dbSNP vcf file by the second argument in command line after E2.py
	oneKGP_annoted = annote(oneKGP_file_name, dbSNP_file_name) # use the above fucntion to annote 1KGP vcf list, store it in 'oneKGP_annoted'

	No_ID_number = 0 # create to count the number of SNP without ID
	for line in oneKGP_annoted: # go through every line in oneKGP_annoted
		if line[0] != 'CHROM': # the first item can not be 'CHROM', to exclude the header line
			if line[2] == '.': # if the ID field is a '.', it means no match in dbSNP
				No_ID_number += 1 # the count number plus 1
	print(f'There are {No_ID_number} records not having a corresponding ID in dbSNP.') # finally print the number of total unmatched records

