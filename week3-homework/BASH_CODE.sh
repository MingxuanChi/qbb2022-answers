# Usage: bash BASH_CODE.sh

# Step_1
bwa index sacCer3.fa
echo "Step1 BWA	finished!"

# ------------------------------------------------------------------------------------------------------------------

# Step_2
for SAMPLE in 09 11 23 24 27 31 35 39 62 63
do 
	bwa mem \
	-R "@RG\tID:A01_${SAMPLE}\tSM:A01_${SAMPLE}" \
	-t 4 \
	-o A01_${SAMPLE}.sam \
	sacCer3.fa A01_${SAMPLE}.fastq
done
echo "Step2 BWA MEM finished!"

# ------------------------------------------------------------------------------------------------------------------

# Step_3a
for SAMPLE in 09 11 23 24 27 31 35 39 62 63
do 
	samtools sort -@4 -O bam -o A01_${SAMPLE}.bam A01_${SAMPLE}.sam
done

# ------------------------------------------------------------------------------------------------------------------

# Step_3b
for SAMPLE in 09 11 23 24 27 31 35 39 62 63
do
	samtools index -b A01_${SAMPLE}.bam
done
echo "Step3 SAMTOOLS finished!"

# ------------------------------------------------------------------------------------------------------------------

# Step_4
freebayes -f sacCer3.fa -= \
*.bam \
> OUTPUT.vcf

# Alternative way 1:
# freebayes -f sacCer3.fa -= \
# A01_09.bam A01_11.bam A01_23.bam A01_24.bam A01_27.bam A01_31.bam A01_35.bam A01_39.bam A01_62.bam A01_63.bam \
# > OUTPUT.vcf

# Alternative way 2:
# ls | grep -v "bai" | grep bam > bm_file.txt
# freebayes -f sacCer3.fa -= \
# -L bm_file.txt \
# > OUTPUT.vcf
echo "Step4 FREEBAYES finished!"

# ------------------------------------------------------------------------------------------------------------------

# Step_5
vcffilter -f "QUAL > 20" OUTPUT.vcf > OUTPUT_filtered.vcf
echo "Step5 VCF_FILTER finished!"

# ------------------------------------------------------------------------------------------------------------------

# Step_6
vcfallelicprimitives -k -g OUTPUT_filtered.vcf > OUTPUT_filtered_decomposed.vcf
echo "Step6 VCF_DECOMPOSING finished!"

# ------------------------------------------------------------------------------------------------------------------

# Step_7 (downgradation part is in README.md)
snpeff ann -formatEff R64-1-1.99 OUTPUT_filtered_decomposed.vcf > OUTPUT_filtered_decomposed_annotated.vcf
echo "Step7 SNPEFF_ANNOTATION finished!"

# ------------------------------------------------------------------------------------------------------------------

# Step_8
python VCF_plot.py OUTPUT_filtered_decomposed_annotated.vcf
echo "Step8 PLOTING finished!"

# ------------------------------------------------------------------------------------------------------------------

echo "Thank you for using this! Please find the .png figue at the current directory."