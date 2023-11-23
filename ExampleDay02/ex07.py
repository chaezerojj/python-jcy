'''
* 파이썬에서는 서식문자를 사용할 수 있다

서식문자(format)
- 반드시 따옴표 안에서 작성한다
%d : 정수(int) 10진수
%d : 8진수
%x : 16진수
%f : 실수
%c : 문자
%s : 문자열
'''
a = 10
print("%d" %10); print("%d" %a);
print("%f" %1.22)
print("%.2f" %1.234)
print("%s" %"문자열")
print("%d %d %d" %(10,20,30))
a1 = 100; a2 = 200;
print("%d %d" %(a1,a2))
print("%s %s" %("문자열1","문자열2"))

num1 = 50;
print("%d" %num1);
str1 = "Python"
str2 = "Java"
print("%s" %str1); print("%s %s" %(str1, str2))