class Person:
    '''
    파이썬에서 클래스 내부에서 메소드를 정의할 때,
    첫번째 인자로 self 사용.
    * self
      - : 인스턴스 자체를 가리킴(즉, 나 자신)
      - 그 객체에 해당하는 메모리 번지를 가리킴
      - 반드시 이 키워드를 써야만 해당 객체 접근 가능
      - 객체 자신을 참조하는 매개변수
    '''
    def sleep(self):
        print("잠잔다");
    def eat(self):
        print("먹는다")
    def run(self):
        print("달린다")

# 클래스는 특정 개념을 표현하고 사용하려면 인스턴스를 생성해야 함
person1 = Person()
person2 = Person()

person1.sleep()
person1.run()
person1.eat()

person2.sleep()
person2.run()
person2.eat()