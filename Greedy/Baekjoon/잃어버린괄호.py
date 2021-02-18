# 잃어버린괄호

n = input().split('-')

num=0
for i, e in enumerate(n):
    if i == 0:
        if '+' in e:             # 처음으로 나오는 부호가 '-'가 아닐경우
            array = e.split('+')
            for j in array:
                num += int(j)
        else:
            num = int(n[0])
    else:
        temp_num = 0
        array = e.split('+')
        for j in array:
            temp_num += int(j)
        num -= temp_num  
print(num)
