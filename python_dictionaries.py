# dictionary: unodered {key: value} pairs

# keys - immutable objects
# values - anything


# ways to create a dictionary:
dict_1 = {
          'k1': 1,
          'k2': ['a', 'b', 'c'],
          'k3': True,
         }

dict_2 = dict(k1 = 1, k2 = 2)

# keys must be immutable, but usually it's a descriptive string:
dict_3 = {
          1: 1,
          True: ['a', 'b', 'c'],
          (1,2): True,
         }


# accessing values via keys:
print(dict_1['k1'])
print(dict_1['k2'])
print(dict_1['k3'])

print(dict_2['k1'])
print(dict_2['k2'])

print(dict_3[1])
print(dict_3[True])
print(dict_3[(1,2)])


# dict.get(key) method allows to avoid KeyError:
user = {'user': 'Alex', 'id': 123}
print(dict_1.get('age'))       # returns None
print(dict_1.get('age', 20))   # add default value in case key doesn't exist


# another way to check if a key is in the dict:
user = {'user': 'Alex', 'id': 123}
print('age' in user)


# methods for accessing only keys, values or items:
print(user.keys())
print(user.values())
print(user.items())


# dict.clear() clears the dict in place:
print(user.clean())      # returns None
print(user)              # returns {}


# dict.copy() creates a copy:
user = {'user': 'Alex', 'id': 123}
user_new = user.copy()
user.clear()
print(user)       # empty
print(user_new)   # not empty


# dict.pop(key) returns the corresponding value and remove the entire item from the list:
user = {'user': 'Alex','id': 123}
print(user.pop('id'))
print(user)


# dict.update({new_key: value}) adds an item to the dict:
user = {'user': 'Alex', 'id': 123}
user.update({'age': 30})
print(user)
