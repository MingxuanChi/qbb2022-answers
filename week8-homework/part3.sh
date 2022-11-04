for dir in chr11:1900000:2800000 chr14:100700000:100990000 chr15:23600000:25900000 chr20:58800000:58912000
do
	ouput_name=${dir//":"/"-"}
	whatshap split --output-h1 "$ouput_name"_h1.bam --output-h2 "$ouput_name"_h2.bam $dir "$dir"_1
done

samtools cat *_h1.bam -o h1_cat.bam
samtools cat *_h2.bam -o h2_cat.bam