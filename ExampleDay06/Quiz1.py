'''
3개의 정수를 입력받아
짝수만 출력하세요

실행 예시
1 2 4
2 4

실행 예시
2 4 1
2 4

'''

num1 = int(input("숫자 입력 >> "))
num2 = int(input("숫자 입력 >> "))
num3 = int(input("숫자 입력 >> "))

if num1 % 2 == 0:
    print(num1)
if num2 % 2 == 0:
    print(num2)
if num3 % 2 == 0:
    print(num3)

'''
숫자를 입력받아 그 수가 양수인지 음수인지
판단하는 코드를 작성하세요
'''

num = int(input("숫자 입력 >> "))
if num > 0:
    print("양수입니다")
if num < 0:
    print("음수입니다")