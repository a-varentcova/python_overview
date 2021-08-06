# list comprehentions:

list_1 = [i for i in range(10)]
list_2 = [i for i in range(10) if i > 5]
list_3 = [i for i in 'abcd']
list_4 = [i for i in range(100) if i % 2 == 0]    #pick up even numbers

print(list_1)
print(list_2)
print(list_3)
print(list_4)


# set comprehensions:

set_1 = {i for i in 'apple'}
set_2 = {i for i in [1,1,1,2,3,4,5,5,5]}

print(set_1)
print(set_2)


# dictionary comprehensions:

dict_0 = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}

dict_1 = {k: v*10 for k, v in dict_0.items()}
dict_2 = {v: v*10 for k, v in dict_0.items()}
dict_3 = {k: v*10 for k, v in dict_0.items() if v > 2}
dict_4 = {i: i**2 for i in range(5)}

print(dict_1)
print(dict_2)
print(dict_3)
print(dict_4)