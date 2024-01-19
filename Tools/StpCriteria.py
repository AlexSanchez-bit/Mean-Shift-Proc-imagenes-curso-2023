import cv2
import numpy as np
from AuxFunc import *

def StpCrit(A, B, e):
    return H(A, B) <= e
    