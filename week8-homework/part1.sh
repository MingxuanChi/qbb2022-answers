FILE="$1"
BAM="$2"
FASTA="$3"
colon=":"
dash="-"

while read -r line
do
	line=${line/"	"/"$colon"}
	line=${line/"	"/"$dash"}
	echo $line
	medaka_variant -i $BAM -s r941_prom_snp_g360 -m r941_prom_variant_g360 -f $FASTA -p -r $line -o $line
done < "$FILE"