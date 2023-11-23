'''
파이썬 도서 관리 프로그램
1. 도서 등록 (도서 번호, 책 이름 ,책 저자, 출판사)
2. 도서 목록
3. 도서 검색 (제목, 저자, 출판사)
4. 도서 삭제 (해당 도서 번호로 삭제)
5. 프로그램 종료
'''

book_mark = []  # 입력받은 도서 저장 리스트

while True:
    print("========== ★ 도서관리 프로그램 ★ ==========")
    print("1. 도서 등록");
    print("2. 도서 목록");
    print("3. 도서 검색");
    print("4. 도서 삭제");
    print("5. 프로그램 종료");

    choice = int(input("메뉴 선택 >> "));
    if choice == 1:
        book_dict = {};

        book_seq = int(input("도서 번호 >> "));
        book_name = input("책 이름 >> ");
        book_author = input("책 저자 >> ");
        book_publisher = input("출판사 >> ");

        book_dict['seq'] = book_seq;
        book_dict['name'] = book_name;
        book_dict['author'] = book_author;
        book_dict['publisher'] = book_publisher;
        book_mark.append(book_dict);

    elif choice == 2:
        '''
        리스트의 길이만큼 루프를 돌면서 각 인덱스에 저장되어 있는
        딕셔너리 키값에 접근하여 해당 값들을 모두 출력
        '''
        for item in book_mark:
            print("★★★★★★★★★★★★★★★★★★★★★★")
            print("도서번호 : {}".format(item.get('seq')))
            print("책 이름 : {}".format(item.get('name')))
            print("책 저자 : {}".format(item.get('author')))
            print("출판사 : {}".format(item.get('publisher')))
            print("★★★★★★★★★★★★★★★★★★★★★★")
    elif choice == 3:
        '''
        n을 입력하면 도서 제목으로 검색
        a를 입력하면 도서 저자로 검색
        p를 입력하면 도서 출판사로 검색
        '''
        print("n: 제목 | a: 저자 | p: 출판사")
        search_type = input("검색할 타입을 선택해주세요 >> ")

        if search_type == 'n':
            title = input("검색 하고 싶은 책 제목을 입력해주세요 >> ")
            for item in book_mark:
                sec = item.get('name');
                if sec == title:
                    print("★★★★★★★★★★★★★★★★★★★★★★")
                    print("도서번호 : {}".format(item.get('seq')))
                    print("책 이름 : {}".format(item.get('name')))
                    print("책 저자 : {}".format(item.get('author')))
                    print("출판사 : {}".format(item.get('publisher')))
                    print("★★★★★★★★★★★★★★★★★★★★★★")
        elif search_type == 'a':
            author = input("검색 하고 싶은 저자를 입력해주세요 >> ")
            for item in book_mark:
                sec = item.get('author')
                if sec == author:
                    print("★★★★★★★★★★★★★★★★★★★★★★")
                    print("도서번호 : {}".format(item.get('seq')))
                    print("책 이름 : {}".format(item.get('name')))
                    print("책 저자 : {}".format(item.get('author')))
                    print("출판사 : {}".format(item.get('publisher')))
                    print("★★★★★★★★★★★★★★★★★★★★★★")
        elif search_type == 'p':
            publisher = input("검색 하고 싶은 출판사를 입력해주세요 >> ")
            for item in book_mark:
                sec = item.get('publisher')
                if sec == publisher:
                    print("★★★★★★★★★★★★★★★★★★★★★★")
                    print("도서번호 : {}".format(item.get('seq')))
                    print("책 이름 : {}".format(item.get('name')))
                    print("책 저자 : {}".format(item.get('author')))
                    print("출판사 : {}".format(item.get('publisher')))
                    print("★★★★★★★★★★★★★★★★★★★★★★")
    elif choice == 4:
        book_del = int(input("삭제할 도서 번호를 입력해주세요. >>"))
        for item in range(len(book_mark)):
            if book_mark[item]['seq'] == book_del:
                del book_mark[item];
                break;
    elif choice == 5:
        print("프로그램 종료");
        break;