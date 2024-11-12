#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:17:34 2024

@author: vaibhav
"""

import string

def remove_punctuation(text):
    return ''.join(char for char in text if char not in string.punctuation)
