
"""
Solutions to module 4
Review date:
"""

student = "Izabelle Norlander"
reviewer = ""


import random as r
import matplotlib.pyplot as plt 
import math

def approximate_pi(n):
    
    coordinates = [(2 * r.random()-1, 2 *  r.random()-1) for _ in range(n)]
    
    coordinates_in_circle = []
    
    for coordinate in coordinates:
        if (coordinate[0]**2 + coordinate[1]**2)**0.5 <= 1:
            coordinates_in_circle.append(coordinate)
        
    number_in_circle = len(coordinates_in_circle)
    
    ratio = number_in_circle/n
    
    return 4 * ratio

def plot_figure(n):
    
    coordinates = [(2 * r.random()-1, 2 * r.random()-1) for _ in range(n)]
    
    coordinates_in_circle = []
    coordinates_outside_of_circle = []
    
    for coordinate in coordinates:
        if (coordinate[0]**2 + coordinate[1]**2)**0.5 <= 1:
            coordinates_in_circle.append(coordinate)
            
        else:
            coordinates_outside_of_circle.append(coordinate)
    
    x_inside, y_inside = zip(*coordinates_in_circle)
    x_outside, y_outside = zip(*coordinates_outside_of_circle)
    
    plt.scatter(x_inside, y_inside, color='red', s=1)
    plt.scatter(x_outside, y_outside, color='blue', s=1)
    
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    
    plt.gca(). set_aspect('equal', adjustable='box')
    
    plt.show()
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        print(approximate_pi(n))
        plot_figure(n)
        
    print(f'Real value: {math.pi}')

if __name__ == '__main__':
	main()
