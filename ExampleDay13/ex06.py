import turtle as t
'''
반복문을 사용해서 사각형 그리기
'''

t.shape("arrow")
t.color("grey")
t.speed(1)
for i in range(4):
    t.forward(140);
    t.left(360 / 4);

t.exitonclick()