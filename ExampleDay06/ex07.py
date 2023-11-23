'''
학점 계산기
'''
score = int(input("점수를 입력하세요. >> "))
if score >= 90:
    if score >= 95:
        print("A+입니다.")
    else:
        print("A 입니다.")
elif score >= 80:
    if score >= 85:
        print("B+입니다.")
    else:
        print("B 입니다.")
elif score >= 70:
    if score >= 75:
        print("C+입니다.")
    else:
        print("C 입니다.")
elif score >= 60:
    if score >= 65:
        print("D+입니다.")
    else:
        print("D 입니다.")
else:
    print("F 입니다.")