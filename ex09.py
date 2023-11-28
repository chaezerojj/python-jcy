# 다중상속
class Person:
    def greeting(self):
        print("안녕하세요")

class University:
    def manage_credit(self):
        print("학점관리");

class Student(Person, University):
    def study(self):
        print("공부하기")

student = Student()
student.greeting()
student.manage_credit()
student.study()