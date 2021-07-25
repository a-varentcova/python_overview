def main():
    
    first_name = "Arni"     # double quotation
    last_name = 'Smith'     # or single quotation
    
    # or triple quotation for long text:
    long_string = ''' 
        Here is long
        and random text
    '''
    
    # string concatenation:
    full_name = first_name + ' ' + last_name
    print(full_name)
    
    # converting to a string type before concatenation:
    age = 25
    print(full_name + ': ' + str(age))
    print(type(str(age)))
    
    # Escape sequence: any character after \ is treated as a string
    # \t = tab
    # \n = new line
    print("it's a string with special characters")
    print("it's a string with \"special\" characters")
    print("\t it's a string with special characters")
    print("it's a string with special characters\n and here is a new line")

    # formatted strings
    # f-strings (python3):
    print(f"{first_name} {last_name} is {age} years old.")    # no need for explicit type conversion

    # .format() method (python2):
    print("{} {} is {} years old".format(first_name, last_name, last_name))
    print("{1} {0} is {2} years old".format(last_name, first_name, last_name)) 
    print("{first_name} is {age} years old".format(first_name="Arni", age=20))
    

if __name__ == "__main__":
    main()
