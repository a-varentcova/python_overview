from collections import defaultdict
from collections import Counter

# defaultdict allows easily to handle missing keys: when one tries to access a missing key,
# defaultdict automatically generates a default value for it.

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


names = Counter(name_list)
