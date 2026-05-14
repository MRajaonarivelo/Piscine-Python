import sys


NESTED_MORSE = {' ': "\\ ", 'A': '.- ', 'B': '-... ',
                'C': '-.-. ', 'D': '-.. ', 'E': '. ',
                'F': '..-. ', 'G': '--. ', 'H': '.... ',
                'I': '.. ', 'J': '.--- ', 'K': '-.- ',
                'L': '.-.. ', 'M': '-- ', 'N': '-. ',
                'O': '--- ', 'P': '.--. ', 'Q': '--.- ',
                'R': '.-. ', 'S': '... ', 'T': '- ',
                'U': '..- ', 'V': '...- ', 'W': '.-- ',
                'X': '-..- ', 'Y': '-.-- ', 'Z': '--.. ',
                '1': '.---- ', '2': '..--- ', '3': '...-- ',
                '4': '....- ', '5': '..... ', '6': '-.... ',
                '7': '--... ', '8': '---.. ', '9': '----. ',
                '0': '----- '}


def main():
    """
    Takes in arguement an alphanumeric string, translates and
    outputs it into morse code on the standard output.
    """
    args = sys.argv
    try:
        assert len(args) == 2
        assert isinstance(args[1], str)
        for c in args[1]:
            assert c.isalnum() or c.isspace()
    except AssertionError:
        print("AssertionError: the arguments are bad")
        sys.exit()
    coded = [NESTED_MORSE.get(c.capitalize()) for c in args[1]]
    print(str.join('', coded))


if __name__ == "__main__":
    main()
