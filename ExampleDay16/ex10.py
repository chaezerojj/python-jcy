
class A:
    def __init__(self):
        print("A생성자");

class B:
    def __init__(self):
        print("B생성자")

'''
다중상속을 받은 클래스에서 super()를 통해 부모클래스의 생성자로
접근을 할때 순서상 가장 먼저 상속받은 클래스로 접근하게 됨

* 다중 상속 시 모든 부모클래스의 생성자를 호출하려면
각 부모 클래스의 이름을 명시해줘야 함
'''
class C(B, A):
    def __init__(self):
        # super().__init__()
        A.__init__(self);
        B.__init__(self);

c = C()