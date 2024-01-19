from mean_shift import apply_mean_shift
from os import listdir

images = listdir('./input')

for image in images:
     apply_mean_shift('./input/'+image,'./output/'+image)
