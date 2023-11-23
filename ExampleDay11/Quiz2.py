'''
세 개의 숫자를 입력받아 가장 큰 수를 출력하는
print_max 함수를 정의하고 가장 큰 수를 출력하세요!
'''

def print_max(a,b,c):
    return (max(a,b,c));

a, b, c = input("숫자 3개 입력 >> ").split();
print(max(a,b,c))

'''
2단부터 9단까지 메뉴 선택에 따라
1. 홀수 구구단
2. 짝수 구구단 
3. 프로그램 종료
출력

홀수 구구단 짝수 구구단 함수 따로
'''

def dan1():
    for i in range(2,10):
        if i % 2 != 0:
            for j in range (1,10):
                print("{} * {} = {}".format(i,j,i*j))
def dan2():
    for i in range(2,10):
        if i % 2 == 0:
            for j in range (1,10):
                print("{} * {} = {}".format(i,j,i*j))

while True:
    print("1. 홀수 구구단 | 2. 짝수 구구단 | 3. 종료")

    choice = int(input("메뉴 입력 >> "))
    if choice == 1:
        dan1()
    elif choice == 2:
        dan2()
    elif choice == 3:
        print("종료");
        break;
