import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [1,1,1,1], '-', color='green',
         linewidth="14.4")
plt.plot([1,2,3,4], [2,2,2,2], ':', color='yellow')
plt.plot([1,2,3,4], [3,3,3,3], '-.', color='red')
plt.plot([1,2,3,4], [4,4,4,4], '--', color='blue')
plt.show()