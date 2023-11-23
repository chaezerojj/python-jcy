# 파라미터수를 정하지 않았으므로 1개, 2개, .... n개 일수도 있다.

def myFunc(*args):
    for arg in args:
        print(arg);

myFunc(10,20,'a');
myFunc('apple','banana',1.0,10,3.141592)

p1 = [10, 20, 30]
myFunc(p1)