import cv2
import numpy as np
from AbelianGroup import *

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
    linialgi = gray_image.flatten()
    # Calcular el histograma de la imagen
    hist, _ = np.histogram(linialgi, bins=256, range=[0,256])
    
    # Calcular la probabilidad de cada nivel de intensidad
    prob = hist / np.sum(hist)

    return np.sum(prob * linialgi)


def C(A, B):
    return E(Sum(A,B))
def D(A, B):
    return Ep(Sum(A,B))

def H(A,B):
    return (C(A,B) + 5*D(A,B))/2
