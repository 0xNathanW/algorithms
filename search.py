from math import ceil
import unittest
import random

# Array must be sorted first, if so runs in log(n) time.
def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper: 
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   
                break    
            lower = x
        elif target < val:
            upper = x

# Finds the ith order statistics (ith smallest element):
def randomised_select(arr, i):
    if len(arr) == 1:
        return arr[0]
    j = partition(arr, random.randrange(len(arr)))
    if i == j:
        return arr[j]
    if j > i:
        return randomised_select(arr[:j], i)
    else:
        return randomised_select(arr[j+1:], i)

def partition(arr: list, p: int):
    i = 0
    if p != 0:
        arr[0], arr[p] = arr[p], arr[0]

    for j in range(len(arr)-1):
        if arr[j+1] <= arr[0]:
            arr[i+1], arr[j+1] = arr[j+1], arr[i+1]
            i+=1
    arr[i], arr[0] = arr[0], arr[i]
    return i

def deterministic_select(arr, i):

    while len(arr) % 5 != 0:
        for j in range(1, len(arr)):
            if arr[0] > arr[j]:
                arr[0], arr[j] = arr[j], arr[0]
        if i == 0:
            return arr[0]
        arr = arr[1:]
        i-=1

    g = int(len(arr) / 5)
    for n in range(g):
        arr[5*n:(5*n)+5] = insertion_sort(arr[5*n:(5*n)+5])

    pivot = deterministic_select(arr[2*g:3*g], ceil(i/2))
    pivot_idx = arr.index(pivot)
    q = partition(arr, pivot_idx)
    if i == q:
        return arr[q]
    if q > i:
        return deterministic_select(arr[:q], i)
    else:
        return deterministic_select(arr[q+1:], i)

def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        n = i
        while n > 0 and arr[n] < arr[n-1]:
            arr[n], arr[n-1] = arr[n-1], arr[n]
            n-=1
    return arr

class Tests(unittest.TestCase):

    def test_binary(self):

        cases = [
            sorted(random.sample(range(1, 40), 5)),
            sorted(random.sample(range(-50, 20), 12)),
            sorted(random.sample(range(0, 1000), 200)),
        ]

        items = [random.choice(case) for case in cases]

        for i in range(len(cases)):
            self.assertEqual(
                cases[i].index(items[i]),
                binary_search(cases[i], items[i])
            )


#unittest.main()