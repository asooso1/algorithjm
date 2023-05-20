import sys
sys.stdin = open('b1181.txt')

N = int(sys.stdin.readline().rstrip())
words = set()
for i in range(N):
    word = sys.stdin.readline().rstrip()
    words.add(word)

sorted_words = sorted(list(words), key=lambda x:(len(x), x))
print(*sorted_words, sep="\n")