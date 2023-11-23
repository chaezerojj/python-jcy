'''
index() 메소드
- index()메소드와 find()메소드의 차이점은
  찾는 문자열이 없을 때 발생
'''
s = "apple";
print(s.index('p'));
# print(s.index('k')); >> ValueError: substring not found

'''
대소문자 변환 메소드
- upper() : 문자열을 모두 대문자로 변환한 결과를 반환
- lower() : 문자열을 모두 소문자로 변환한 결과를 반환
- capitalize() : 첫 글자는 대문자로 변환하고 나머지는 소문자로 변환한 결과를 반환
'''
eng_str = "BEST of best";
print(eng_str.upper())  # BEST OF BEST
print(eng_str.lower())  # best of best
print(eng_str.capitalize()) # Best of best


'''
join() 메소드
- 인수로 전달한 반복가능객체(리스트, 문자열 등)의 각 요소 사이에 문자열을 포함시켜 새로운 문자열을 만들고 그 결과를 반환
'''
print('-'.join('python'))   # p-y-t-h-o-n
print('+'.join(['a','b','c','d','e']))  # a+b+c+d+e

'''
split() 메소드
- 하나의 문자열을 여러개의 문자열로 분리해서 저장한 리스트를 반환
- 기본적으로 공백 문자를 기준으로 분리하지만, 특정 문자열을 기준으로 분리할 수도 있다.
'''
s = "Life is too short";
print(s.split())    # ['Life', 'is', 'too', 'short']
s = "010-1234-4567";
print(s.split('-'))     # ['010', '1234', '4567'] / split을 - 로 반환

'''
replace()메소드
- 문자열의 일부 문자열을 다른 문자열로 바꾼 결과를 반환
- 어떤 문자열을 제거하기 위한 용도로도 사용 가능
'''
str1 = "Life is too short";
print(str1.replace('short','long'))     # Life is too long

str2 = "010-1234-1234"
print(str2.replace('-',''))     # 01012341234