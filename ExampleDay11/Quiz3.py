'''
자신의 이름 전체를 영어로 입력받고
'성'과 '이름'을 바꾸는 함수를 만들어 해당 함수를 통해 바뀐 영문 이름을 출력하세요.
- split() join()메소드 활용!!

입력 예)
Yun JunHyeong

출력 예)
JunHyeong Yun
'''

def listToString(name):
    result = name.split();
    temp = result[0]
    result[0] = result[1]
    result[1] = temp;
    # join()함수는 매개변수로 들어온 리스트에 있는 요소 하나하나르 합쳐
    # 하나의 문자열로 바꿔 반환함
    str_name = ' '.join(s for s in result)
    return str_name

name = input("영문 이름을 입력하세요 >> ");
print(listToString(name))