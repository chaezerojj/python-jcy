'''
계산기 클래스를 만들고
덧셈, 뺄셈, 곱셈, 나눗셈(/) 연산을 수행하는 클래스를 작성하세요

실행)
숫자 입력 >> 4
연산자 입력 >> +
숫자 입력 >> 5
결과 : 9
'''

class Calculator:

    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def min(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

num1 = int(input("숫자 입력 >> "))
op = input("연산자 입력 >> ")
num2 = int(input("숫자 입력 >> "))
cal = Calculator(num1, op, num2)

if op == '+':
    print(cal.add())
elif op == '-':
    print(cal.min())
elif op == '*':
    print(cal.mul())
elif op == '/':
    print(cal.div())