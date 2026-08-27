import pandas as pd


def error_exit(msg: str):
    '''prints an error msg and exits the program'''
    print(f"Error: {msg}")
    exit()


def load(path: str) -> pd.DataFrame:
    '''returns a DataFrame from a path to .csv file'''
    try:
        assert path != "", "empty path name"
        assert path.endswith(".csv"), "bad format"
        res = pd.read_csv(path, index_col="country")
    except FileNotFoundError:
        error_exit("File not foud")
    except AssertionError as e:
        error_exit(e)
    print(f"Loading dataset of dimensions {res.shape}")
    return res
