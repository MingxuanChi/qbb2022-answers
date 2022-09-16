fn = 'OUTPUT.fasta'
output_list = list()
for i in open(fn):
	output_list.append(int(i.split('\t')[1]))
total_base = sum(output_list)
add_up = 0
while add_up < total_base*0.5:
	longest = max(output_list)
	add_up += longest
	output_list.remove(longest)
n50 = longest
print(n50)