'''
파이썬에서는 자바와 달리 소멸자가 있다.

* 소멸자(Destructor)
- 인스턴스가 생성이 될 때 생성자가 자동으로 생성되는 것과 같이 클래스가 소멸될 때, 자동으로 소멸자를 호출함

'''

class Line:
    length = 0;

    def __init__(self, length):
        self.length = length;

    def __del__(self):
        print(self.length, "길이의 선이 삭제되었습니다.");

    def __add__(self, other):
        return self.length + other.length;

myLine1 = Line(100);
myLine2 = Line(200);

print("두 선의 길이 합: ", myLine1 + myLine2)
del(myLine1);
del(myLine2);