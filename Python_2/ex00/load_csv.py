import pandas as pd

def error_exit(msg: str):
    '''prints an error msg and exits the program'''
    print(f"Error: {msg}")
    exit()

def load(path: str) -> pd.DataFrame:
    try:
        assert path != "", "empty path name"
        res = pd.read_csv(path)
    except AssertionError as e:
        error_exit(e)
    print(f"Loading dataset of dimensions {res.shape}")
    return res