#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:50:26 2024

@author: vaibhav
"""

def minimax(node, depth, maximizing_player):
    if depth == 0 or is_terminal_node(node):
        return evaluate(node)
        
    if maximizing_player:
        max_eval = float('-inf')
        for child in get_children(node):
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for child in get_children(node):
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

# Example helper functions (need to be implemented based on specific game)
def is_terminal_node(node):
    # Check if node is terminal (game over)
    pass

def evaluate(node):
    # Return evaluation score for node
    pass

def get_children(node):
    # Return list of possible next states
    pass