'''
input()함수
- 사용자가 입력을 받을 때 사용
- input() 함수는 입력되는 모든 것을 문자열로 취급
- 다른 타입을 입력받고 싶을 시 형 변환을 해주어야 함!
'''
a = input("문자열 입력 >> ");
print(a); print(type(a));

name = input("이름입력 >> ")
age = input("나이입력 >> ")
gender = input("성별입력 >> ")
address = input("주소입력 >> ")

print("이름 : ", name)
print("나이 : ", age)
print("성별 : ", gender)
print("주소 : ", address)