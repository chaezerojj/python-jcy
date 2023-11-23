'''
숫자를 입력받아 그 수의 절대값을 구하세요

입력 >> -5
출력 >> 5

입력 >> 5
출력 >> 5
'''
result = int(input("숫자 입력 >> "))
if result>0:
    print(result)
else:
    print(-result)

'''
수를 입력받아 짝수인지 홀수인지 판단하세요
짝수면 짝수입니다 출력
홀수면 홀수입니다 출력
'''

num = int(input("숫자 입력 >> "))
if num % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")