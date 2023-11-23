i = 0;
while i < 100: # i가 100보다 작을때까지 반복
    i = i + 1; # i를 1씩 증가시킨다
    if i % 2 == 0: # i값이 짝수일때
        continue; # 아래 코드를 실행하지 않고 건너뛴다!
    print(i);

'''
continue
- continue문은 반복문(for, while)에서 아래 코드를 실행시키지 않고 
  다음 반복 구문으로 넘어가도록 하는 제어자! 
'''