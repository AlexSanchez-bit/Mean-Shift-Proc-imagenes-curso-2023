import cv2
import numpy as np
from Tools.AuxFunc import *

def StpCrit(A, B, e):
    k =H(A, B)
    print(k)
    return k <= e
    