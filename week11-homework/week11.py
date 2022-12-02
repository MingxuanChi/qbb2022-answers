#!/usr/bin/env python
# Usage: python week11.py

import scanpy as sc
import matplotlib.pyplot as plt

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()
# print(adata.X)

sc.tl.pca(adata)
sc.pl.pca(adata, save = '_before_filter.png', title = 'PCA before filtering')

sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)

sc.tl.pca(adata)
sc.pl.pca(adata, save = '_after_filter.png', title = 'PCA after filtering')

sc.pp.neighbors(adata)
sc.tl.leiden(adata)
sc.tl.umap(adata, maxiter = 1000)
sc.pl.umap(adata, title = 'UMAP', save = '_leiden.png', color = 'leiden')
cluster2annotation = {
	'25': 'Pericytes',
	'23': 'All types of ECs',
	'26': 'Microglia',
	'24': 'Astrocyte',
	'21': 'Oligodendrocytes',
	'8': 'All Fibroblast-like types'
	}
adata.obs['cell type'] = adata.obs['leiden'].map(cluster2annotation).astype('category')
sc.pl.umap(adata, color='cell type', legend_loc='on data',
           frameon=False, legend_fontsize=10, legend_fontoutline=2, save = '_labeled_leiden.png')
# sc.pl.umap(adata, title = 'Mdk_UMAP', save = '_FB_Mdk_leiden.png', color = 'Mdk')
# sc.pl.umap(adata, title = 'Eomes_UMAP', save = '_FB_Eomes_leiden.png', color = 'Eomes')
# sc.pl.umap(adata, title = 'Mfap4_UMAP', save = '_FB_Mfap4_leiden.png', color = 'Mfap4')
# sc.pl.umap(adata, title = 'Zbtb20_UMAP', save = '_FB_Zbtb20_leiden.png', color = 'Zbtb20')
# sc.pl.umap(adata, title = 'Tmem108_UMAP', save = '_FB_Tmem108_leiden.png', color = 'Tmem108')
# sc.pl.umap(adata, title = 'Trim59_UMAP', save = '_FB_Trim59_leiden.png', color = 'Trim59')
# sc.pl.umap(adata, title = 'Fa2h_UMAP', save = '_FB_Fa2h_leiden.png', color = 'Fa2h')
# sc.pl.umap(adata, title = 'Adamts4_UMAP', save = '_AC_Adamts4_leiden.png', color = 'Adamts4')
sc.tl.tsne(adata)
sc.pl.tsne(adata, save = '_leiden.png', title = 'tSNE', color = 'leiden')

sc.tl.rank_genes_groups(adata, 'leiden', method = 't-test')
sc.pl.rank_genes_groups(adata, sharey = False, title = 't-test clustered genes', save = '_t-test.png')

sc.tl.rank_genes_groups(adata, 'leiden', method = 'logreg')
sc.pl.rank_genes_groups(adata, sharey = False, title = 'logistic regression clustered genes', save = '_logreg.png')