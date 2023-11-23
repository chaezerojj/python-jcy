'''
파이썬은 크게 표준 라이브러리, 외부 라이브러리로 나눌 수 있다.

표준 라이브러리
- 기본적으로 제공되는 라이브러리
외부 라이브러리
- 별도의 파일을 설치해야 사용할 수 있는 라이브러리
'''
import datetime
import math

import usemod

# import datetime

r1 = math.gcd(12,24)
print(r1);  # 12

r2 = math.lcm(15,27);
print(r2);  # 135

'''
'datetime' 내장 모듈의 'timedelta' 클래스는 기간을 표현하기 위해 사용됨
'''
from datetime import timedelta
print(timedelta(days=5, hours=17, minutes=30))

day1 = datetime.date(2023,11,14)
day2 = datetime.date(2017,5,31)
diff = day1 - day2
print("두 날짜 간 차이 : ", diff.days);

'''
모듈을 하나 생성하여
짝수인지 홀수인지 판단하는 프로그램을 작성하세요.
'''

from usemod import odd_even

i = int(input("숫자 입력 >> "));
usemod.odd_even(i);