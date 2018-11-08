#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:06:23 2018

@author: yotroz
"""

#hello this s first commit 

#%%

# Bubble sort implementation.
#
# This function returns nothing because it works by mutating the lst.
def bubble(lst):
    for j in range(0, len(lst) - 1):
        for i in range(0, len(lst) - j - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                
# this function uses our previously declared function merge
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    return merge(merge_sort(left), merge_sort(right))
