for dir in chr11:1900000-2800000 chr14:100700000-100990000 chr15:23600000-25900000 chr20:58800000-58912000
do
	region=${dir/"-"/":"}
	echo $region
	whatshap haplotag -o $region -r hg38.fa --output-haplotag-list "$region"_1 --regions $region $dir/*.gz methylation.bam
done