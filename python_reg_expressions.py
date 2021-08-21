import re

test_string = "Here is some text for testing. Test is right here!"

a = re.search("is", test_string)
print(a.span())
print(a.group())

pattern = re.compile("is")
a = pattern.search(test_string))
print(a.group())

a = pattern.findall(test_string)
print(a)

a = pattern.fullmatch(test_string)
a = pattern.match(test_string)
