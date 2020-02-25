# Selection Sort 
#
#  
#
#

import sys

A = [100, 30, 376, 5, 78, 120, 100]

# Traverse through all the array elements
for i in range(len(A)): 

    # Find the minimum element in the remaining unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]: 
            min_idx = j

    # Swap the minimun found with the first element
    A[i], A[min_idx] = A[min_idx], A[i]


print ("Sorted array")
for i in range(len(A)): 
    print("%d" %A[i]),