'''
리스트에 저장된 값들 중 짝수들의 합을 구하세요
'''

arr = [1,2,3,4,5,6,7,8,9,10];
i = 0;
sum = 0;

while i < len(arr) :
    if arr[i] % 2 == 0: # 인덱스에 짝수
        sum = sum + arr[i];
    i = i + 1;
print("arr 리스트의 짝수들의 합 : ", sum);
