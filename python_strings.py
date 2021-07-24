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
    print(full_name + ': ' + str(25))
    print(type(str(25)))
    
    # Escape sequence: any character after \ is treated as a string
    # \t = tab
    # \n = new line
    print("it's a string with special characters")
    print("it's a string with \"special\" characters")
    print("\t it's a string with special characters")
    print("it's a string with special characters\n and here is a new line")


if __name__ == "__main__":
    main()
