#!/usr/bin/env python

# Usage: python load_data.py ddctcf dctcf bin output_file_name

import sys
import math
import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1 import make_axes_locatable


def remove_dd_bg(mat):
    N = mat.shape[0]
    mat2 = numpy.copy(mat)
    for i in range(N):
        bg = numpy.mean(mat[numpy.arange(i, N), numpy.arange(N - i)])
        mat2[numpy.arange(i, N), numpy.arange(N - i)] -= bg
        if i > 0:
            mat2[numpy.arange(N - i), numpy.arange(i, N)] -= bg
    return mat2

def smooth_matrix(mat):
    N = mat.shape[0]
    invalid = numpy.where(mat[1:-1, 1:-1] == 0)
    nmat = numpy.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat

def posi_filter(data, start_bin, end_bin):
    # # data_filtered = numpy.empty(3)
    # # print(data_filtered)
    # for index, line in enumerate(data):
    #     if (line['F1'] >= end_bin) or (line['F1'] <= start_bin) or (line['F2'] >= end_bin) or (line['F2'] <= start_bin):
    #         # print(line)
    #         numpy.delete(data, index, 0)
    return data

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

def main():
    # in1_fname should be ddCTCF
    # in2_fname should be dCTCF
    # bin_fname should be bed file with bin locations
    
    in1_fname, in2_fname, bin_fname, out_fname = sys.argv[1:5]
    data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

    chrom = b'chr15'
    start = 11170245
    end = 12070245
    start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1
    # print(start_bin)
    # print(end_bin)

    data1_filtered = posi_filter(data1, start_bin, end_bin)
    data2_filtered = posi_filter(data2, start_bin, end_bin)
    # print(data1_filtered)
    # print(data2_filtered)

    data1_log = log_transform(data1_filtered)
    data2_log = log_transform(data2_filtered)
    # print(data1_log)
    # print(data2_log)

    data1_shifted = shift_data(data1_log)
    # print(data1_shifted)
    # print(numpy.amin(data1_shifted['score']))
    data2_shifted = shift_data(data2_log)
    # print(data2_shifted)

    matrix1 = produce_matrix(data1_shifted, start_bin, end_bin)
    matrix2 = produce_matrix(data2_shifted, start_bin, end_bin)
    # print(matrix1)
    # print(matrix2)

    matrix1_ddremoved = remove_dd_bg(matrix1)
    matrix1_ddremoved_smoothed = smooth_matrix(matrix1_ddremoved)
    matrix2_ddremoved = remove_dd_bg(matrix2)
    matrix2_ddremoved_smoothed = smooth_matrix(matrix2_ddremoved)
    # print(matrix1_ddremoved_smoothed)
    # print(matrix2_ddremoved_smoothed)

    matrix_diff = numpy.subtract(matrix2_ddremoved_smoothed, matrix1_ddremoved_smoothed)
    # print(matrix_diff)

    vmax = 0
    vmin = - max(numpy.amax(matrix1_ddremoved_smoothed), numpy.amax(matrix2_ddremoved_smoothed))

    fig = plt.figure()
    fig.suptitle(out_fname + ' analysis')
    ax1 = fig.add_subplot(1, 3, 1)
    plt.axis('off')
    divider = make_axes_locatable(ax1)
    ax1_cb = divider.append_axes("left", size="5%", pad=0.05)
    fig = ax1.get_figure()
    fig.add_axes(ax1_cb)
    im1 = ax1.imshow(-matrix1_ddremoved_smoothed, vmax = vmax, vmin = vmin, cmap = 'magma')
    plt.colorbar(im1, cax=ax1_cb)
    ax1_cb.yaxis.tick_left()
    ax1_cb.yaxis.set_tick_params(labelleft=True)
    # plt.colorbar(use_gridspec = True)
    # ax1.set_xticks([])
    # ax1.set_yticks([])

    ax2 = fig.add_subplot(1, 3, 2)
    im2 = ax2.imshow(-matrix2_ddremoved_smoothed, vmax = vmax, vmin = vmin, cmap = 'magma')
    plt.axis('off')
    # ax2.set_xticks([])
    # ax2.set_yticks([])

    ax3 = fig.add_subplot(1, 3, 3)
    plt.axis('off')
    divider = make_axes_locatable(ax3)
    ax3_cb = divider.append_axes("right", size="5%", pad=0.05)
    fig = ax3.get_figure()
    fig.add_axes(ax3_cb)
    im3 = ax3.imshow(matrix_diff, cmap = 'seismic', norm = colors.CenteredNorm())
    plt.colorbar(im3, cax=ax3_cb)
    ax3_cb.yaxis.tick_right()
    ax3_cb.yaxis.set_tick_params(labelright=True)
    # ax3.set_xticks([])
    # ax3.set_yticks([])
    # plt.tight_layout()
    # plt.show()
    fig.savefig(out_fname + '.png')
    plt.close(fig)

if __name__ == "__main__":
    main()
