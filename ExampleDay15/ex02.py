'''
2명의 학생이 있는데, 각각 0부터 임의의 수를 더해나간 결과(함수버전)
'''
student1 = 0;
student2 = 0;

def plus1(num):
    global student1; # global: 전역변수
    student1 = student1 + num;
    return student1;

def plus2(num):
    global student2;
    student2 = student2 + num;
    return student2;

print(plus1(10));
print(plus1(20));

print(plus2(30));
print(plus2(40));