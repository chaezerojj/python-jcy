'''
1 ~ 10까지 전달받은 값의
짝수의 합계를 구하세요
'''
def add_many(*args):
    result = 0
    for i in args:
        if i % 2 == 0:
            result = result + i;
    return result;

print(add_many(1,2,3,4,5,6,7,8,9,10));

