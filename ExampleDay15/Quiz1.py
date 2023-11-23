'''
책 제목과 책 저자의 정보를 담고 있는 book 클래스를 생성하세요.
1. 책 제목과 책 저자 정보를 출력하는 print_info() 메소드를 구현하세요.
2. 다음과 같은 방법으로 book1, book2 인스턴스를 생성하세요.

실행 예)
책 제목: 파이썬
책 저자: 민경태
책 제목: 어린왕자
책 저자 : 생택쥐페리
'''

class book:
    title = ""
    author = ""

    def info(self, title, author):
        self.title = title
        self.author = author
        print("책 제목 : ", self.title)
        print("책 저자 : ", self.author)
book1 = book();
book2 = book();

book1.info("파이썬", "민경태")
book2.info("어린왕자", "생택쥐페리")

