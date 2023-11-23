'''
숫자를 입력받아 입력받은 숫자 범위 내에서 홀수만 출력하는 프로그램을 작성하세요
'''
num = int(input("숫자입력 >> "))
i = 0
while i < num:
    i = i + 1;
    if i % 2 == 1:
        print(i)