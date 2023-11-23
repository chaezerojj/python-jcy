import random
def choice(num):
    if num == 1:
        print("커피")
    elif num == 2:
        print("쿠키")
    elif num == 3:
        print("카스테라")
    elif num == 4:
        print("티라미수")
    elif num == 5:
        print("유자차")
    else:
        print("꽝!")
num = random.randint(1,6)
choice(num)