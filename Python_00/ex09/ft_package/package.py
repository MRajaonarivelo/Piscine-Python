def count_in_list(l, a):
    """
    returns the number of occurences of a in l.
    """
    return (len([v for v in l if v == a]))