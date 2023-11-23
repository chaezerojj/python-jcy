'''
while문을 활용하여 list에 저장되어 있는 총 합계를 구하는 프로그램
'''

arr = [1,2,3,4,5,6,7,8,9,10];
sum = 0;
i = 0;
while i < len(arr):
    # 루프를 회전하며 arr 리스트의
    # 각 인덱스 요소에 접근하여 누적 합계를 구한다
    print(i);
    sum = sum + arr[i]
    i = i + 1;
print("arr list의 총 합 : ", sum);