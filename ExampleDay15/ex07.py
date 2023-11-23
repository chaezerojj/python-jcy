class Calculator:
    '''
    __init__(self)
    - 클래스의 인스턴스를 초기화하는 생성자
    - 클래스가 인스턴스화 될 때 자동 호출
    '''
    def __init__(self):
        self.result = 0;

    def add(self, num):
        self.result = self.result + num;
        return self.result;

cal1 = Calculator();
cal2 = Calculator();
print(cal1.add(3));
print(cal1.add(7));

print("===============");
print(cal2.add(10));
print(cal2.add(20));