from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    img = ft_load("animal.jpeg")
    print(img)
    zoom = img[100:500, 450:850, 0:1]
    small_shape = np.squeeze(zoom).shape
    print(f"The shape of the image is: {zoom.shape} or {small_shape}")
    print(zoom)
    row = range(len(zoom))
    col = range(len(zoom[0]))
    trans = [[zoom[j][i] for j in row] for i in col]
    plt.imshow(trans, 'gray')
    try:
        plt.show()
    except KeyboardInterrupt:
        print("\nProgram interrupted!")
        exit()


if __name__ == "__main__":
    main()
