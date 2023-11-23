'''
문자열 슬라이싱
- 문자열의 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출할 때 사용
- 추출하고자 하는 단어나 문장의 시작 인덱스와 종료 인덱스를 통해 그 사이의 문자열을 추출한다

형식)
문자열[시작인덱스 : 끝인덱스 -1 : 오프셋]
'''

slice_a = "Hi Python";
print(slice_a[0:2]);
print(slice_a[3:9]);


a = "Life is too short, You need Python"
print(a[3:10]);
print(a[0:4])
print(a[5:8])

'''
오프셋 : 오프셋을 설정할 경우 해당 숫자만큼 건너뛰면서 출력
        오프셋은 생략 가능
'''
a1 = "Hello";
print(a1[0:5:2])