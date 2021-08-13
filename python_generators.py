# Generators are more memory efficient 
# (they provide item after item not holding all of them at once in the memory)

# range is a special generator-like object:
print(range(10))

# converting range to a list:
print(list(range(10)))

# general way to construct generator:
def generator_function(N):
    for i in range(N):
        yield i**2

for i in generator_function(10):
    print(i)

# how next works in generators:
# yield pauses the functions, and next invokes it again by 1 iteration
g = generator_function(10)
print(next(g))
print(next(g))
print(next(g))
