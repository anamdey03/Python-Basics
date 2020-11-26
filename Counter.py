# Counter is a dictionary subclass for counting hashtable objects
from collections import Counter

a = [1, 2, 1, 3, 2, 2, 3, 1, 4, 5, 1, 3]

count = Counter(a)
print(count)

print(list(count.elements()))

print(count.most_common())

sub = {1: 2, 2: 1, 3: 1}
count.subtract(sub)

print(count.most_common())
