'''
해당 월을 입력받아 계절 이름이 출력되는 프로그램을 작성

12, 1, 2 : 겨울
3, 4, 5 : 봄
6, 7, 8 : 여름
9, 10, 11 : 가을
'''

weather = int(input("월 입력 >>"))
if weather == 12 or weather == 1 or weather == 2:
    print("겨울")
elif weather == 3 or weather == 4 or weather == 5:
    print("봄")
elif weather == 6 or weather == 7 or weather == 8:
    print("여름")
elif weather == 9 or weather == 10 or weather == 11:
    print("겨울")