def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    dict = {}
    difference = len(keys) - len(values)
    print(difference)

    [values.append(None) for n in range(1, difference +1) if difference >= 0]
    [keys.pop() for n in range (1, difference+1) if difference < 0]
    print(values)
    print(keys)

    for i in range(0, len(values)):
        dict[keys[i]] = values[i]
    
    return dict

        

    

        