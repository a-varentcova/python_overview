# LIST METHODS

# list.append(item) adds item to the end of the list,
# changes list in place, doesn't create its copy
test_list = [1, 2, 3, 4, 5]
print(test_list.append(100))


# # list.insert(index,item) adds item at a certain index,
# changes list in place, doesn't create its copy
test_list = [1, 2, 3, 4, 5]
print(test_list.insert(3, 100))


# # list.extend(index,item) adds iterable to the end of the list,
# changes list in place, doesn't create its copy
test_list = [1, 2, 3, 4, 5]
print(test_list.extend([100, 200])


# list.pop(index) removes item at the given index and returns this item
# by default list.pop() removes and returns the last item from the list
test_list = [1, 2, 3, 4, 5]
print(test_list)
print(test_list.pop())
print(test_list.pop(0))
print(test_list)


# list.remove(item) removes first occurence of the given item
# changes list in place
test_list = ['a', 'b', 'c', 'd', 'e']
test_list.remove('a')
print(test_list)


# list.clear() removes everything what is in the list (in place)
test_list = ['a', 'b', 'c', 'd', 'e']
test_list.clear()
print(test_list)


# check if item is in the list (returns True/False)
test_list = ['a', 'b', 'c', 'd', 'e']
print('a' in test_list)

      
# list.index() returns index of the given item,
# doesn't change the initial list
test_list = ['a', 'b', 'c', 'd', 'e']
print(test_list.index('b'))
print(test_list)


# list.count() returns how many times item occurs in the list,
# doesn't change the initial list
test_list = ['a', 'b', 'c', 'd', 'e', 'b']
print(test_list.count('b'))
print(test_list)

 
# list.sort() sorts a list
# changes list in place
test_list = ['a', 'b', 'c', 'd', 'e', 'b']
test_list.sort()
print(test_list)
      

# sorted(list) sorts a list,
# doesn't change the initial list,
# returns a sorted copy
test_list = ['a', 'b', 'c', 'd', 'e', 'b']
print(f"sorted copy: {sorted(test_list)}")
print(f"original list: {test_list}")


# list.reverse() reverses a list without sorting,
# changes list in place
test_list = ['a', 'b', 'c', 'd', 'e', 'b']
print(test_list.reverse())
print(test_list)


# list slicing: creates a new list
test_list = [0, 1, 2, 3, 4, 5]
print(f"copy of the list: {test_list[:]}")


test_list = [0, 1, 2, 3, 4, 5]
print(f"reversed: {test_list[::-1]}")
print(f"original: {test_list}")


# string.join(list) creates a new string with items from the given list
# separated by the string:
test_list = ['here', 'is', 'a', 'new', 'list']
print(f"new string: {' '.join(test_list)}")
print(f"original string: {test_string}")


# list unpacking:
a, b, c = [1, 2, 3]
print(a, b, c)

a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a, b, c, other)

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a, b, c, other, d)
