#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:38:40 2024

@author: vaibhav
"""

def is_safe(board, row, col, n):
    # Check row on left side
    for j in range(col):
        if board[row][j] == 1:
            return False
            
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
            
    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
            
    return True

def solve_n_queens(n):
    board = [[0 for x in range(n)] for y in range(n)]
    
    def solve_util(col):
        if col >= n:
            return True
            
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                if solve_util(col + 1):
                    return True
                board[i][col] = 0
        return False
    
    if solve_util(0):
        return board
    return None