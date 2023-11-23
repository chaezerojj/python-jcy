import turtle

'''
마우스 클릭으로 도형그리기
'''
window = turtle.Screen();
shape_turtle = turtle.Turtle();

def draw_shape(x, y):
    shape_turtle.penup()
    shape_turtle.goto(x, y)
    shape_turtle.pendown()
    shape_turtle.circle(50)

window.onclick(draw_shape)
window.mainloop()