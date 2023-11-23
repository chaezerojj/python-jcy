# 거북이의 이름을 pet으로 지정
import turtle as pet
pet.speed(1);

# shape를 turtle로 지정하면,
# 화살표가 아닌 거북이 모양으로 바뀜

pet.shape("turtle");
pet.color("green") # 거북이 색상 지정

pet.begin_fill(); # begin_fill()로 색칠할 준비
for i in range(5): # 오각형 만들기
    pet.forward(100);
    pet.left(360 / 5)
pet.end_fill(); # 도형을 다 그린 후 도형에 현재 펜 색이 칠해짐
pet.exitonclick();
