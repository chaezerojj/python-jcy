# 두 변수 값 교환
a1 = 10;
b1 = 20;
print("a1의 값 : ", a1); print("b1의 값 : ", b1);
temp = a1; # temp에 a1 값을 저장
a1 = b1; # b1값이 a1에 저장됨
b1 = temp; # b1에는 temp값이 저장됨
print("a1의 값 : ", a1); print("b1의 값 : ", b1);

# 세 수의 합계 구하기
kor = 90; mat = 40; eng = 70;
sum = kor + mat + eng;
print("국영수 점수 총 합 : ", sum);
avg = sum // 3;
print("국영수 평균 : ", avg);

'''
+= : 숫자를 더한 후 대입
-= : 숫자를 뺀 후 대입
*= : 숫자를 곱한 후 대입
/= : 숫자를 나눈 후 대입
//= : 숫자를 나눈 후 그 몫만 대입
%= : 숫자를 나눈 후 그 나머지만 대입
**= : 숫자를 제곱한 후 대입
'''
num = 100;
print(num);

num += 10; print(num);
num *= 2; print(num);
num /= 2; print(num);
num *= 3; print(num);

greet = "안녕";
greet = greet + '하세요';
print(greet);
greet *= 2;
print(greet)