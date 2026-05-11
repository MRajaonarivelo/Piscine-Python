import sys


def assrertExit(e: any):
    """
    Prints assertion error and exits the program
    """
    print(f"AssertionError: {e}")
    sys.exit()


def main():
    args = sys.argv
    text = ""
    try:
        assert len(args) <= 2, "Wrong number of arguments"
    except AssertionError as e:
        assrertExit(e)
    if len(args) == 1 or args[1] == "":
        try:
            text = sys.stdin.readline()
        except KeyboardInterrupt as e:
            print("\nError: Keyboard interruption!")
            sys.exit()
        try:
            assert text != "", "Empty text sent!"
        except AssertionError as e:
            assrertExit(e)
        if "\n" not in text:
            print("")
    else:
        text = args[1]
    print(f"The text contains {len(text)} characters:")
    print(f"{len([c for c in text if c.isupper()])} upper letters")
    print(f"{len([c for c in text if c.islower()])} lower letters")
    print(f"{len([c for c in text if not c.isalnum()
                  and not c.isspace()
                  and c.isprintable()])} punctuation marks")
    print(f"{len([c for c in text if c.isspace()])} spaces")
    print(f"{len([c for c in text if c.isdigit()])} digits")


if __name__ == "__main__":
    main()
