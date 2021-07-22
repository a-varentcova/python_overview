def main():

    test_list_1 = [0, 1, 2, 3, 4, 5]
    test_list_2 = [0, False, None, {}]
    test_list_3 = [1, 2, 3, 4, 5, 6]
    
    # any(iterable), returns True if at least one item evaluates to True
    print(any(test_list_1))     # True, since all items except for 0 evaluate to True
    print(any(test_list_2))     # False, since all items evaluate to False
    
    # all(iterable), returns True if all items evaluates to True
    print(all(test_list_1))     # False, since 0 evaluates to False
    print(all(test_list_3))     # True, since all items evaluate to True
    
    # min(iterable), return the smallest item in an iterable
    # max(iterable), return the largest item in an iterable
    print(min(test_list_1))
    print(max(test_list_1))
    
    # sum(iterable), sums all the items in an iterable
    print(sum(test_list_1))


if __name__ == "__main__":
    main()
