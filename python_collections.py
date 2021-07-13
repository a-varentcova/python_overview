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
