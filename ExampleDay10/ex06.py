'''
zip()함수
- 전달된 여러개의 반복가능객체의 각 요소를 튜플로 묶어서 반환
- 전달된 반복가능객체들의 길이가 서로 다르면 길이가 짧은 반복가능객체를 기준으로 동작
'''

names = ['james','emily','amanda']
score = [60,70,80]
for student in zip(names,score):
    print(student)