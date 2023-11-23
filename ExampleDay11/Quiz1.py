'''
두 수를 입력받아 계산기 프로그램을 작성하세요
계산기 기능
1. 더하기
2. 빼기
3. 곱하기
4. 나누기 (0으로 나누려 하면 '0으로 나눌 수 없습니다'라고 출력)
5. 프로그램 종료
5번을 누르기 전까지는 각 메뉴를 입력받아 그에 해당하는 기능을 수행하도록 작성하세요.
'''

def add(num1, num2):
    return num1 + num2;
def minus(num1, num2):
    return num1 - num2;

def mul(num1, num2):
    return num1 * num2;

def div(num1, num2):
    if num2 == 0:
        return "0으로 나눌 수 없습니다"
    else:
        return num1 / num2;

while True:
    print("=================")
    print("1. 더하기 | 2. 빼기 | 3. 곱하기 | 4. 나누기 | 5. 프로그램 종료")
    print("================")

    choice = int(input("계산기 메뉴 선택 >> "))
    if choice == 1:
        num1 = int(input("숫자 입력 >> "))
        num2 = int(input("숫자 입력 >> "))
        print("더하기 값 : ",add(num1, num2));
    elif choice == 2:
        num1 = int(input("숫자 입력 >> "))
        num2 = int(input("숫자 입력 >> "))
        print("빼기 값 : ",minus(num1, num2));
    elif choice == 3:
        num1 = int(input("숫자 입력 >> "))
        num2 = int(input("숫자 입력 >> "))
        print("곱하기 값 : ",mul(num1, num2));
    elif choice == 4:
        num1 = int(input("숫자 입력 >> "))
        num2 = int(input("숫자 입력 >> "))
        print("나누기 값 :",div(num1, num2));
    elif choice == 5:
        print("프로그램 종료.")
        break;