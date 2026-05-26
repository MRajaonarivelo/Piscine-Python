def count_in_list(lst, a):
    """
    returns the number of occurences of a in lst.
    """
    return (len([v for v in lst if v == a]))


def rev_list(lst):
    """returns a reversed built from lst"""
    return lst[::-1]


def most_in_list(lst):
    """
    returns the most frequent element from lst.
    if a tie occurs, the returned element is arbitrary.
    returns None if lst is empty.
    """
    if lst == []:
        return None
    uniques = set(lst)
    most = {u: count_in_list(lst, u) for u in uniques}
    return max(most, key=lambda x: most[x])
