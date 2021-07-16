from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from collections import namedtuple
from collections import deque

# collections module supplies alternatives to built-in list, dict, set and tuple
# providing additional methods and functionality.


# defaultdict
# defaultdict allows easily to handle missing keys:
# when one tries to access a missing key, defaultdict automatically generates a default value for it.

name_list = ["John", "Max", "James", "Peter", "Robert", "John", "John", "James"]

# defaultdict takes a factory function as an argument which defines a default value.
# Passing class int will generate 0 as the default value:
name_counter = defaultdict(int)

for name in name_list:
    name_counter[name] += 1

print(name_counter)

# Also lambda functions can be used to change the default value.
# For instance, to have 10 as default:
name_counter = defaultdict(lambda: 10)

for name in name_list:
    name_counter[name] += 1

print(name_counter)


# Counter
# Class Counter from collections is a dictionary subclass with special methods to count objects.
team_1 = ["Joe", "John", "Max", "James", "Peter", "Robert", "John", "John", "James"]
team_2 = ["Tom", "Alex", "John", "Max", "James", "Thomas", "Peter", "Robert", "John", "Alex"]

dict_team_1 = Counter(team_1)
dict_team_2 = Counter(team_2)

# accessing number of players with a certain name:
print(dict_team_1["James"])
print(dict_team_1["Max"])

# counting total number:
print(f"{sum(dict_team_1.values())} players in team_1")
print(f"{sum(dict_team_2.values())} players in team_2")

# combining two teams together:
dict_team_1.update(team_2)

print(dict_team_1)
print(f"{sum(dict_team_1.values())} players in updated team_1")

# finding N most common names (which is the largest values in the dict):
print(dict_team_1.most_common(3))
print(dict_team_1.most_common())

# subtracting dictionaries:
dict_team_1.subtract(team_2)

print(f"again {sum(dict_team_1.values())} players in team_1")
print(dict_team_1.most_common(3))
print(dict_team_1.most_common())

# finding intersection of two teams:
print(dict_team_1 & dict_team_2)


# OrderedDict
# An instance of the OrderedDict keeps track of the order in which items were inserted.
# Namely, it remembers the position of the last inserted key. If it overwrites an existing key
# its position goes to the end.

od_1 = OrderedDict({"a": 1, "b": 2, "c": 3})
od_2 = OrderedDict({"a": 1, "b": 2, "c": 3})
od_3 = OrderedDict({"c": 3, "b": 2, "a": 1})
od_4 = {"c": 3, "b": 2, "a": 1}

# order-sensitive comparison:
print("od_1 and od_2 are equal:", test_od_1==test_od_2)
print("od_1 and od_3 are equal:", test_od_1==test_od_3)

# comparison to an ordinary is order-insensitive:
print("od_1 and od_4 are equal:", test_od_1==test_od_4)


# namedtuple
# Tuple subclass: instantiates a tuple-like object which have fields accessible by name
# and which is indexable and iterable as built-in tuple.

Point = namedtuple('Point', ['x', 'y'])
Point = namedtuple('Point', 'x y'])

p = Point(x=1, y=2)    # instantiating with keywords arguments
p = Point(1, 2)        # or instantiating with positional arguments

print(p._fields)       # view the field names

print(p)               # readable __repr__

print(p.x, p.y)        # accessing by name
print(p[0], p[1])      # accessing by indeces

x, y = p.x, p.y        # unpacking like a regular tuple
print(x, y)

# _replace method returns a new instance with new provided values:
p_new = p._replace(y=3)
print(p)
print(p_new)


# deque
# List-like container with fast appends and pops on either end. 
# Memory efficient operations on each end.

d = deque('abcdefghijk')

for element in d:
    print(element, end=",")

d.pop()             # return and remove the rightmost item
d.popleft()         # return and remove the leftmost item

d.append(1)         # add a new item to the right
d.appendleft(2)     # add a new item to the left

# rotate method has default argument n=1, negative numbers will rotate to the left, 
# positive to the right:
print(d)
d.rotate(4)         # right rotation by 4 steps
print(d)
