# 럭키 스트레이트

n = input()
s = int(len(n) / 2)
first = n[0:s]
second = n[s:]

f_count = 0
s_count = 0

for i in range(s):
    f_count += int(first[i])
    s_count += int(second[i])

if f_count == s_count:
    print('LUCKY')
else:
    print('READY')

