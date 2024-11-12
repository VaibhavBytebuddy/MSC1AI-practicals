#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:48:33 2024

@author: vaibhav
"""

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_terminal_node(node):
        return evaluate(node)
        
    if maximizing_player:
        max_eval = float('-inf')
        for child in get_children(node):
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for child in get_children(node):
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval