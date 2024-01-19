import cv2
import numpy as np
from Tools.AuxFunc import *

def StpCrit(A, B, e):
    return H(A, B) <= e
    