import sys
sys.stdin = open('b10988.txt')

word = list(input())

if word == list(reversed(word)):
    print(1)
else:
    print(0)