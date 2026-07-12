from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    '''displays a square cut of animal.jpeg'''
    img = ft_load("animal.jpeg")
    print(img)
    zoom = img[100:500, 450:850, 0:1]
    print(f"New shape after slicing: {zoom.shape} or {np.squeeze(zoom).shape}")
    print(zoom)
    plt.imshow(zoom, 'gray')
    try:
        plt.show()
    except KeyboardInterrupt:
        print("\nProgram interrupted!")
        exit()


if __name__ == "__main__":
    main()
