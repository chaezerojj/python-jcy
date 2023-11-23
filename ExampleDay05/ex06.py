'''
삼항 연산자
- 참 if 조건식 else 거짓
- 전체를 하나의 식으로 생각해야 한다
- if ~ else 문을 통해서 해결할 수 있는 연산을 한 줄로 간단하게 나타낼 수 있다.

[True] if [값] else [False]
'''
num1 = 20; num2 = 10;
result = num1 if num1 > num2 else num2;
print("두 수중 큰 값 : ", result);

a = int(input("숫자입력 >> "))
print("짝수입니다.") if a % 2 == 0 else print("홀수입니다.")