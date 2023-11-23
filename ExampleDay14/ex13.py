'''
산점도 그래프
'''
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0);

n = 50;
x = np.random.rand(n) # 난수 생성
y = np.random.rand(n)

plt.scatter(x, y) # x,y 값에 해당하는 위치에 기본 마커가 표시됨
plt.show()