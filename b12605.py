import sys
for tc in range(1, int(input())+1):
    string = list(sys.stdin.readline().rstrip().split(' '))
    answer = ''
    for i in range(len(string)):
        answer += string.pop() + ' '
    print('Case #{}: {}'.format(tc,answer[:]))
