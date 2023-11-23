import random
'''
while문을 이용해 두 개의 주사위를 던졌을 때 나오는 눈을 출력하고
눈의 합이 5가 아니면 계속 주사위를 던지고 
눈의 합이 5이면 실행을 멈추세요
종료가 되면 루프를 돈만큼 주사위 합을 출력해주세요.

3번을 돌면
2 + 4 = 6
1 + 3 = 4
2 + 3 = 5  >> 종료

'''
i = 0;
while True:
    a = random.randint(1,6)
    b = random.randint(1,6)
    i = a + b;
    print("{} + {} = {}".format(a, b, (a+b)))
    if i == 5:
        break;