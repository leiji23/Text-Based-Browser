from collections import deque


def book_lover(act, bk_name):
    if act == 'BUY':
        my_stack.append(bk_name)
    elif act == 'READ':
        my_read_stack.append(my_stack.pop())


action_num = int(input())
my_read_stack = deque()
my_stack = deque()
for i in range(action_num):
    lover_action = input().split(' ', 1)
    action = lover_action[0]
    if len(lover_action) == 2:
        book_name = lover_action[1]
    else:
        book_name = ''
    book_lover(action, book_name)

for i in range(len(my_read_stack)):
    print(my_read_stack.popleft())
