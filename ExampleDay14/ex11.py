'''
그래프 제목 설정
'''
import matplotlib.pyplot as plt

# 빨간색 + 마커 + 실선
#plt.plot([1,2,3,4], [2,3,5,10], 'ro-') # 빨간 원형 점에 실선
# 빨간색 + 마커 + 점선
plt.plot([1,2,3,4], [2,3,5,10], 'ro--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Grape Title')
plt.show()
