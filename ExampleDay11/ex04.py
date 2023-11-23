'''
리턴값
- 리턴값은 없을 수도 있고, 하나 혹은 여러 값일 수도 있다.

return문이 없는 함수는 None값을 리턴함
(return문은 하나의 객체만 돌려줄 수 있다

* 함수는 실제로 하나의 값을 돌려주는게 원칙,
 하지만 파이썬은 리스트, 튜플, 딕셔너리 등의 자료형에 여러 값을 담아서 돌려줄 수 있음

def 함수명:
    return 10, 20 (가능)
'''

def returnTest():
    return 20,10;

def turnNone(value):
    x = value;

def turnValue(value):
    x = value * 10;
    return x;

print(returnTest());
print(turnNone(10))      # None
print(turnValue(10))        # 100