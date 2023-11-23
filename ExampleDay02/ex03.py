'''
문자열 인덱싱
- 문자열의 인덱스(index)는 문자열을 구성하는 모든 문자에 부여한 고유의 번호
- 인덱스의 시작 번호는 0
  ex) Hello
      01234
- 문자와 문자 사이 공백도 문자열 포함

'''

str1 = "Hello Python";
print(len(str1))
print(str1[0]); print(str1[2]); print(str1[3]);
print(str1[4]); print(str1[5]); print(str1[6]);

'''
- 문자열 인덱스는 마이너스(-) 인덱스가 존재
- 마이너스 인덱스는 문자열 뒤에서부터 부여하는 번호
'''
print("str1 문자열의 마지막 인덱스 : ", str1[-1]);
print("str1 문자열의 끝에서 두번째 인덱스 : ", str1[-2])