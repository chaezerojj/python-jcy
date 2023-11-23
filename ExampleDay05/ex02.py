'''
대입연산사
- 변수에 값을 저장하기 위해 사용하는 연산자
- 대입연산자는 '='는 반드시 왼쪽에 변수가 배치되고 오른쪽에 저장할 값이 배치

복합 대입 연산자
- 복합 대입 연산자를 통해서 연산을 먼저 진행하고 그 결과를 변수에 저장

예)
a += 2
b -= 2
c *= 2
d /= 2
'''

# 대입연산자
a = 10;
print(a)
val1 = 100; val2 = 200; val3 = 300;
print(val1); print(val2); print(val3);

# 복합 대입 연산자
b = 0;
b += 2; # b = b + 2
print(b);
b += 2;
print(b);
b -= 1; # b = b - 1
print(b);

# 저금통에 용돈을 넣고 빼는 과정
piggy_bank = 0;
money = 10000;
piggy_bank += money;
print("저금통에 용돈 {}원을 넣었습니다.".format(money));
print("지금 저금통에 {}원이 있습니다.".format(piggy_bank));

snack = 2000;
piggy_bank = piggy_bank - snack;
print("저금통에서 스낵 구입비 {}원을 뺐습니다.".format(snack));
print("지금 저금통에는 {}원이 있습니다.".format(piggy_bank));
