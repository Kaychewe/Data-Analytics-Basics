"""
    Author: Kasonde Chewe 
    File: Searching.py
    
    Table of Content
    ----------------------------------
    1. Brute Force Search
    2. Binary Search
        
"""

# 1. Brute Force Search Algorithm
# Complexity = Linear 

def brute_force_search(list, target):
    for item in list:
        if item == target:
            return True
        else:
            return False
        
# 2. Binary Search Algorithm
def binarySearch(list,target):
    low = 0 
    high = len(list)-1
    
    for i in range(len(list)):
        mid = (low+high)/2 
        if target > list[mid]:
            low = mid+1
        elif t < list[mid]:
            high = mid-1
        else:
            return list.index(t)
    return 'item not in list'

