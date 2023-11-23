'''
2~9단까지 구구단 출력
짝수단은 역순으로, 홀수단은 정순으로 출력하는 프로그램을 작성하세요.

출력예시)
2 * 9 = 18
2 * 8 = 16
....

3 * 1 = 3
3 * 2 = 6
....
'''

for i in range(2,10):
    if i % 2 == 0:
        for j in range(9, 0 -1):
            print("{} * {} = {}".format(i,j,(i*j)));
    else:
        for j in range(1, 10, 1):
            print("{} * {} = {}".format(i,j,(i*j)));
    print();