# Usage: bash bash exercise2.sh [regions_and_states_file.bed] [SNP_file.vcf]
promoter_file=promoters.bed
awk '{if ($4 == "1" || $4 == "2" || $4 == "3" || $4 == "10" || $4 == "11") {print}}' $1 > $promoter_file

intersect_file=intersect.vcf
bedtools intersect -a $2 -b $promoter_file > $intersect_file

snps_file=snps.vcf
awk '/^#/{next} {if ($4 == "C"){print $5}}' $intersect_file > $snps_file

sort $snps_file | uniq -c