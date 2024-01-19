import cv2
import numpy as np

def Sum(A, B):
    # Ejemplo de operación Sum en dos arrays tridimensionales
    return np.minimum((A + B) % 256, (-(A + B)) % 256)


def ImgDif(A, B):
    height, width, channels = A.shape
    # Crear una matriz de ceros (imagen en negro)
    image =np.minimum((A + B) % 256, (-(A + B)) % 256)
    # Construir la imagen píxel a píxel
    cv2.imwrite("imSum.png", image)
    return cv2.imread("imSum.png")