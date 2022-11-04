# Part 1:  
`bash part1.sh regions.bed methylation.bam hg38.fa`  
  
# Part 2:  
`bash part2.sh`  
  
# Part 3:  
`bash part3.sh`  
  
# Part 4:  
`conda deactivate`  
`conda create -n igv gradle openjdk=11 -y`  
`conda activate igv`  
`git clone https://github.com/igvteam/igv.git`  
  
`cd igv`  
`./gradlew createDist`  
`cd ../`  
  
`ln -s ${PWD}/igv/build/IGV-dist/igv.sh ./`  
  
# Part 5:  
`samtools index h1_cat.bam`  
`samtools index h2_cat.bam`  
  
# Part 6:  
Chr11: KCNQ1OT1
![Example](chr11-KCNQ1OT1.png)  
  
Chr14: MEG3  
![Example](chr14-meg3.png)  
  
Chr15: SNURF  
![Example](chr15-snurf.png)  
  
Chr20: NESP55  
![Example](chr20-nesp55.png)  
  
