def calc(operator, *args):
    if operator == '+':
        sum = 0;
        for i in args:
            sum = sum + i;
    elif operator == '*':
        sum = 1;
        for i in args:
            sum = sum * i;
    return sum;

print(calc('+',1,2,3,4,5));  # 15
print(calc('*',1,2,3,4,5));  # 120