DATATYPES

tuples:
imutable (can not be changed)
t = ("a", 'b', 'c')
access via index e.g. t[0] # t[0] = 'a'
or decomposition x, y, z = t  # x = 'a'

named tuples:
like struct in c
from collections import namedtuple
Person = namedtuple('Person', ['first', 'last', 'age'])  # define type Person
i = Person('Peter', 'Klimo', 33)
i.first = 'Peter'

list:
mutable, like array in c, preserve order
l = [0, 1, 2]
methods: sort, append, []

set:
s = {0, 1, 2, 2, 3, 1}
each item is representd only once, odred is not preserve
easy way of sort and uniq list: set(list)

dict:
lookup tables, one-to-one relations
d = {"8.8.8.8": "google dns", "95.105.150.2": "home address"}

counter:
dictionary subclass - for counting objects
from collections import Counter
c = Counter(iterable)  # return dictionary, where keys() = iterable and values are numbers (how many times value is in iterable)
count letters:
Counter('acbddcba')  # Counter({'a': 2, 'c': 2, 'b': 2, 'd': 2})
count words:
c = Counter("word after word".split(' '))  # Counter({'word': 2, 'after': 1})
methods: most_common(10), substract(iterable)

defaultdict:
dict subclass - one-to-many relations
from collections import defaultdict
as an argument is factory used as type for values
d = defaultdict(list)  # for each key is associated list
d['k1'].append(42)
d['k1'].append(10)
d['k2'].append(17)
defaultdict(<type 'list'>, {'k2': [17], 'k1': [42, 10]})

COMPREHENSION: return list/set/dict
list: [expression for x in iterable if condition]
set : {expression for x in iterable if condition}
dict: {key:val for key, val in iterable if condition}

generators: (key:val for key, val in iterable if condition) - not stored in memory, but dynamically computed

SLICE operator:
l = [0, 1, 2, 3, 4, 5]
l[a:b:c]
a - lower bound
    if missing (or None) is 0
    if negative - then lower bound id len(l)+a
b - upper bound
    if missing (or None) is len(l)
    if negative - then upper bound is len(l)+a
c - step (default 1)
    if negative - reverse list and set step = -c (positive value)

reverse of list: l[::-1]  # [5, 4, 3, 2, 1, 0]
last 3 items: l[-3:]  # [3, 4, 5]
slice last 2 items: l[:-2]  # [0, 1, 2, 3]
