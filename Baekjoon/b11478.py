import sys
sys.stdin = open('b11478.txt')

S = list(sys.stdin.readline().rstrip())

set_S = set()
for i in range(len(S)):
    for j in range(len(S) + 1):
        if S[i:j]:
            set_S.add("".join(S[i:j]))
print(len(set_S))
    
# print(set_S)