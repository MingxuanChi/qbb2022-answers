# Usage: bash step2b.sh

file_list=./metagenomics_data/step0_givendata/READS/*_1.fastq
for k_file in $file_list
do
	name=$(echo $k_file | cut -d '/' -f 5 | cut -d '_' -f 1)
	# echo $k_file
	path="./metagenomics_data/step0_givendata/READS/${name}"
	bwa mem -t 4 ./metagenomics_data/step0_givendata/assembly.fasta "${path}_1.fastq" "${path}_2.fastq" > "${path}.bam"
	samtools sort "${path}.bam" -@ 4 -o "${name}_sorted.bam"
	echo $name
done

