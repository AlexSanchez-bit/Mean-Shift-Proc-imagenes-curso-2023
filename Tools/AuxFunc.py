import cv2
import numpy as np
from Tools.AbelianGroup import *

def E(image):
    # Convertir la imagen a escala de grises
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    linialgi = gray_image.flatten()
    # Calcular el histograma de la imagen
    hist, _ = np.histogram(linialgi, bins=256, range=[0,256])
    
    # Calcular la probabilidad de cada nivel de intensidad
    prob = hist / np.sum(hist)
    
    # Eliminar ceros para evitar problemas con el logaritmo
    prob = prob[prob > 0]
    
    # Calcular la entropía de Shannon
    entropy = -np.sum(prob * np.log2(prob))

    return entropy

def Ep(image):
    # Convertir la imagen a escala de grises
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calcular el histograma y las probabilidades de la imagen
    hist, _ = np.histogram(gray_image.flatten(), bins=256, range=[0,256])
    prob = hist / np.sum(hist)

    # Calcular la esperanza (suma ponderada)
    result = np.sum(prob * np.arange(256))
    
    return result


def C(A, B):
    return E(ImgDif(A,B))
def D(A, B):
    return Ep(ImgDif(A,B))

def H(A,B):
    return (C(A,B) + 5*D(A,B))/2
