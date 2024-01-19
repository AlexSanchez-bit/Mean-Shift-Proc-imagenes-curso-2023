import cv2
import numpy as np

def Sum(A, B):
    return min((A+B), -(A+B))

def ImgSum(A, B):
    height, width, channels = A.shape
    # Crear una matriz de ceros (imagen en negro)
    image = np.zeros((height, width), dtype=np.uint8)

    # Construir la imagen píxel a píxel
    for y in range(height):
        for x in range(width):
            # Asignar un valor de intensidad (escala de grises) al píxel
            image[y, x] = Sum(A[y,x], B[y,x])
    cv2.imwrite("imSum.png", image)
    return cv2.imread("imSum.png")