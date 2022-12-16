# Usage: bash step1c.sh

for txt_file in *krona.txt
do
	name=$(echo $txt_file | cut -d '_' -f 1)
	ktImportText $txt_file -q -o "${name}graph.html"
	echo $name
done