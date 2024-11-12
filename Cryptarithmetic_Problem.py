#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:47:09 2024

@author: vaibhav
"""

from itertools import permutations

def solve_cryptarithmetic():
    # All digits from 0-9
    digits = range(10)
    
    # Get all possible permutations for T, W, O, F, U, R
    for t, w, o, f, u, r in permutations(digits, 6):
        # Skip if T or F is 0 (no leading zeros)
        if t == 0 or f == 0:
            continue
            
        # Calculate TWO and FOUR
        two = 100 * t + 10 * w + o
        four = 1000 * f + 100 * o + 10 * u + r
        
        # Check if TWO + TWO = FOUR
        if two + two == four:
            return {
                'T': t, 'W': w, 'O': o,
                'F': f, 'U': u, 'R': r,
                'TWO': two,
                'FOUR': four
            }
    return None