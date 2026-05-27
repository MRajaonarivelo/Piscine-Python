import sys


def ft_filter(func, iter):
    """Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true."""
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
