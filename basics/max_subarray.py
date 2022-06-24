import math
import numpy as np
import time
import matplotlib.pyplot as plt

# Finds max sum subarray which indicies cross the mid-point. 
def max_crossing_subarray(arr, low, mid, high):

    leftSum = -math.inf
    sum, maxLeft = 0, None
    for i in range(mid, low-1, -1):
        sum += arr[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i
    
    rightSum = -math.inf
    sum, maxRight = 0, None
    for j in range(mid+1, high+1):
        sum += arr[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j
    
    # Return max indicies and total sum of max subarray.
    return maxLeft, maxRight, leftSum+rightSum

def max_subarray(arr, low, high):   
    
    # Base case, one element, largest subarray is it.
    if high==low:
        return low, high, arr[low]
    
    mid = (low+high) // 2

    # Max subarry either in arr[low:mid].
    leftLow, leftHigh, leftSum = max_subarray(arr, low, mid)
    # or arr[mid:high].
    rightLow, rightHigh, rightSum = max_subarray(arr, mid+1, high)
    # or accross the midpoint.
    crossLow, crossHigh, crossSum = max_crossing_subarray(arr, low, mid, high)

    if leftSum >= rightSum and leftSum >= crossSum:
        return leftLow, leftHigh, leftSum
    elif rightSum >= leftSum and rightSum > crossSum:
        return rightLow, rightHigh, rightSum
    else:
        return crossLow, crossHigh, crossSum

def brute(arr):
    max_sum, low, high = -math.inf, -1, -1
    for i in range(len(arr)):
        k = arr[i]
        if k > max_sum:
                max_sum, low, high = k, i, i
        for j in range(i+1, len(arr)):
            k += arr[j]
            if k > max_sum:
                max_sum, low, high = k, i, j
    return low, high, max_sum


# Plots runtimes of the two algorithms.
def compare():

    fig, ax = plt.subplots()

    for n in range(2, 100):

        arr = np.random.randint(-100, 100, n)
        
        t1_start = time.perf_counter_ns()
        a, b, c = max_subarray(arr, 0, len(arr)-1)
        t1_stop = time.perf_counter_ns()
        
        t2_start = time.perf_counter_ns()
        d, e, f = brute(arr)
        t2_stop = time.perf_counter_ns()
        
        ax.plot(n, t1_stop-t1_start, marker="o", color="r")
        ax.plot(n, t2_stop-t2_start, marker="^", color="b")

    plt.show()

compare()
