'''
매개변수의 기본값 설정해두기
- 매개변수에 기본값 설정하면 함수 호출시 생략 가능
'''

def report(message, who = 'Everyone'):
    print(message, who);
# who 매개변수에 기본값이 할당되어 good moring Everyone 출력
report("good morning");

# 첫번째 입력은 message 매개변수에 두번째 입력은 who 매개변수에 저장한다.
report("good morning","Mr.Park")   # good morning Mr.Park

def is_odd(num):
    if num % 2 == 0:
        print("짝수입니다")
    else:
        print("홀수입니다.")
num = int(input("숫자입력 >> "))
is_odd(num);