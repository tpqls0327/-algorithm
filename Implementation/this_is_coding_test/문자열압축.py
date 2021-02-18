# 문자열 압축

s = list(input().split())

def divide(list, n):
    return (list[i:i+n] for i in range(0, len(list), n))

result = []

for i in range(int(len(s))/2):
    array = divide(s,i)
    m = array[0]
    count = 0
    
    for j in range(1,len(array)):
        if m == array[j]:
            count += 1
        else:
            m = array[j]
            result[i].append(str(count) + str(m))

print(min(result))
        
