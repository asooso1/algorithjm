import sys
sys.stdin = open('b1269.txt')

a, b = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))


# # set => 성공
# set_A = set(A)
# set_B = set(B)
# result = (set_A - set_B) | (set_B - set_A)
# print(len(result))

# dict => 성공
dict_A = {}
dict_B = {}
for i in range(a):
    dict_A[A[i]] = True
for j in range(b):
    dict_B[B[j]] = True

cnt = 0
for k in A:
    if dict_B.get(k) != True:
        cnt += 1
for k in B:
    if dict_A.get(k) != True:
        cnt += 1
    
print(cnt)