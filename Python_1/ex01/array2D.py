import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        assert isinstance(family, list), "family has to be a list"
        assert isinstance(start, int) and isinstance(end, int), \
            "start and end must be integers"
        assert family, "family must not be empty"
        assert all(isinstance(x, list) for x in family), \
            "family has to be a 2D array"
        assert all(bool(x) for x in family), \
            "nested lists in family must not be empty"
        assert all(len(family[0]) == len(x) for x in family[1:]), \
            "nested lists in family must all be same size"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit()

    print(f"My shape is : {np.array(family).shape}")
    res = family[start:end]
    print(f"my new shape is : {np.array(res).shape}")
    return res
