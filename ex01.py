'''
국어, 영어, 수학 세 과목의 점수를 입력받아
Grade 클래스를 생성하고
총점과 평균을 구하세요
'''

class Grade:

    def __init__(self, k, e, m):
        self.k = k
        self.e = e
        self.m = m

    def score(self):
        return self.k + self.e + self.m

    def i(self):
        return (self.k + self.e + self.m) // 3


k = int(input("국어 점수 >> "))
e = int(input("영어 점수 >> "))
m = int(input("수학 점수 >> "))

grade = Grade(k, e, m)

print("총점 : ", grade.score());
print("평균 : ", grade.i());