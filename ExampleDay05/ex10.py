'''
and, or, not

and : x 와 y 모두 참이어야 참
or : x와  y 둘중에 하나만 참이어도 참
not : x가 거짓이면 참
'''
money = 2000;
card = True

if money >= 3000 or card:
    print("택시타고 가라")
else:
    print("걸어가라")