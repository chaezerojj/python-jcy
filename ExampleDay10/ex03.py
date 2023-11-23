'''
range()함수
- 전달된 인수값에 따라 시퀀스 자료형의 데이터를 생성하는 함수
- 특정 범위의 값을 생성하기 때문에 범위 생성자라고 한다.
'''
result1 = list(range(10))
print(result1);

result2 = list(range(1, 11))
print(result2)

result3 = list(range(1, 10, 3))
print(result3);

'''
len()함수
- len()함수에 전달된 객체의 길이를 반환하는 함수
'''
li = ['a','b','c','d','e']
print("li 리스트의 길이 : ", len(li));

str_hello = "Hello World";
print("str_hello 문자열의 길이 : ", len(str_hello))

'''
sorted() 함수
- sorted() 함수에 전달된 반복가능객체(list, tuple) 오름차순 정렬 결과를 반환
'''

my_list = [6,3,1,2,5,4]
print(sorted(my_list)); # 오름차순
print(sorted(my_list, reverse=True)); # 내림차순