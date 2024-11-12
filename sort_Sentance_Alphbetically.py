#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:12:47 2024

@author: vaibhav
"""


# 3. Sort Sentence Alphabetically
def sort_sentence(sentence):
    words = sentence.split()
    return ' '.join(sorted(words))