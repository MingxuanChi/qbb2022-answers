#!/usr/bin/env python

import numpy
from scipy.stats import binomtest
from statsmodels.stats.multitest import multipletests
import matplotlib.pyplot as plt
import seaborn
import matplotlib.colors as clr # import matplotlib.colors


def simulate_coin_toss(n_tosses, prob_heads = 0.5, seed=None):
    '''
    Input: n_tosses, an integer, number of coin tosses to simulate
           prob_heads, a float, the probability the coin toss will return heads; default is 0.5, meaning a fair coin
           seed, an integer, the random seed that will be used in the simulation
    Output: results_arr, an array of 1's and 0's with 1's representing heads and 0's representing tails
    Resources: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    '''
    if seed is not None:
        numpy.random.seed(seed)
    results_arr = numpy.random.choice([0,1], size=n_tosses, p = [1-prob_heads, prob_heads])
    return (results_arr)


result = numpy.sum(simulate_coin_toss(10))
result2 = numpy.sum(simulate_coin_toss(10, seed = 4))
# print(result)
# print(result2)


def perform_hypothesis_test(n_heads, n_toss):
    binom_result = binomtest(n_heads, n_toss)
    pval = binom_result.pvalue
    return pval

# print(perform_hypothesis_test(2,5))

def correct_pvalues(pvals):
    corrected_pvalues = multipletests(pvals, method = 'bonferroni')
    return corrected_pvalues[1]

# print(correct_pvalues([.005, .04, .03, .0003, .00001]))

def interpret_pvalues(pvals):
    interpreted = numpy.array(pvals) < 0.05
    return interpreted

def compute_power(n_rejected_correctly, n_test):
    power = n_rejected_correctly / n_test
    return power

def run_experiment(probs, tosses, n_iters = 100, seed = 389, correct_the_pvalues = False):
    numpy.random.seed(seed)
    twodim_arr = numpy.zeros((len(probs), len(tosses)))
    # print(twodim_arr)
    for i_p, prob_heads in enumerate(probs):
        for i_t, n_toss in enumerate(tosses):
            pvals = []
            for k in range(n_iters):
                results_arr = simulate_coin_toss(n_toss, prob_heads = prob_heads)
                n_success = numpy.sum(results_arr)
                pvals.append(perform_hypothesis_test(n_success, n_toss))
            if correct_the_pvalues:
                pvals = correct_pvalues(pvals)
            pvals_translated_to_bools = interpret_pvalues(pvals)
            power = compute_power(numpy.sum(pvals_translated_to_bools), n_iters)
            twodim_arr[i_p][i_t] = power
    return twodim_arr


tosses = numpy.array([10, 50, 100, 250, 500, 1000])
probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
# print(type(probs))

power_array = run_experiment(probs, tosses)
power_array_c = run_experiment(probs, tosses, correct_the_pvalues = True)
# print(power_array)

fig, (ax1, ax2) = plt.subplots(1,2)
fig.set_size_inches(9, 6) # set the figure size
ax1 = plt.subplot(1,2,1)
# ax = seaborn.heatmap(power_array, vmin = 0.02, vmax = 1.0, center = 0.5, cmap = ['xkcd:macaroni and cheese', 'xkcd:orangeish', 'xkcd:blood orange', 'xkcd:cinnamon'], xticklabels = list(tosses), yticklabels = list(probs))
ax1 = seaborn.heatmap(power_array, vmin = 0.02, vmax = 1.0, center = 0.5, cmap = 'viridis', annot = power_array, xticklabels = list(tosses), yticklabels = list(probs))
ax1.set_xlabel('Number of Tosses')
ax1.set_ylabel('Probability of Turning Head')
ax1.title.set_text('Heat Plot of Power in \nCoin Toss Simulation \n(No Correction)')
# plt.show()
ax2 = plt.subplot(1,2,2)
ax2 = seaborn.heatmap(power_array_c, vmin = 0.02, vmax = 1.0, center = 0.5, cmap = 'viridis', annot = power_array_c, xticklabels = list(tosses), yticklabels = list(probs))
ax2.set_xlabel('Number of Tosses')
ax2.set_ylabel('Probability of Turning Head')
ax2.title.set_text('Heat Plot of Power in \nCoin Toss Simulation \n(with Correction)')
plt.show()
fig.savefig('day4-hw.png')
plt.close(fig)