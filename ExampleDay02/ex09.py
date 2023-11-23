'''
format 함수
- 포매팅이란 문자열 중간 중간에 특정 변수의 값을 넣어주기 위해 사용하는 것
- 문자열을 출력할 때 서식 지정자를 사용하여 출력하는 경우에 사용
- format() 함수의 인자값으로 여러개의 변수를 받아서 처리하는 경우 인덱스 값으로 기준을 정한다
- 중괄호 안에 인텍스는 생략 가능

'''

a = 8; b = 2;
print("{} * {} = {}".format(a,b,(a * b)))
print("{1} * {0} = {2}".format(a,b,(a * b)))

s1 = 'name : {0}'.format('blockDM');
print(s1)

age = 28
s2 = 'age : {}'.format(age)
print(s2)

# 인덱스의 순서가 바뀐 예제
s5 =  'song1 : {1}, song2 : {0}'.format('song1','song2')
print(s5)

str2 = 'name : {}, city : {}'.format("윤준형","Busan")
print(str2)