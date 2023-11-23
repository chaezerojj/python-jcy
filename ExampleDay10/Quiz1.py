'''
A ~ Z 까지의 알파벳을 입력받아
대문자는 소문자로, 소문자는 대문자로 변경하는 프로그램을 작성하세요.

- ord()함수를 이용 => 문자의 유니코드 숫자값을 리턴하는 함수
'''

# 0~25
print(chr(65)) # A
print(chr(90)) # Z
print(chr(97)) # a
print(chr(122)) # z
print()
print(ord('A'))
print(chr(ord('A')))
print(ord('a')); print(chr(97)); print(ord('A'))
print();



alphabet = input("알파벳을 입력하세요 >> ");
if ord(alphabet) >= 65 and ord(alphabet) <= 90:
    result = ord(alphabet) + 32;
    print(chr(result));
elif ord(alphabet) >= 97 and ord(alphabet) <= 122:
    result = ord(alphabet) - 32;
    print(chr(result))