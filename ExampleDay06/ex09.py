treeHit = 0

while treeHit < 10:
    treeHit = treeHit + 1;
    print("나무를 {}번 찍었습니다.".format(treeHit))
    if treeHit == 10:
        print("나무가 넘어갑니다.")

'''
숫자를 입력받아 입력받은 숫자만큼 반복문을 실행하세요
1부터 입력받은 숫자를 전부 출력하면 됩니다.
'''

num = int(input("숫자 입력 >> "))
i = 0
while i < num:
    i = i + 1;
    print(i);