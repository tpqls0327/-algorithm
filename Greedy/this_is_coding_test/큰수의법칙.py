# 큰 수의 법칙

# 방법1
n,m,k = map(int, input().split())
num = list(map(int, input().split()))

num.sort(reverse=True)
max_num = num[0]
max2_num = num[1]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += max_num
        m -= 1
        print(result)
    print('next')
    if m == 0:
        break
    result += max2_num
    m -= 1
print(result)


# 방법2
n,m,k = map(int, input().split())
num = list(map(int, input().split()))

num.sort(reverse=True)
max_num = num[0]
max2_num = num[1]

result = 0

count = int((m / (k+1))*k) + (m % (k+1))
count_2 = int(m / (k+1))
result += ((max_num * count) + (max2_num *count_2))
print(result)
