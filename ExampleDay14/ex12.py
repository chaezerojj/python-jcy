'''
막대그래프 그리기
terminal > pip install numpy

'''

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(3)
years = ['2021','2022','2023']
values = [19000000, 21000000,22000000]

plt.bar(x, values)
plt.xticks(x, years)
plt.show()