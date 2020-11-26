# OrderedDict is a dictionary subclass which remembers the order in which the entries were done

from collections import OrderedDict

d = OrderedDict()

d[0] = 'a'
d[1] = 'n'
d[2] = 'a'
d[3] = 'm'
d[4] = 'i'
d[5] = 't'
d[6] = 'r'
d[7] = 'a'

print(d)

print(d.keys())

d[1] = 'a'

print(d)
