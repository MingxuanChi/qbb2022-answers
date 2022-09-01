#! /usr/bin/env python
# Usage: python E3.py <joined .txt file (fields: 'indv.', '0', 'pc1', 'pc2', 'pc3', 'population', 'superpopulation', 'sex')>

import matplotlib.pyplot as plt # import matplotlib.pyplot
import matplotlib.colors as clr # import matplotlib.colors
import numpy as np # import numpy
import sys # import sys
import random # import random

def form_item_list(data_array, field_name = str): # define a function to build a list all unique items in each field of an array
	''' # ridiculous strategy 
	item_dict = dict() # create a dictionary for items
	for line in data_array: # for each line in the array
		item_dict.setdefault(line[field_name]) # if the item does not exist in the item_dict, add it
	item_list = list(item_dict) # convert the dictionary into a list
	return item_list # output the item list
	'''
	item_list = np.unique(data_array[field_name]) # use unique function to build the list of each column
	return item_list # output thr item_list

def color_plot(data_array, item_list = list, title_string = str, color_list = list, fig_name_png = str): # define a plot function 
	fig, ax = plt.subplots() # create a figure 
	fig.set_size_inches(8, 5) # set the figure size
	ax.set_title(f'PC1-PC2 PCA for 1K Genome Project SNP (colored by {title_string})') # set the figure title
	ax.set_xlabel('PC1') # set a label for x axis
	ax.set_ylabel('PC2') # set a label for y axis
	for i, item in enumerate(item_list): # for index and items in item_list, e.g. sex
		x_list = list() # create an empty list for x values
		y_list = list() # create an empty list for y values
		for line in data_array: # go through each line in the array
			if item in line: # if the data in this line has the property as the item, e.g. male
				x_list.append(line['pc1']) # add pc1 values in to x_list
				y_list.append(line['pc2']) # add pc2 values in to y_list
		# ax.scatter(x_list, y_list, s = 5, color = color_list[i], label = item) # no need to use a color list
		ax.scatter(x_list, y_list, s = 5, label = item) # draw scatter points
	ncol = round(len(item_list) // 10 + 1) # calculate how many columns of legend is needed
	ax.legend(loc = 1, fontsize = 8, ncol = ncol) # add legend, adjust font size, location, and number of columns
	plt.show() # preview the figure before saving it
	fig.savefig(fig_name_png) # save the figure
	plt.close(fig) # close the figure

# fn = 'joined.txt'
fn = sys.argv[1] # # give file path of joined.txt by the first argument in command line after E3.py

joined_data = np.genfromtxt(fn, dtype = None, encoding = None, names = ['indv', '0', 'pc1', 'pc2', 'pc3', 'pop', 'suppop', 'sex']) # # generate a numpy array from the given .txt file
# print(list(joined_data['pc1'][1:10]))

pop_list = form_item_list(joined_data, 'pop') # build a list for population
pop_title_str = 'population' # give the name of each field, to be used for generate figure title
pop_fig_name = 'ex3_a.png' # assign file names for each figure
suppop_list = form_item_list(joined_data, 'suppop') # build a list for super population
suppop_title_str = 'super population' # give the name of each field, to be used for generate figure title
suppop_fig_name = 'ex3_b.png' # assign file names for each figure
sex_list = form_item_list(joined_data, 'sex') # build a list for sex
sex_title_str = 'sex' # give the name of each field, to be used for generate figure title
sex_fig_name = 'ex3_c.png' # assign file names for each figure

'''
random.seed('2022cmdb') # use a seed to set a random
color_list = random.sample(list(clr.XKCD_COLORS), max(len(pop_list), len(suppop_list), len(sex_list))) # randomly pick out several colors from XCKD color
# print(color_list)
'''

color_plot(joined_data, pop_list, pop_title_str, color_list, pop_fig_name) # draw plot for pc1-pc2 population
color_plot(joined_data, suppop_list, suppop_title_str, color_list, suppop_fig_name) # draw plot for pc1-pc2 super population
color_plot(joined_data, sex_list, sex_title_str, color_list, sex_fig_name) # draw plot for pc1-pc2 sex