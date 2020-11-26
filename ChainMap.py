# Chainmap is a dictionary like class for creating a single view of multiple mappings

from collections import ChainMap

a = {1: 'Java', 2: 'Python'}
b = {3: 'AI', 4: 'ML'}

c = ChainMap(a, b)

print(c)

for index in c:
    print(c[index])
