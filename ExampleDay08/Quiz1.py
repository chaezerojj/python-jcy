'''
기존 list에서 새로운 리스트에 짝수만 넣으시오.
append()메소드 사용!
'''
arr = [1,2,3,3,7,9,12,100,4,12,7];
arr2 = [];

i = 0;
while i < len(arr): # arr 리스트 길이만큼 루프회전
    # 루프를 돌며 각 인덱스에 접근하여 2로 나누었을때
    # '짝수'라면,
    if arr[i] % 2 == 0:
        # 빈리스트arr2에 arr 리스트에 저장되어있는
        # 숫자 중 짝수만 arr1 리스트에 추가됨
        arr2.append(arr[i]);
    i = i + 1; # 증감식
print(arr2);

# while arr:
#     if 2 in arr:
#         arr2.append(2);
#     if 12 in arr:
#         arr2.append(12);
#     if 100 in arr:
#         arr2.append(100);
#     if 4 in arr:
#         arr2.append(4);
#     if 12 in arr:
#         arr2.append(12);
#     if 3 in arr:
#         break;
# print(arr2);

