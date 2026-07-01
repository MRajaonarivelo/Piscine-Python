from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np

def main():
    img = ft_load("animal.jpeg")
    print(img)
    zoom = img[100:500, 450:850, 0:1]
    print(f"The shape of the image is: {zoom.shape} or {np.squeeze(zoom).shape}")
    print(zoom)
    trans = [[zoom[j][i] for j in range(len(zoom))] for i in range(len(zoom[0]))]
    plt.imshow(trans, 'gray')
    try:
        plt.show()
    except KeyboardInterrupt:
        print("\nProgram interrupted!")
        exit()


if __name__ == "__main__":
    main()
