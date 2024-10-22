
"""
Solutions to module 4
Review date:
"""

student = 'Izabelle Norlander'
reviewer = ""

import math as m
import random as r
from time import perf_counter as pc
import concurrent.futures as future

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    points = [[r.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    
    inside_hypersphere = lambda point: sum(map(lambda x: x**2, point)) <= 1
    
    points_inside = list(filter(inside_hypersphere, points))
    
    volume_approx = 2**d * len(points_inside) / n

    return volume_approx
    

def hypersphere_exact(n,d):
    
    return (m.pi**(d/2))/(m.gamma((d/2)+1))
     

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
     #using multiprocessor to perform 10 iterations of volume function  
     
    with future.ProcessPoolExecutor() as executor:
        futures = [executor.submit(sphere_volume, n, d) for _ in range(np)]
        results = [future.result() for future in futures] 
        
    
     
    return sum(results) / np

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    
    n_per_process = n // np
    
    with future.ProcessPoolExecutor() as executor:
        results = list(executor.map(sphere_volume, [n_per_process] * np, [d] * np))
        
    
    
    return sum(results) / np

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11

    start_time = pc()

    for y in range (10):
        sphere_volume(n,d)

    end_time = pc()
    
    print(f'Serial execution time: {end_time - start_time} seconds')
    
    
    # Parallel loop execution timing
    start_time = pc()
    results_parallel1 = sphere_volume_parallel1(n, d, 10)
    end_time = pc()
    print(f"Parallel loop execution time: {end_time - start_time} seconds")
    print(f"Parallel loop results: {results_parallel1}")

    # Parallel data division execution timing
    start_time = pc()
    volume_parallel2 = sphere_volume_parallel2(n, d, 10)
    end_time = pc()
    print(f"Parallel data split execution time: {end_time - start_time} seconds")
    print(f"Parallel data split volume: {volume_parallel2}")

    # Exact volume for comparison
    exact_volume = hypersphere_exact(n, d)
    print(f"Exact volume for V({d})(1): {exact_volume}")
    
    
if __name__ == '__main__':
	main()
