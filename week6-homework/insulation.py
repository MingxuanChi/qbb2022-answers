#!/usr/bin/env python

# Usage: python insulation.py 40kb output_file_name

import sys
import math
import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1 import make_axes_locatable

def log_transform(data):
    data_to_be_calculated = numpy.copy(data)
    for index, line in enumerate(data):
        score = data_to_be_calculated[index]['score']
        line[2] = math.log(score, 10)
    return data

def shift_data(data):
    minimum = numpy.amin(data['score'])
    # print(minimum)
    for line in data:
        line[2] -= minimum
    return data

def produce_matrix(data, start_bin, end_bin):
    matrix_array = numpy.zeros((end_bin - start_bin -1, end_bin - start_bin - 1), dtype = float)
    for line in data:
        # print(line)
        if (line['F1'] < end_bin) and (line['F1'] > start_bin) and (line['F2'] < end_bin) and (line['F2'] > start_bin):
            # print((line[0] - start_bin - 1, line[1] - start_bin - 1))
            matrix_array[line[0] - start_bin - 1][line[1] - start_bin - 1] = line[2]
            matrix_array[line[1] - start_bin - 1][line[0] - start_bin - 1] = line[2]
    return matrix_array

in1_fname, out_fname = sys.argv[1:3]
data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
    ('F1', int), ('F2', int), ('score', float)]))

data_log = log_transform(data1)
data_shifted = shift_data(data_log)
matrix = produce_matrix(data_shifted, 54878, 54951)

mean_list = list()
for i in range(len(matrix)):
	mean = numpy.mean(matrix[(i - 5):i, i:(i + 5)])
	mean_list.append(mean)

vmax = 0
vmin = - numpy.amax(matrix)

fig = plt.figure()
fig.suptitle(out_fname + ' analysis')
ax1 = fig.add_subplot(2, 1, 1)
plt.axis('off')
divider = make_axes_locatable(ax1)
ax1_cb = divider.append_axes("left", size="5%", pad=0.05)
fig = ax1.get_figure()
fig.add_axes(ax1_cb)
im1 = ax1.imshow(-matrix, vmax = vmax, vmin = vmin, cmap = 'magma')
plt.colorbar(im1, cax=ax1_cb)
ax1_cb.yaxis.tick_left()
ax1_cb.yaxis.set_tick_params(labelleft=True)

ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(mean_list)
ax2.set_xticks([0, 54951-54878], ['chr15:10400000', '13400000'])
ax2.set_title('Insulation Score')

plt.show()
fig.savefig(out_fname + '.png')
plt.close(fig)

