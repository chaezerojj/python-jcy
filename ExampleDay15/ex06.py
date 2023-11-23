'''
어느 직사각형의 정보를 출력하고 넓이를 구하는 클래스를 만드세요.
'''

class Rectangle:
    # 필드(멤버변수): 데이터를 표현하는 속성
    result = 0;
    width = 0;
    height = 0;

    # 메소드 : 클래스의 어떠한 행위를 표현하는 것
    def arga(self):
        self.result = self.width * self.height;
        return self.result;

    def info(self):
        print("가로길이는 : {}".format(self.width))
        print("세로길이는 : {}".format(self.height))

# 인스턴스 : 추상적인 개념을 구체화시킨 것
rectangle = Rectangle();
width = int(input("가로 입력 >> "));
height = int(input("세로 입력 >> "));

# rectangle의 width, height라는 속성에 값을 할당
rectangle.width = width
rectangle.height = height

print("직사각형의 넓이 : ", rectangle.arga())
rectangle.info();