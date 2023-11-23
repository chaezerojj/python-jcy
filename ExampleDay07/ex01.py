'''
while문의 형식

초기식
while <조건식>
      i = i + 1 => 증감식
      수행할 문장

1 ~ 10 까지의 수 중에 반복문을 이용하여 짝수를 출력하세요
'''

num = int(input("입력 >> "))
while 1 < num < 10 :
    num = num + 1;
    if num % 2 == 0:
        print(num);