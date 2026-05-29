import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Takes two lists of int or float values and returns a list of
    BMI values. The lists must be of the same length and not empty.
    """
    try:
        assert height != [] and weight != [], "lists cannot be empty"
        assert len(height) == len(weight), "lists are not of the same size"
        assert (all(isinstance(x, (int, float)) for x in height)
                and all(isinstance(x, (int, float)) for x in weight)), \
            "lists must be all int or float values"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit()
    arr_h = np.array(height)
    arr_w = np.array(weight)
    return (arr_w / (arr_h**2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Takes a list of int or float bmi values and an int limit
    and returns a list of bool values(True if the bmi is
    above the limit). The list must not be empty.
    """
    try:
        assert bmi != [], "list cannot be empty"
        assert {isinstance(bmi, (int, float)),
                "list elements must be integer or float"}
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit()
    return [b > limit for b in bmi]
