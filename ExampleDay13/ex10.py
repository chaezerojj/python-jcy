import turtle as t

t.speed(0);
t.bgcolor('black')
for x in range(200):
    if x % 3 == 0:
        t.color("red")
    if x % 3 == 1:
        t.color("yellow")
    if x % 3 == 2:
        t.color("blue")

    t.forward(x * 2)
    t.left(119)

t.reset(); # 거북이 그림 삭제하고 기본값으로 복원

angle = 88;
t.color("yellow")
t.speed(0)
for x in range(200):
    t.forward(x)
    t.left(angle)

t.reset()

n = 50;
t.color("red")
t.speed(0)
for i in range(n):
    t.circle(80)
    t.left(360 / n)

t.exitonclick();