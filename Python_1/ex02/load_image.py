import numpy as np
from PIL import Image, UnidentifiedImageError


def error_exit(msg: str):
    print(f"Error: {msg}")
    exit()


def ft_load(path: str) -> np.array:  # type: ignore
    try:
        assert path != "", "empty path name"
        assert isinstance(path, str), "path must be a string"
        im = Image.open(path, "r", ["PNG", "JPEG"])
    except FileNotFoundError:
        error_exit("Could not open " + path)
    except TypeError:
        error_exit("File format not handled")
    except ValueError:
        error_exit("IO instance input")
    except UnidentifiedImageError:
        error_exit("Cannot open and identify image")
    except AssertionError as e:
        error_exit(e)
    arr = np.asarray(im)
    print(f"the shape of the image is: {arr.shape}")
    return arr
