import math
from display import *

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    pass

#Return the dot porduct of a . b
def dot_product(a, b):
    return (a[0] * b[0]) + (a[1] * b[1]) + (a[2] * b[2])

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    point0 = polygons[i]
    point1 = polygons[i + 1]
    point2 = polygons[i + 2]
    a = [point1[0] - point0[0], point1[1] - point0[1], point1[2] - point0[2]]
    b = [point2[0] - point0[0], point2[1] - point0[1], point2[2] - point0[2]]
    return [(a[1] * b[2]) - (a[2] * b[1]),
            (a[2] * b[0]) - (a[0] * b[2]),
            (a[0] * b[1]) - (a[1] * b[0])]
