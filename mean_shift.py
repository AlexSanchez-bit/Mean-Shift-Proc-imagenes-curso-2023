import cv2
import numpy as np
import Tools
from Tools.StpCriteria import StpCrit

def custom_stopping_criterion(prev_shift, current_shift, threshold):
    return StpCrit(prev_shift,current_shift,threshold)
def mean_shift_custom_stopping(image, sp, sr, threshold):
    # Inicia la iteración
    prev_shift = np.zeros_like(image, dtype=np.float32)
    current_shift = np.ones_like(image, dtype=np.float32)

    while not custom_stopping_criterion(prev_shift, current_shift, threshold):
        # Aplica Mean Shift
        current_shift = cv2.pyrMeanShiftFiltering(image, sp=sp, sr=sr)

        # Actualiza prev_shift para la próxima iteración
        prev_shift = current_shift.copy()

    return current_shift

# Carga tu imagen
image = cv2.imread('image.tif')

# Parámetros de Mean Shift y criterio de parada
spatial_radius = 10
color_radius = 50
convergence_threshold = 1.0

# Aplica Mean Shift con criterio de parada personalizado
result_image = mean_shift_custom_stopping(image, sp=spatial_radius, sr=color_radius, threshold=convergence_threshold)

# Muestra la imagen resultante
cv2.imshow('Segmented Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
