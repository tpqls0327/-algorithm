# 곱하기혹은더하기

s = input()
num = 0

for index, v in enumerate(s):
    if index == 0:
        num += int(v)
    else:
        if num <=0:
            num += int(v)
        elif v == '0' or v =='1':
            num += int(v)
        else:
            num *= int(v)
print(num)
