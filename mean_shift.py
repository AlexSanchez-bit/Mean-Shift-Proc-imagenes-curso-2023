import cv2
import numpy as np
import Tools
from Tools.StpCriteria import StpCrit

def custom_stopping_criterion(prev_shift, current_shift, threshold):
    return StpCrit(prev_shift,current_shift,threshold)
def mean_shift_custom_stopping(image, sp, sr, threshold):
    # Inicia la iteración
    prev_shift = np.ones_like(image, dtype=np.float32)
    #np.zeros_like(image, dtype=np.float32)
    current_shift = image  

    while not custom_stopping_criterion(prev_shift, current_shift, threshold):
        
        # Actualiza prev_shift para la próxima iteración
        prev_shift = current_shift.copy()
        
        # Aplica Mean Shift
        current_shift = cv2.pyrMeanShiftFiltering(prev_shift, sp=sp, sr=sr)


    return current_shift


def apply_mean_shift(imageDirectory,outputDir):
    image = cv2.imread(imageDirectory)

    # Parámetros de Mean Shift y criterio de parada
    spatial_radius = 15
    color_radius = 12
    convergence_threshold = 0.5
    # Aplica Mean Shift con criterio de parada personalizado
    result_image = mean_shift_custom_stopping(image, sp=spatial_radius, sr=color_radius, threshold=convergence_threshold)
    # Muestra la imagen resultante
    # cv2.imshow('Segmented Image', result_image)
    cv2.imwrite(outputDir, result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
