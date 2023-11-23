import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[2,3,5,10],label='Demo1');
plt.plot([1,2,3,4],[3,10,9,12],label= 'Demo2')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best', ncol=2, fontsize='xx-large')
plt.show()