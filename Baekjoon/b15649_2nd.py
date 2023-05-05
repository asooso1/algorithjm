import sys
sys.stdin = open('b15469.txt', 'r')

N, M = map(int, input().split())

def search(sequence, K):
    if K == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, N + 1):
        if i not in sequence:
            sequence.append(i)
            search(sequence, K + 1)
            sequence.pop()
        
    
search([], 0)