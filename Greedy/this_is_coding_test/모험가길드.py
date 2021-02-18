# 모험가길드

n = int(input())
m = list(map(int, input().split()))

m.sort(reverse=True)

count = 0
x = m[0]
while True:
    if n <1:
        break
    n -= x
    count +=1
    x = m[x]
print(count)
