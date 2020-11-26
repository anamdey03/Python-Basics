# Deque is an optimised list to perform insertion and deletion easily
from collections import deque

a = ['e', 'd', 'u', 'r', 'e', 'k', 'a']
d = deque(a)
print(d)

d.append('python')
print(d)

d.appendleft('java')
print(d)

d.pop()
print(d)

d.popleft()
print(d)