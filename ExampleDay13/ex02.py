import turtle
from turtle import *

''' 정삼각형 그리기 '''

speed(1); # 1: 가장 느리게
forward(140); # 앞으로 140만큼 이동
left(120); # 왼쪽으로 120만큼 회전
forward(140); # 회전한 상태에서 140만큼 이동 (위로 감)
left(120); # 왼쪽으로 다시 120 회전
forward(140); # 회전한 상태에서 140만큼 이동

# 마우스로 그래픽창을 클릭했을 때 창이 닫히도록 함
turtle.exitonclick();