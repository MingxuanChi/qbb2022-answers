## Week 5 -- 10 points possible

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1  = 10 points out of 10

1. Filter reads, Call peaks, and intersect peaks across Sox2 replicates (0.33 points each)

2. Find the number of total peaks and overlapping peaks for Klf4 and Sox2 (0.5 for commands, 0.5 for result)

3. scale bedgraph files (4 different datasets, 0.25 each)

* assuming this in the .sh script that isn't uploaded

4. crop bedgraph files (4 different datasets, 0.25 each)

* assuming this in the .sh script that isn't uploaded

5. python script for plotting

* great use of `glob` to read in the filenames
* fantastic script overall

6. 4 panel plot of read pile ups

* Barplot? Would recommend using `plot` for the line and then `fill_between` to fill in the plotting area.
* Nice use of the tick marks and tick mark labels so that we can see the different scales. Most would prefer using the same scale/max value for all four subplots.

7. motif finding sort intersected sox2 replicate narrow peak by 5th columm, keep first 300 lines, awk command for reformatting (0.33 each)

8. use samtools faidx to extract peak sequences and meme-chip to perform motif finding (0.5 each)

9. download and unpack motif database

10. match profiles from tomtom for klf4 and sox2 (0.5 for commands, 0.5 for result)

Very good overall! Please add `Q1_STEP5.sh` for the scaling and cropping steps, but you have full credit since the files seem to be made prior to the python script being run
