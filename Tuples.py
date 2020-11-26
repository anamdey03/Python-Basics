# Tuples are Immutable and ordered in nature. Can have duplicate entries present inside it
from collections import namedtuple

coordinates = (4, 5)  # Tuple is similar to List but it is immutable
print(coordinates[0])

try:
    list_of_tuples = [(1, 2), (3, 4), (5, 6)]
    print((list_of_tuples[0][3]))
except IndexError as err:
    print(err)

a = namedtuple('courses', 'name, technology')
# s = a('Data Science', 'Python')
s = a._make(['Artificial Intelligence', 'Python'])
print(s)
