# Usage: bash step1b.sh

file_list=./metagenomics_data/step0_givendata/KRAKEN/*.kraken
for k_file in $file_list
do
	name=$(echo $k_file | cut -d '/' -f 5 | cut -d '.' -f 1)
	python step1b.py $k_file $name
	echo $name
done

