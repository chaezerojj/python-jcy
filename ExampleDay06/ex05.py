'''
두 정수 a와 b를 입력받아서
두 정수의 크기를 비교하여 왼쪽 수가 크면 > 출력
오른쪽 수가 크면 < 출력
두 수가 같다면 =를 출력
'''

num1 = int(input("숫자 입력 >>"))
num2 = int(input("숫자 입력 >>"))

if num1 > num2:
    print(">")
elif num1 < num2:
    print("<")
else:
    print("=")