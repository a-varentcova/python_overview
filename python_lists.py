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
