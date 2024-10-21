#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 07:37:25 2024

@author: vaibhav
"""


from collections import defaultdict

jug1 = int(input("Enter the jug 1 size: "))
jug2 = int(input("Enter the jug 2 size: "))
aim = int(input("Enter the goal state: "))

visited = defaultdict(lambda: False)

def waterjug(x, y):
    # Base case: If either jug reaches the goal state
    if (x == aim or y == aim):
        print(f"({x}, {y})")  # Print final state
        return True
    
    # If the state has not been visited before
    if visited[(x, y)] == False:
        # Mark the current state as visited
        visited[(x, y)] = True
        
        # Print current state
        print(f"({x}, {y})")
        
        # Try all possible actions and return True if one of them solves the problem
        return (waterjug(x, 0) or      # Empty jug 2
                waterjug(0, y) or      # Empty jug 1
                waterjug(x, jug2) or   # Fill jug 2
                waterjug(jug1, y) or   # Fill jug 1
                waterjug(x + min(y, jug1 - x), y - min(y, jug1 - x)) or  # Pour water from jug 2 to jug 1
                waterjug(x - min(x, jug2 - y), y + min(x, jug2 - y))     # Pour water from jug 1 to jug 2
               )
    else:
        return False

print("Water jug steps:")

# Call the function starting with both jugs empty
if not waterjug(0, 0):
    print("No solution possible.")
