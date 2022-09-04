#!/usr/bin/env python
# Usage: python E2.py <.txt file with fields: ['Proband_id', 'NO_paternal_ori', 'NO_maternal_ori', 'Father_age', 'Mother_age'], no headers>

import sys
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy import stats

filename = 'proband_fthr_mthr_age.txt'
# filename = sys.argv[1]

proband_array = np.genfromtxt(filename, delimiter = ' ', dtype = None, encoding = None, 
	                          names = ['Proband_id', 'NO_paternal_ori', 'NO_maternal_ori', 'Father_age', 'Mother_age'])
# print(proband_array)

fig_m, ax_m = plt.subplots()
ax_m.scatter(proband_array['Mother_age'], proband_array['NO_maternal_ori'], color = 'red')
ax_m.set_title("Maternal-origin Mutation Number - Mother's Age")
ax_m.set_xlabel("Mother's Age")
ax_m.set_ylabel("Number of Maternal-origin Mutations")
plt.show()
fig_m.savefig('ex2_a.png')
plt.close(fig_m)

fig_f, ax_f = plt.subplots()
ax_f.scatter(proband_array['Father_age'], proband_array['NO_paternal_ori'], color = 'green')
ax_f.set_title("Paternal-origin Mutation Number - Father's Age")
ax_f.set_xlabel("Father's Age")
ax_f.set_ylabel("Number of Paternal-origin Mutations")
plt.show()
fig_f.savefig('ex2_b.png')
plt.close(fig_f)

m_model = smf.ols(formula = "NO_maternal_ori ~ 1 + Mother_age", data = proband_array).fit()
f_model = smf.ols(formula = "NO_paternal_ori ~ 1 + Father_age", data = proband_array).fit()

print(m_model.summary())
print(f_model.summary())

fig_h, ax_h = plt.subplots()
ax_h.hist(proband_array['NO_maternal_ori'], alpha = 0.5, label = 'Maternal-origin Mutation Number', color = 'red')
ax_h.hist(proband_array['NO_paternal_ori'], alpha = 0.5, label = 'Paternal-origin Mutation Number', color = 'green')
ax_h.legend(fontsize = 8)
ax_h.set_title("Occurance of Maternal and Paternal Mutation Number")
ax_h.set_xlabel('Mutation Numbers')
ax_h.set_ylabel('Occurance')
plt.show()
fig_h.savefig('ex2_c.png')
plt.close(fig_h)

ttest_result = stats.ttest_ind(proband_array['NO_maternal_ori'], proband_array['NO_paternal_ori'])
print(ttest_result)

predict_data = proband_array[0]
predict_data.fill(0)
predict_data['Father_age'] = 50.5
print(f_model.predict(predict_data))