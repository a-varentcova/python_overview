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


if __name__ == "__main__":
    main()
