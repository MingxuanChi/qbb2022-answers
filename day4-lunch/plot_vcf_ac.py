#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

vcf = sys.argv[1]
# vcf = 'exons.chr21.bed.vcf'
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    # print(line)
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )

fig, ax = plt.subplots()
ax.hist( ac, density=True, log = True )
vcf_keyword = vcf.split('.')[0]
title_or_label_str = vcf_keyword[:1].upper()+vcf_keyword[1:]
ax.set_ylabel(f'Log Density')
ax.set_title(f'Log Density of SNPs Allele Count in {title_or_label_str}')
ax.set_xlabel(f'Allele Counts')
plt.show()
fig.savefig( vcf + ".png" )

fs.close()

