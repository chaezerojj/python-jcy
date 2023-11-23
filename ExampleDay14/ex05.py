import matplotlib.pyplot as plt
# 사용할 폰트명 경로 삽입
from matplotlib import font_manager, rc

font_path = "C:\Windows\Fonts\H2GTRE.TTF";
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

plt.plot([1,2,3,4],[2,8,10,16]);
plt.xlabel('X축')
plt.ylabel('Y축')
plt.show()