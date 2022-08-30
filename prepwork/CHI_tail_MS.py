# USAGE: python CHI_tail.py input_file_path number_of_lines_to_display
import sys

file_name = sys.argv[1] # input file name
number_of_lines = 10 # default number of lines

if len(sys.argv) == 3: # if the user input a specific number
	try:
		number_of_lines = int(sys.argv[2]) # converse to integer
	except ValueError:
		print('Sorry, but you seemed to input an invalid number ~~\n10 lines will be read as default ^o^') # in case the user typed in wrong format

content = [] # create an empty list for storing the lines
for line in open(file_name): # for every line in the opened file
	content.append(line) # append the line into the 'content' list
	if len(content) > number_of_lines: # if the number of lines in 'content' exceed the set number (Indicates that the first item in the list do not belong in the last few lines of the file)
		content.pop(0) # so remove the first item

for line in content: # for every item in 'content'
	print(line.strip('\n\r')) # print the item while remove '\n' or '\r'

# I really like this script. The popping of the first item from the list is
# a really clever way to keep the last n lines without having to store the 
# whole file. I also like your error handling. Your comments are useful and
# I appreciate the blank lines to make the code more readable. I only have
# two points of feedback. First, it is often easier to read if you put long
# comments on their own line. And second, if the user put an extra argument in,
# their requested number of lines would be ignored, even if it were valid.
# You may want your conditional to be if len(sys.argv) >= 3. Overall,
# you clearly have a good grasp of what you are doing. Great work and keep it
# up! - Mike