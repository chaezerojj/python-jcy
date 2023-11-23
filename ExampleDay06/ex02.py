'''
* 다양한 조건을 판단하는 조건문
if 조건A:
    A 조건이 참일 때 수행
elif 조건B:
     B 조건이 참일 때 수행
else:
    모든 조건이 거짓일 때 수행 (default)
'''
choice = int(input("메뉴 선택 >> "))
if choice == 1:
    print("콜라")
elif choice == 2:
    print("사이다")
elif choice == 3:
    print("환타")
elif choice == 4:
    print("커피");
else:
    print("메뉴를 잘못 선택하셨습니다.")