import matplotlib.pyplot as plt

'''그래프 영역에 범례를 나타내기 위해서 plt()함수를 label 문자열 지정'''
plt.plot([1,2,3,4],[2,3,5,10],label='label(%)');
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc=('upper right')) # 범례 위치를 지정할 수 있다
plt.show()