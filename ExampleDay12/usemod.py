'''
직접 생성한 모듈
* 파이썬 확장자 .py로 만든 파이썬 파일은 모두 모듈이 될 수 있다.
'''
def add(a,b):
    return a + b;

def sub(a,b):
    return a - b;

def odd_even(x):
    if x % 2 == 1:
        print("홀수");
    elif x % 2 == 0:
        print("짝수");