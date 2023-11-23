import random

computer = random.randint(1, 100)
print("1~ 100 사이 랜덤 숫자 하나를 입력하세요. 그리고 \n이 숫자를 맞추세요. ")
count = 0;
while True:
    user = int(input("숫자 입력 >> "));
    count = count + 1
    if computer > user :
        print("up")