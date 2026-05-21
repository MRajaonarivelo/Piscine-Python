def count_in_list(list, a):
    """
    returns the number of occurences of a in list.
    """
    return (len([v for v in list if v == a]))

def rev_list(list):
    """returns a reversed built from list"""
    return list[::-1]
