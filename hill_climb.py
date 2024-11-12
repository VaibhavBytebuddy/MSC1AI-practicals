#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:12:20 2024

@author: vaibhav
"""

'''

import random

# Define the function we want to maximize
def f(x):
    return -x**2 + 4*x

# Hill climbing algorithm
def hill_climbing(start, step_size, max_iterations):
    current_x = start
    current_f = f(current_x)
    
    for _ in range(max_iterations):
        # Generate a neighbor by taking a step to the left or right
        next_x = current_x + random.choice([-step_size, step_size])
        next_f = f(next_x)
        
        # If the neighbor has a better value, move to that point
        if next_f > current_f:
            current_x, current_f = next_x, next_f
    
    return current_x, current_f

# Parameters
start = 0         # Starting point
step_size = 0.1   # Step size for hill climbing
max_iterations = 10  # Maximum iterations

# Run the hill climbing algorithm
best_x, best_f = hill_climbing(start, step_size, max_iterations)

# Output the results
print(f"Best x: {best_x}")
print(f"Maximum value of f(x): {best_f}")

'''
import random

def f(x):
    return x*2+x**2

def hill(start,steps,maxI):
    curr_x=start
    curr_f=f(curr_x)


    for _ in range(maxI):
        next_x=curr_x+random.choice([-steps,steps])
        next_f=f(next_x)

        if next_f>curr_f:
            curr_f,curr_x=next_f,next_f


    return curr_x,curr_f


a,b=hill(1,0.1,20)

print(f"a= ",a, "b= ",b )



