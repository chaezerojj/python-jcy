class Person:
    def __init__(self, name, age, gender):
        self.name = name;
        self.age = age;
        self.gender = gender;

    def info(self):
        print("제 이름은 " + self.name + "이고 나이는 " + self.age + "살 입니다.");

class Employee(Person):
    def __init__(self, name, age, gender, salary, hiredate):
        super().__init__(name, age, gender);
        self.salary = salary;
        self.hiredate = hiredate;

    def doWork(self):
        print("열심히 일을 합니다.")

    def aboutMe(self):
        super().info();
        print("제 급여는 " + self.salary + "원 이고", end='  ')
        print("입사일은 " + self.hiredate + "입니다.")

employee = Employee("윤준형", "28", "남자", "30000", "20230411")

employee.doWork()
employee.aboutMe()