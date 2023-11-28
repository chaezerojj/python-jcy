'''
* 서브클래스가 슈퍼클래스를 상속받으면
  서브클래스는 슈퍼클래스의 변수, 메소드 기능들을 사용할 수 있다.
'''

class Person:
    def __init__(self, name):
        self.name = name;

    def eat(self, food):
        print(self.name + "가 " + food + "를 먹습니다.")

class Student(Person):
    '''
    super()
    - 상속관계에서 상속의 대상인 부모클래스를 호출하는 함수
    - 자식클래스에서 부모클래스의 기능을 사용하고 싶을 때 사용하면 됨
    '''
    def __init__(self, name, school):
        super().__init__(name);
        self.school = school;

    def study(self):
        print(self.name + "는 " + self.school + "에서 공부합니다.")

potter = Student("해리포터", "호그와트")
potter.eat("피자")
potter.study()