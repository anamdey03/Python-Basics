# DefaultDict is a dictionary subclass which calls a factory function to supply missing values

from collections import defaultdict

d = defaultdict(int)

d[1] = 'Java'
d[2] = 'Python'

print(d)

print(d[3])  # Doesn't throw KeyError which we generally get in case of Dictionary
