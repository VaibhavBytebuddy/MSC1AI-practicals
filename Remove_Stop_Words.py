#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:43:39 2024

@author: vaibhav
"""

import nltk
from nltk.corpus import stopwords

def remove_stopwords(text):
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)