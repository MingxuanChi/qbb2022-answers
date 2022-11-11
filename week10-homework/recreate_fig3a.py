#!usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# fn = sys.argv[1]
fn = 'DATA.txt'

k562_model_predictions = []
k562_observations = []
gene_names = []
descriptions = []
for i, line in enumerate(open(fn)):
	if line.strip('"').startswith('##'):
		header = np.array(line.strip('"# \r\n').split('\t'))
		k562_obs_idx = np.where(header == 'E123')[0][0]
		# print(k562_obs_idx)
		# print(header)
	elif not line.strip('"').startswith('#'):
		fields = line.strip('"\r\n').split('\t')
		k562_model_predictions.append(float(fields[4]))
		k562_observations.append(float(fields[k562_obs_idx]))
		gene_names.append(fields[1])
		descriptions.append(fields[2])

cor = pearsonr(k562_model_predictions, k562_observations)

genesoi = ["PIM1", "SMYD3", "FADS1", "PRKAR2B", "GATA1", "MYC"]
genesoilocs = []
for geneoi in genesoi:
	genesoilocs.append(np.where(np.array(gene_names) == geneoi)[0][0])
for i in range(len(descriptions)):
	if 'hemoglobin subunit' in descriptions[i]:
		genesoi.append(gene_names[i])
		genesoilocs.append(i)

# make a cool graph
fig, ax = plt.subplots()
ax.scatter(k562_model_predictions, k562_observations, color = 'blue', s = 0.25, alpha = 1)
ax.set_xlabel('Predicted K562 expression level, \n10-folded cross-validated')
ax.set_ylabel('K562 expression level (log10)')
line_xs = np.linspace(max(min(k562_model_predictions),min(k562_observations)), min(max(k562_model_predictions),max(k562_observations)), 100)
line_ys = 1 * line_xs
ax.plot(line_xs, line_ys, color = 'maroon')
ax.text(0.5, 3.75, 'r^2 = ' + str(round(cor.statistic**2, 2)) + '\nn = ' + str(len(k562_observations)))
for geneoi, idx in zip(genesoi, genesoilocs):
	ax.text(k562_model_predictions[idx], k562_observations[idx], geneoi, color = 'maroon', fontweight = 'demi')
ax.spines.top.set_visible(False)
ax.spines.right.set_visible(False)
plt.tight_layout()
# plt.show()
fig.savefig('week10.png')
plt.close(fig)