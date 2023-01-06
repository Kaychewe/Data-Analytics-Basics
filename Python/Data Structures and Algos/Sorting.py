"""
    Author: Kasonde Chewe 
    File: sorting.py
    
    Table of Contents
    1. Bubble Sort 
    2. Insertion Sort
    3. Selection Sort 
    4. Merge Sort 
    5. Shell Sort 
    6. Quick Sort
    7. Heap Sort
    8. Cycle Sort
    9. Storage Sort 
    10. Gnome Sort 
    11. Odd Even sort
    12. Bogo Sort
    13. Combo Sort
    
"""


# 1. Bubble Sort Algorithm aka sinking sort
# Complexity: O(n^2) because of inner and outer loop


def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(i)-1:
            # Swap Condition 
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


# 2. Insertion Sort Algorithm 
# Complexity: O(n^2)
arr = [1, 8, 3, 2, 5, 10]

def insertion_sort(arr):
    for i in range(1, len(arr)): #Outer loop is O(n) - worst case
        j = i
        while arr[j-1]> arr[j] and j > 0: # Inner loop is O(n) - worst case
            arr[j-1], arr[j] = arr[j],arr[j-1]
            j-=1
insertion_sort((arr))
print(arr)

#



            
            
        
    
        
                
                




