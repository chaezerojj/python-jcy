'''
사용자로부터 양의 정수를 하나 입력 받은 뒤
그 수만큼 3의 배수를 출력하는 프로그램을 작성하세요

예시)
입력 >> 5
출력 >> 3 6 9 12 15
'''

# i % 3 == 0

num = int(input("숫자 입력 >> "));
i = 1;
while i <= num:
    print(i * 3);
    i = i + 1;