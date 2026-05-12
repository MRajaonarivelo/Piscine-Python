import sys
from ft_filter import ft_filter


def main():
    """
    Takes two arguments, a string S and an interger N.
    S musn't have any invisible or special characters
    returns a list containing every word from S longer
    than N
    """
    args = sys.argv
    try:
        assert len(args) == 3
        assert isinstance(args[1], str)
        assert args[2].isdigit()
        for c in args[1]:
            assert c.isalnum() or c.isspace()
    except AssertionError:
        print("AssertionError: the arguments are bad")
        sys.exit()

    s = args[1]
    n = int(args[2])
    words = s.split(" ")
    words = [w for w in words if w != ""]
    print(ft_filter(lambda x: len(x) > n, words))


if __name__ == '__main__':
    main()
