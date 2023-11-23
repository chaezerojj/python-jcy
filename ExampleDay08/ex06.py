'''
for문의 기본구조
for 변수 in range(초기식, 조건식 -1, 증감식):
    수행할 문장
'''
for i in range(1, 11, 1): # 10까지 출력하려면 조건식에 값을 11 줘야 함
    print(i);

print("------------------")
# 증감식을 생략하면 자동으로 1씩 증가!!
for i in range(10): # 초기식을 생략하면 0부터 시작!!
    print(i);

print("------------------")

# 1~ 10까지 2씩 증가하면서 출력
for i in range(1,11,2):
    print(i);
print("------------------")
for i in range(1,11):
    print(i)