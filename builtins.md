# Pythom built-ins
* Data types
  * [Tuples](#tuples)
  * [Named tuples](#named-tuples)
  * [List](#list)
  * [Set](#set)
  * [Dict](#dict)
  * [Counter](#counter)
  * [Defaultdict](#defaultdict)
* [Comprehension](#comprehension-return-listsetdict)
* [Slice](#slice-operator)

## Data types

### Tuples

* immutable (can not be changed)
```python
t = ("a", 'b', 'c')
```

### Named Tuples

* like struct in c
```python
from collections import namedtuple
Person = namedtuple('Person', ['first', 'last', 'age'])  # define type Person
i = Person('Peter', 'Klimo', 33)
i.first = 'Peter'
```

### List

* mutable, like array in c, preserve order
```python
l = [0, 1, 2]
l.append(1)
l.sort()
```

### Set

* each item is representd only once, odred is not preserve
* easy way of sort and uniq list: set(list)
```python
s = {0, 1, 2, 2, 3, 1}
```

### Dict
* lookup tables, one-to-one relations
```python
d = {"8.8.8.8": "google dns", "95.105.150.2": "home address"}
```

### Counter
* dictionary subclass - for counting objects
* input is iterable object, outpus is dictionary with counts
```python
from collections import Counter
c = Counter(iterable)
Counter('acbddcba')  # count letters
c = Counter("word after word".split(' '))  # count words
c.most_common(10)
c.substract(iterable)
```

### Defaultdict
* dict subclass - one-to-many relations
* as an argument is factory used as type for values
```python
from collections import defaultdict
d = defaultdict(list)  # for each key is associated list
d['k1'].append(42)
d['k1'].append(10)
d['k2'].append(17)
defaultdict(<type 'list'>, {'k2': [17], 'k1': [42, 10]})
```

## Comprehension: return list/set/dict
* list: [expression for x in iterable if condition]
* set : {expression for x in iterable if condition}
* dict: {key:val for key, val in iterable if condition}

* generators: (key:val for key, val in iterable if condition) - not stored in memory, but dynamically computed

## Slice operator
`l[a:b:c]`
* a - lower bound
  * if missing (or None) is 0
  * if negative - then lower bound is `len(l) + a`
* b - upper bound
  * if missing (or None) is `len(l)`
  * if negative - then upper bound is `len(l) + a`
* c - step (default 1)
  * if negative - reverse list and set `step = -c` (positive value)
```python
l = [0, 1, 2, 3, 4, 5]
l[::-1]  # [5, 4, 3, 2, 1, 0]  # reverse of list
l[-3:]  # [3, 4, 5]  # last 3 items
l[:-2]  # [0, 1, 2, 3]  # slice last 2 items
```

