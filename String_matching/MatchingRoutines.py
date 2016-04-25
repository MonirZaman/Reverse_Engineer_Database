# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:52:28 2016

@author: Monir Zaman
"""

def levenshtein(s1, s2):
    """
    Args:
        s1,s2 - strings
    Return:
        edit distance between two strings
    Collected from:
    https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
    
    """
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def similarity(s1,s2):
    """
    Args:
        s1,s2 - strings
    Return:
        normalized similarity score between two strings
        Method is case sensitive
    """
    denom=len(s1) if len(s1)>len(s2) else len(s2)
    #return the normalized similarity score
    sscore=1.0-(float(levenshtein(s1,s2))/denom)
    return sscore