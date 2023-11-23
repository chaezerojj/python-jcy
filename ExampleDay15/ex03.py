class Oper:
    
    def __init__(self):
        self.res = 0;
        
    def plus(self, num):
        self.res = self.res + num;
        return self.res;

# 인스턴스는 클래스 밖에서 생성
student1 = Oper();
student2 = Oper();

print(student1.plus(10));
print(student1.plus(20));

print(student2.plus(30));
print(student2.plus(40));