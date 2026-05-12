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
    args = sys.argv
    try:
        assert len(args) == 2
        assert isinstance(args[1], str)
        for c in args[1]:
            assert c.isalnum()
    except AssertionError:
        print("AssertionError: the arguments are bad")

if __name__ == "__main__":
    main()