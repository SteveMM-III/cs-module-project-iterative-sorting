# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range( i + 1, len( arr ) ):
            smallest_index = j if arr[ j ] < arr[ smallest_index ] else smallest_index
        # TO-DO: swap
        # Your code here
        arr[ i ], arr[ smallest_index ] = arr[ smallest_index ], arr[ i ]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range( len( arr ) ):
        for j in range( 0, len( arr ) - i - 1 ):
            if arr[ j ] > arr[ j + 1 ]:
                arr[ j ], arr[ j + 1 ] = arr[ j + 1 ], arr [ j ]

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr):
    # Your code here

    # check for empty array
    if len( arr ) == 0:
        return []

    arr_len = len( arr )
    maximum = max( arr ) + 1 # + 1 allows for zero index

    # initialize the position array
    position = [ 0 ] * maximum

    # use value of each arr item as index to increment position array values
    for i in arr:
        # check for negative
        if i < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        position[ i ] += 1

    x = 0
    for i in range(0, maximum):
        temp = position[ i ]
        position[ i ] = x
        x += temp
    
    result = [ None ] * arr_len

    for i in arr:
        result[ position[ i ] ] = i
        position[ i ] += 1

    return result
# https://ayada.dev/posts/counting-sort/