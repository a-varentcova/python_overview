def main():
    
    first_name = "Arni"     # double quotation
    last_name = 'Smith'     # or single quotation
    
    # or triple quotation for long text:
    long_string = ''' 
        Here is long
        and random text
    '''
 
    # Concatenation:
    full_name = first_name + ' ' + last_name
    print(full_name)

    # converting to a string type before concatenation:
    age = 25
    print(full_name + ': ' + str(age))
    print(type(str(age)))


    # Escape sequences:

    # any character after \ is treated as a string
    # \t = tab
    # \n = new line
    print("it's a string with special characters")
    print("it's a string with \"special\" characters")
    print("\t it's a string with special characters")
    print("it's a string with special characters\n and here is a new line")

 
    # Formatted strings:

    # f-strings (python3):
    print(f"{first_name} {last_name} is {age} years old.")    # no need for explicit type conversion

    # .format() method (python2):
    print("{} {} is {} years old".format(first_name, last_name, last_name))
    print("{1} {0} is {2} years old".format(last_name, first_name, last_name)) 
    print("{first_name} is {age} years old".format(first_name="Arni", age=20))


    # Strings are ordered sequences of charachters and immutable: cannot be change once created.
    # Any item can be accessed by index str[i], but not reassigned.
    # Slicing: str[start:stop:step], with default values start=0, stop=len(str), step=1
    # Slicing creates a new string without changing the original.

    test_str_1 = "0123456789"
 
    print("first item: ", test_str[0])
    print("second item: ", test_str[1])
    print("last item: ", test_str[-1])
    print("second item from the end: ", test_str[-2])

    print("two first items: ", test_str[0:2])
    print("two first items: ", test_str[:2])

    print("all items: ", test_str[:])
    print("all items: ", test_str[::])

    print("all items with step 2: ", test_str[::2])    # every second item
    print("all items reversed: ", test_str[::-1])      # reversed string
    print("all items reversed with step 2: ", test_str[::-2])


    # Some string's methods:
 
    test_str_2 = "here is a string!"
 
    print("uppercase: ", test_str_2.upper())
    print("lowercase: ", test_str_2.lower())
    print("capital: ", test_str_2.capitalize())
    print("index where 'e' appears: ", test_str_2.find('e'))
    print("replace '!' with '?': ", test_str_2.replace('!', '?'))    # creates a new string
    
    
if __name__ == "__main__":
    main()
