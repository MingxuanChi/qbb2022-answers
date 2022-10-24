# Week 3 Variant Calling -- Feedback

1 + 1 + 1 + 0.5 + 1 + 1 + 1 + 1 + 1 + 1 = 9.5 points out of 10 possible points

1. Index genome

  * --> +1

2. align reads

  * good for loop; --> +1

3. sort bam files and index sorted bam files (0.5 points each)

  * consider using a single for loop for questions 2 and 3 --> +1

4. variant call with freebayes

  * should include the `-p 1` flag since the yeast ploidy is 1.
  * should include the `--genotype-qualities` flag since we're asking you to plot a histogram of the GQ (variant genotype qualities)
  * --> +0.5
  * nice exploration of the different ways you could call freebayes passing multiple bam files

5. filter variants

  * --> +1

6. decompose complex haplotypes

  * --> +1

7. variant effect prediction

  * --> +1

8. python plotting script

  * --> +1; nice script overall. Would recommend GQ in the Format/sample specific column, not QUAL in column 5. You want the genotype quality and genotypes are sample specific

9. 4 panel plot (0.25 points each panel)

  * great plot; I like the layout a lot.
  * the text size is a little too small. Here are some examples in a [stackoverflow post](https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot) on how to increase the font size.
  * --> +1

10. 1000 line vcf

  * --> +1

Very good comments and echo statements in your scripts
