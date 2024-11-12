#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:32:45 2024

@author: vaibhav
"""


import random

def hangman():
    words = ['python', 'programming', 'computer', 'algorithm ', 'database']
    word = random.choice(words)
    guessed = set()
    tries = 6
    
    while tries > 0:
        display = ''.join(c if c in guessed else '_' for c in word)
        print(f"\nWord: {display}")
        print(f"Tries left: {tries}")
        
        if '_' not in display:
            print("You won!")
            return
            
        guess = input("Guess a letter: ").lower()
        if guess in guessed:
            print("You already guessed that!")
            continue
            
        guessed.add(guess)
        if guess not in word:
            tries -= 1
            print("Wrong guess!")
    
    print(f"\nGame Over! The word was: {word}")