#!/usr/bin/env python3

# Usage: python NW_align.py <sequence_file_for_alighment.fa> <match_score_file.txt> gap_penalty(negative) <outputfile>

from fasta import readFASTA
import sys
import numpy as np


# ===============================================================================

# Deal with the macth scores, generate a score array, an index dictionary.

# ===============================================================================

score_fn = sys.argv[2]
# score_fn = 'needleman-wunsch/HOXD70.txt'
# score_fn = 'needleman-wunsch/BLOSUM62.txt'

score_file = open(score_fn, 'r')
score_content = score_file.readlines()
score_file.close()
# print(score_content)

score_col_list = list()
score_col_raw_list = score_content[0].strip(' \n').split(' ')
for item in score_col_raw_list:
	if item != '':
		score_col_list.append(item)
# print(score_col_list)

score_row_list = list()
score_nested_list = list()
for i in range(1, len(score_content)):
	score_row_list.append(score_content[i][0])
	raw_score_line_list = score_content[i][1:].strip('\n').split(' ')
	# print(raw_score_line_list)
	score_line_list = list()
	for item in raw_score_line_list:
		if item != '':
			score_line_list.append(float(item))
	score_nested_list.append(score_line_list)
# print(score_row_list)
# print(score_nested_list)
score_array = np.array(score_nested_list)
# print(score_array)

score_index_dict = dict()
for index_row, row in enumerate(score_row_list):
	for index_col, col in enumerate(score_col_list):
		score_index_dict[row + col] = (index_row, index_col)
# print(score_index_dict)

gap_penalty = float(sys.argv[3])
# gap_penalty = -10


# ===============================================================================

# Reading in sequences.

# ===============================================================================

# input_sequences = readFASTA(open('needleman-wunsch/CTCF_38_M27_AA.faa'))
input_sequences = readFASTA(open(sys.argv[1]))
seq1_id, seq1 = input_sequences[0]
seq2_id, seq2 = input_sequences[1]
# print(seq2)
# print(len(input_sequences))


# ===============================================================================

# Generating F_matrix and traceback matrix (in <'''> comments).

# ===============================================================================

F_matrix = np.zeros((len(seq1)+1, len(seq2)+1))
'''
Trcbk_matrix = np.zeros(len(seq1)+1, len(seq2)+1)
'''
for i in range(0, F_matrix.shape[0]):
	F_matrix[i, 0] = i * gap_penalty
for j in range(0, F_matrix.shape[1]):
	F_matrix[0, j] = j * gap_penalty
# print(F_matrix)

for i in range(1, F_matrix.shape[0]):
	for j in range(1, F_matrix.shape[1]):
		# print((i,j))
		score_index = score_index_dict[seq1[i-1]+seq2[j-1]]
		d = score_array[score_index[0],score_index[1]] + F_matrix[i-1, j-1]
		# print(d)
		h = F_matrix[i, j-1] + gap_penalty
		# print(h)
		v = F_matrix[i-1, j] + gap_penalty
		# print(v)

		F_matrix[i, j] = max(d, h, v)
		
'''
		if F_matrix[i, j] == d:
			Trcbk_matrix[i,j] = 'd'
		elif F_matrix[i, j] == h:
			Trcbk_matrix[i,j] = 'h'
		elif F_matrix[i, j] == v:
			Trcbk_matrix[i,j] = 'v'
'''
# print(F_matrix)


# ===============================================================================

# Traceback to get alignment sequence, gaps and alignment score. Also can use traceback matrix, as in <'''> comments.

# ===============================================================================

traceback_i = F_matrix.shape[0]-1
traceback_j = F_matrix.shape[1]-1
alignment_score = F_matrix[traceback_i, traceback_j]
seq1_back = str()
seq2_back = str()
while traceback_i > 0 or traceback_j > 0:
	score_index = score_index_dict[seq1[traceback_i-1]+seq2[traceback_j-1]]
	if F_matrix[traceback_i,traceback_j] - F_matrix[traceback_i-1, traceback_j-1] == score_array[score_index[0], score_index[1]]:
		seq1_back += seq1[traceback_i-1]
		seq2_back += seq2[traceback_j-1]
		traceback_i -= 1
		traceback_j -= 1
	elif F_matrix[traceback_i,traceback_j] - F_matrix[traceback_i, traceback_j-1] == gap_penalty:
		seq1_back += '-'
		seq2_back += seq2[traceback_j-1]
		traceback_j -= 1
	elif F_matrix[traceback_i,traceback_j] - F_matrix[traceback_i-1, traceback_j] == gap_penalty:
		seq1_back += seq1[traceback_i-1]
		seq2_back += '-'
		traceback_i -= 1

'''
while traceback_i > 0 or traceback_j > 0:
	if Trcbk_matrix[traceback_i,traceback_j] == 'd':
		seq1_back += seq1[traceback_i-1]
		seq2_back += seq2[traceback_j-1]
		traceback_i -= 1
		traceback_j -= 1
	elif Trcbk_matrix[traceback_i,traceback_j] == 'h':
		seq1_back += '-'
		seq2_back += seq2[traceback_j-1]
		traceback_j -= 1
	elif Trcbk_matrix[traceback_i,traceback_j] == 'v':
		seq1_back += seq1[traceback_i-1]
		seq2_back += '-'
		traceback_i -= 1
'''

seq1_align = seq1_back[::-1]
# print(len(seq1_align))
seq1_gap_search = '$' + seq1_align + '$'
seq1_gap_search_list = seq1_gap_search.split('-')
while '' in seq1_gap_search_list:
	seq1_gap_search_list.remove('')
# print(seq1_gap_search_list)
seq1_gap_number = len(seq1_gap_search_list) - 1

seq2_align = seq2_back[::-1]
# print(len(seq2_align))
seq2_gap_search = '$' + seq2_align + '$'
seq2_gap_search_list = seq2_gap_search.split('-')
while '' in seq2_gap_search_list:
	seq2_gap_search_list.remove('')
# print(seq2_gap_search_list)
seq2_gap_number = len(seq2_gap_search_list) - 1


# ===============================================================================

# Writing into outputfile.

# ===============================================================================

output_fn = sys.argv[4]
# output_fn = 'OUTPUT.txt'
output_write = open(output_fn, 'w')
output_write.write('Sequence_1: ' + seq1_id + '\n')
output_write.write(seq1_align + '\n')
output_write.write('Sequence_2: ' + seq1_id + '\n')
output_write.write(seq2_align + '\n')
output_write.write('Alignment_Score:' + str(alignment_score) + '\n')
output_write.write('Number_of_gaps:\n' + 'Sequence_1:' + str(seq1_gap_number) + '\n' + 'Sequence_2:' + str(seq2_gap_number))
output_write.close()
print('Okey Dokey! Alignment finished! Now please find the results in the output file.\nThank you for using!')

