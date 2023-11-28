class Human:
    name = "사람이름";
    age = "나이"
    city = "사는 도시"

    def show(self):
        print("사람 클래스의 메소드")

class Student(Human):
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("사람의 이름은 : ", self.name)

student = Student("홍길동")
'''
부모클래스인 Human클래스를 상속받았으므로
자식 객체가 부모 클래스의 기능 show()메소드를 사용할 수 있다.
'''
student.show()
student.show_name()