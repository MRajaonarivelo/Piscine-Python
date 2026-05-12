import sys


def ft_filter(func, iter):
    """
    returns an iterable object containing every element
    of iter for which func returns true
    """
    try:
        assert {callable(func) or func is None,
                "func must be a callable!"}
        assert {hasattr(iter, '__iter__'),
                "iter must be an iterable object!"}
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit()
    if func is None:
        return [i for i in iter if bool(i)]
    else:
        return [i for i in iter if func(i)]
