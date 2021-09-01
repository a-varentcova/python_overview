test_list = [1, 2, 3, 4, 5]

# LIST METHODS

# list.append(item) adds item to the end of the list,
# changes list in place, doesn't create its copy
print(test_list.append(100))

# # list.insert(index,item) adds item at a certain index,
# changes list in place, doesn't create its copy
print(test_list.insert(3, 100))

# # list.extend(index,item) adds iterable to the end of the list,
# changes list in place, doesn't create its copy
print(test_list.extend([100, 200])
