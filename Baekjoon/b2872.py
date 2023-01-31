import sys

N = int(input())
book_list = [int(sys.stdin.readline())]
max_num = book_list[0]
cnt = 0

for i in range(1, N):
    book_list.append(int(sys.stdin.readline()))

for i in range(1, N):
    if max_num < book_list[i]:
        if max_num+1 != book_list[i]:
            cnt += 1
        max_num = book_list[i]
    else :
        cnt += 1
print(cnt)

# 첫번째 인덱스에서부터 오름차순으로 있는지 확인하면서 만약 아니라면 pop 한다는 가정 (이 문제에서는 카운트만)