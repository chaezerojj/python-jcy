'''
수를 입력받아서 입력받은 수의 총 합계를 구하세요
-1을 입력받으면 반복이 종료되고
현재까지 입력받은 수의 총 합계를 구하시오.
'''

i = 0;
while True:
    num = int(input("숫자 입력 >> "));
    if num == -1:
        print()
        break;
    i = i + num;
print(i);