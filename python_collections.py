from collections import defaultdict

# defaultdict allows easily to handle missing keys:
# when one tries to access a missing key, defaultdict automatically 
# creates this key and generates a default value for it.

name_list = ["John", "Max", "James", "Peter", "Robert", "John", "John", "James"]

name_counter = defaultdict(int)
