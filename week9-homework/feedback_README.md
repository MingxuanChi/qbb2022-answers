Great start! Just a few things that need some work:
1. For the clustering, it looks like you're just clustering the transcripts and not the stages. We want to cluster by both genes and stage, and then plot the dendrogram for stage, not transcript (-0.5 point)
2. Your FDR correction isn't quite right. The way you have it currently, you're checking if ANY transcripts are FDR significant, every time you run a regression on a new transcript. Which means that you're reporting that ALL of your transcripts are significant, which definitely isn't right. Run the regression and store the pvals for ALL transcripts, and only then check which of them are significant at 10% FDR (so move the multiple testing outside your for loop) (-1 point)

Otherwise, great job!
(8.5/10)
