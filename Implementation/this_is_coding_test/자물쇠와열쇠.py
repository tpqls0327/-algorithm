# 자물쇠와 열쇠

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

len_key = len(key)
len_lock = len(lock)


# 자물쇠의 홈 부분
list_lock0 = []
for i in range(len(lock)):
    for j in range(len(lock)):
        if lock[i][j] == 0:
            array = []
            array.append(i)
            array.append(j)
            list_lock0.append(array)
print(list_lock0)

# key 90도 회전
for i in range(4):
    print(key)
    rotate_key = [[0]*len_key for _ in range(len_key)]
    for k in range(len_key):    # 행
        for j in range(len_key):    # 열
            rotate_key[j][k-1-len_key] = key[k][j]
    print(rotate_key)


# key 가운데로 이동후 상화좌우 n-1만큼 움직이기
