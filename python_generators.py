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
g = generator_function(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# exceeding number of items gives StopIteration error:
# print(next(g))


# creating custom for-loop:

def new_for_loop(iterable):
    # making a generator from any kind of iterable:
    generator = iter(iterable)
    while True:
        try:
            print(next(generator))
        except StopIteration:
            break

g = generator_function(5)
new_for_loop(g)

g = [1,2,3,4,5]
new_for_loop(g)


# creating custom range object:

class MyRange():
    
    def __init__(self, start, stop):
        self.current = start
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.stop:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


new_range = MyRange(0,10)

for i in new_range:
    print(i)
