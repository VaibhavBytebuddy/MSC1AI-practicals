#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:40:14 2024

@author: vaibhav
"""

import nltk
from nltk.stem import WordNetLemmatizer

def lemmatize_text(text):
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')
    lemmatizer = WordNetLemmatizer()
    
    # Tokenize and lemmatize
    words = text.split()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)


import nltk
nltk.download('all')
