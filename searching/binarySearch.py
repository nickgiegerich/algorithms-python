# Recursive binary search
#
# Binary search requires the array to be sorted first 
#
#


# arr - the array that we are searching 
# l - the leftmost position in the array usually 0 
# r - the rightmost position in the array (length - 1)
# x - the element we are searching for
def binarySearch (arr, l, r, x):


    #Check the base case
    if r >= l:

        mid = l + (r - l)/2

        # If the element happens to be in the middle
        if arr[mid] == x: 
            return mid

        # If the element is smaller than the mid then it can
        # only exist in the left part of the array
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else the element can only be present in the right subarray
        else: 
            return binarySearch(arr, mid+1, r, x)
        
    # Else the item does not exist in the array
    else:
        return -1


# TEST DATA

arr = [ 2, 3, 4, 10, 40]
x = 2

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1: 
    print "Element is present at index %d" % result
else:
    print "Element is not present in the array"