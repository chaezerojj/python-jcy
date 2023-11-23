'''
내장함수
- 파이썬에서는 항상 사용할 수 있는 많은 함수가 내장되어 있으며 이를 내장함수라고 한다.
예) print(), input()
'''

# chr() 함수
# chr() 함수는 특정 문자의 유니코드 값을 전달하면 해당 유니코드 값을 가진 문자를 반환하는 함수

print(chr(48));
print(chr(65));
print(chr(66)); print(chr(97)); print(chr(98));

print("========================");

'''
ord()함수
- 문자를 전달하면 해당 문자의 유니코드 값을 반환한다
'''
print(ord('A')); print(ord('a'));

'''
eval() 함수
- 문자열로 표현되는 표현식을 실행해서 결과값을 받아오는 함수
'''
result = "1 + 2";
print(eval(result));

x = 1;
print(eval("x + 1"));

a = 10; b = eval('a * 5'); print(b);

print(eval("min(10,30,20)"));  # 10
print(eval("max(10,30,20)"));  # 30

print("=======================")
'''
format()함수
- 전달받은 인수와 포맷 코드에 따라 형식을 갖춘 문자열을 반환하는 함수
'''
print(format(10000));
print(format(100000,'_')); # 천단위 구분 기호로 밑줄을 표시 100_000
print(format(100000000,',')) # 천단위 구분 기호로 쉼표를 표시 100,000,000

print("=======================")

'''
str()함수
- 전달받은 인수를 문자열로 변환
'''
print(str(10)); print(type(str(10)));
x = 20;
change_x = str(x);
print(change_x); print(type(change_x)); print(type(x));