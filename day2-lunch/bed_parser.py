#! /usr/bin/env python3
# Usage: python bed_parser.py <.bed file to be parsed>

import sys # import sys

file_name = sys.argv[1] # give file path of .bed file by the first argument in command line after bed_parser.py

def bed_parser(file_name): # define the function bed_parser(), take file path as argument

	fs = open(file_name, mode='r') # open up a file 

	bed = list() # create a list that will store all the needed information from the parsed .bed file
	bed_temp = list() # create a list to tempararily store bed infomation, each line becomes a list containing each field in string as items

	bed_type = [str, int, int, str, float, str, int, int, list, int, list, list] # the list of all the type functions that each field should be

	format_error_number = 0 # create a counter that will be used to count the number of format error (line with 10 or 11 fields)
	format_error_recorder = list() # create a list to store the line number of lines with format error
	format_error_switch = False # a switch to store whether format error occured or not

	count_error_number = 0 # create a counter that will be used to count the number of count error (number of block start/end site can not match block number)
	count_error_recorder = list() # create a list to store the line number of lines with count error
	count_error_switch = False # a switch to store whether count error occured or not

	rgb_error_number = 0 # create a counter that will be used to count the number of rgb error (rgb value does not contain 3 integers)
	rgb_error_recorder = list() # create a list to store the line number of lines with rgb error
	rgb_error_switch = False # a switch to store whether rgb error occured or not
	
	for file_line in fs: # for each line in the file
		fields = file_line.rstrip('\n\r').split('\t') # remove the new line characters and split strings into lists by TAB, each line becomes a list containing each field in string as items
		bed_temp.append(fields) # store the lines generated above in to a temparary holder

	for i, line in enumerate(bed_temp): # go through the bed_temp, obtain index and the content of each line
		try:
			assert len(line) != 10 and len(line) != 11 # try assert this line does not have 10 or 11 fields, if it does, assertion error
		except: # if assertion error
			format_error_switch = True # turn format error switch on
			format_error_number += 1 # format error counter plus 1
			format_error_recorder.append(str(i)) # append the line number into format error recorder list, in string type

		for j in range(min(len(bed_type),len(line))): # go through every items in line list
			if j == 8 or j == 10 or j == 11: # when dealing with the 9th, 11th or 12th lines
				line[j] = line[j].rstrip('\n\r,').split(',') # remove the new line characters and ',', and split strings into lists by ','. Each line becomes a list with several numbers in string type
				for k, item in enumerate(line[j]): # go through each items in the list generated above and get the index of it
					line[j][k] = int(item) # replace the secific string-type item into integer
			elif line[j] != '.': # for lines other than 9, 11, 12
				line[j] = bed_type[j](line[j]) # convert the content into the type it should be

		try:
			assert len(line[11]) == line[9] and len(line[10]) == line[9] # try assert 12th field and 11th field both have the same number of items as the number in 10th field, if not, assertion error
		except: # if assertion error 
			count_error_number += 1 # count error counter plus 1
			count_error_recorder.append(str(i)) # append the line number into count error recorder list, in string type
			count_error_switch = True # turn count error switch on

		try:
			assert len(line[8]) == 3 # try assert the 9th field has 3 integers, if not, assertion error
		except: # if assertion error
			rgb_error_number += 1 # RGB error counter plus 1
			rgb_error_recorder.append(str(i)) # append the line number into RGB error recorder list, in string type
			rgb_error_switch = True # turn RGB error switch on

		bed.append(line[:min(len(bed_type),len(line))]) # appende all the parsed items into bed list

	fs.close() # close the file

	for error_lines in [*set(count_error_recorder + rgb_error_recorder + format_error_recorder)]: # go through the index of all the malformed lines, use '*set' to remove duplicates
		bed.pop(int(error_lines)) # pop these lines out from the output bed list

	if format_error_switch: # if format error switch was turned on
		print(f'FileFormatError: Sorry! But this script does not surpport BED10 or BED11 parsing. There are {format_error_number} format errors.', file = sys.stderr) # print how many such errors there are, give it to standard error.
		print('Please check these lines carefully: Line ' + ','.join(format_error_recorder) + '.', file = sys.stderr) # print which line has such error, give it to standard error
		print('All FileFormatError are listed here. BED10 or BED11 files can not be processed. ^-^', file = sys.stderr) # print the error type again in the end, in case there are to mamy errors. Thus, users can avoide scroll up and down to see the error type
	if count_error_switch:
		print(f'BlockCountError: Sorry! The block count can not match with the number of block start/end points. There are {count_error_number} block count errors.', file = sys.stderr) # print how many such errors there are, give it to standard error.
		print('Please check these lines carefully: Line ' + ','.join(count_error_recorder) + '.', file = sys.stderr) # print which line has such error, give it to standard error
		print('All BlockCountError are listed here. Please check these lines carefully. ^-^', file = sys.stderr) # print the error type again in the end, in case there are to mamy errors. Thus, users can avoide scroll up and down to see the error type
	if rgb_error_switch:
		print(f'RGBError: Sorry! The RGB value need to have three integers. There are {rgb_error_number} RGB errors.', file = sys.stderr) # print how many such errors there are, give it to standard error.
		print('Please check these lines carefully: Line ' + ','.join(rgb_error_recorder) + '.', file = sys.stderr) # print which line has such error, give it to standard error
		print('All RGBError are listed here. Please check these lines carefully. ^-^', file = sys.stderr) # print the error type again in the end, in case there are to mamy errors. Thus, users can avoide scroll up and down to see the error type

	return bed # output bed list

if __name__ == "__main__": # if we run this script
	print(bed_parser(file_name)[:2]) # use the function above to parse .bed file. And print the first two lines of the parsing output list