import matplotlib.pyplot as plt
import numpy as np


def display(array):
    '''displays the array as an image'''
    plt.imshow(array)
    try:
        plt.show()
    except KeyboardInterrupt:
        print("\nProgram interrupted!")
        exit()


def ft_invert(array) -> np.array:  # type: ignore
    '''Inverts the color of the image provided'''
    res = (255 - array)
    display(res)
    return res


def ft_red(array) -> np.array:  # type: ignore
    '''Applies a red color filter to the image provided'''
    res = array * np.array([1, 0, 0])
    display(res)
    return res


def ft_green(array) -> np.array:  # type: ignore
    '''Applies a green color filter to the image provided'''
    z = np.zeros((array.shape[0], array.shape[1], 1), dtype=np.uint8)
    r = np.array(array[:, :, 0:1])
    b = np.array(array[:, :, 2:3])
    tmp = np.concatenate((r,z,b), 2)
    res = array - tmp
    display(res)
    return(res)
