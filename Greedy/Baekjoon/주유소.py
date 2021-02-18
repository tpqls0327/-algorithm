# 주유소

n = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))

result = p[0]*d[0]
temp_p = p[0]
for i in range(1, len(d)):
    if temp_p <= p[i]:
        result+=temp_p*d[i]
    else:
        temp_p = p[i]
        result += temp_p*d[i]
print(result)
