# ATM

n = int(input())
person = list(map(int, input().split()))

person.sort()

p = 0
result = 0
for i in person:
    p+=i
    result += p
print(result)
    
