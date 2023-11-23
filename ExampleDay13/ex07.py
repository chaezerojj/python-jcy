import turtle as pet

'''
거북이 위치 이동시키기
'''
pet.shape("turtle");
pet.goto(100,0) # goto(): 특정 위치로 이동시키는 함수
pet.dot(20, "red"); # 점을 찍는 함수
pet.goto(100,100);
pet.dot(20,"green")
pet.goto(0,100)
pet.dot(20,"blue")
pet.goto(0,-1);
pet.dot(20,"purple")

pet.exitonclick()