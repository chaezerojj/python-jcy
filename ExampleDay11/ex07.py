def turnNone(value):
    x = value;

def turnValue(value):
    x = value * 10;
    return x;

def turnSet(value): # set 자료형 return
    x = {value, value + 1, value + 2};
    return x;

def turnTuple(value): # 튜플형 리턴
    return value, value -1, value -2;

print(turnNone(10))  # None
print(turnValue(10))  # 100
print(turnSet(10))  # {10, 11, 12}
print(turnTuple(10))  # (10, 9, 8)