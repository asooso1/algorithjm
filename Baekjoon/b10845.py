import sys
s = []
queue_pointer = -1
def push(item):
    global queue_pointer
    s.append(item)
    queue_pointer += 1
def pop():
    global queue_pointer
    if queue_pointer > -1:
        queue_pointer -= 1
        print(s[0])
        del s[0]
    else:
        print(-1)
def size():
    return len(s)
def empty():
    if queue_pointer > -1:
        return 0
    else:
        return 1
def front():
    if queue_pointer > -1:
        return s[0]
    else:
        return -1
def back():
    if queue_pointer > -1:
        return s[queue_pointer]
    else:
        return -1

for case in range(int(input())):
    order = sys.stdin.readline().rstrip()
    if order == 'pop':
        pop()
    elif order == 'front':
        print(front())
    elif order == 'back':
        print(back())
    elif order == 'size':
        print(size())
    elif order == 'empty':
        print(empty())
    else:   # push
        order, items = order.split(' ')
        push(items)