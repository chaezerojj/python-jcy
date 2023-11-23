'''
중첩 while문
while 조건식:
      while 조건식:
'''

i = 2;
while i <= 9:
    j = 1;
    while j <= 9:
        print("{} * {} = {}".format(i,j,(i*j)))
        j = j + 1;
    i = i + 1;