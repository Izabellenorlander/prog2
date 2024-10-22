
"""
Solutions to module 4
Review date:
"""

student = "Izabelle Norlander"
reviewer = ""

import math as m
import random as r
from functools import reduce

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    points = [[r.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    
    inside_hypersphere = lambda point: sum(map(lambda x: x**2, point)) <= 1
    
    points_inside = list(filter(inside_hypersphere, points))
    
    volume_approx = 2**d * len(points_inside) / n

    return volume_approx

def hypersphere_exact(n,d):
    
    return (m.pi**(d/2))/(m.gamma((d/2)+1))
     
def main():
    
    for n, d in [(100000, 2), (100000, 11)]:
        
        print(f'Approximate volume for ({n}, {d}): {sphere_volume(n, d)}')
        print(f'Real volume for ({n}, {d}): {hypersphere_exact(n, d)}')


if __name__ == '__main__':
	main()
