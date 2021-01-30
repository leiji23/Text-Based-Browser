from collections import deque

result = 'OK'
my_input = list(input())
my_stack = deque()
for i in my_input:
    if i == "(":
        my_stack.append(i)
    elif i == ")":
        if len(my_stack) != 0:
            my_stack.pop()
        else:
            result = 'ERROR'

if len(my_stack) != 0:
    print('ERROR')
else:
    print(result)
