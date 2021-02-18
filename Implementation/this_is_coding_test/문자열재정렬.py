# 문자열 재정렬

s = input()

alpha_list = []
num_list = []

for i in s:
    if i.isalpha():
        alpha_list.append(i)
    else:
        num_list.append(i)
alpha_list.sort()
num_list.sort()
print(''.join(alpha_list + num_list))
