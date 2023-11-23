import turtle as t

n = 50;
t.bgcolor("black") # 창 배경색 지정
t.speed(0);
t.color("yellow") # 선 색 지정
for i in range (70):
    t.circle(80);
    t.left(360 / n);

t.exitonclick();
