'''
실행 결과와 같은 간단한 계산 기능을 수행하는 프로그램을 작성하세요
단, 나눗셈 연산 시 몫만 출력하세요
실행 예)
기능 선택
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
계산기 기능을 선택하세요 (1/2/3/4) >> 3
첫번째 숫자를 입력하세요 >> 5
두번째 숫자를 입력하세요 >> 10
5 * 10 = 50
'''

choice = int(input("계산기 기능을 선택하세요 (1/2/3/4) >> "))
num1 = int(input("첫번째 숫자를 입력하세요. >> "))
num2 = int(input("두번째 숫자를 입력하세요. >> "))
if choice == 1:
    print("{} + {} = {}".format(num1, num2, (num1 + num2)))
elif choice == 2:
    print("{} - {} = {}".format(num1, num2, (num1 - num2)))
elif choice == 3:
    print("{} * {} = {}".format(num1, num2, (num1 * num2)))
elif choice == 4:
    print("{} // {} = {}".format(num1, num2, (num1 // num2)))