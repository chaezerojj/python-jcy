'''
* Python에서의 반복문은 크게 2가지 유형이 있다 => for, while

while문
- 조건이 참인 동안 해당하는 코드를 실행
형식)
while <조건문>: (=> 얼마나 몇번? 반복할건지)
      수행문장1
      수행문장2

'''

i = 0 # 초기값 설정
while i < 10: # i값이 10보다 작을 동안
    i = i + 1 # i값을 1씩 증가시킴
    print(i);