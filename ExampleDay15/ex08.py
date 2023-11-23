class Person:

    def __init__(self, name, age):
        self.name = name;
        self.age = age;

    def info(self):
        print("제 이름은 {}이고, {}살 입니다."
              .format(self.name, self.age));

man1 = Person("홍길동", 20);
man2 = Person("김철", 25)

man1.info()
man2.info()