from logging import captureWarnings
from unittest import TestCase
import random
import unittest

# Big(O) = n*log2(n)
def merge_sort(arr: list) -> list:

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left: list, right: list) -> list:
    merged = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i +=1
        else:
            merged.append(right[j])
            j += 1
    
    merged += left[i:]
    merged += right[j:]
    return merged
     

def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        n = i
        while n > 0 and arr[n] < arr[n-1]:
            arr[n], arr[n-1] = arr[n-1], arr[n]
            n-=1
    return arr


def selection_sort(arr: list) -> list:
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


def bubble_sort(arr: list) -> list:

    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

def quick_sort(arr: list, low=0, high=None):
    if high is None:
        high = len(arr)-1

    if low < high:
        q, arr = partition(arr, low, high)
        quick_sort(arr, low, q-1)
        quick_sort(arr, q+1, high)

def partition(arr: list, low: int, high:int):

    pivot = arr[high]
    i = low-1

    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1, arr

# best when range of possible values is small.
def counting_sort(arr: list) -> list:
    k = [0] * (max(arr)+1)
    out = [0] * len(arr)
    for elem in arr:
        k[elem] += 1
    
    for i in range(1, len(k)):
        k[i] += k[i-1]

    # iterating backwards preserves stability.
    for elem in arr[::-1]:
        idx = k[elem] - 1
        out[idx] = elem
        k[elem] -= 1
        
    return out

def radix_sort(arr: list) -> list:
    maxi = max(arr)
    for i in range(1, len(str(maxi))):
        arr = counting_sort(arr)
    return arr

def counting4radix(arr: list) -> list:
    k = [0] * 10 # working in base 10.
    out = [0] * len(arr)
    for i in arr:
        k[i] += 1
    for j in range(1, len(k)):
        k[j] += k[j-1]
    for elem in arr[::-1]:
        idx = k[elem] - 1
        out[idx] = elem
        k[elem] -= 1
    return out

def bucket_sort(arr: list) -> list:

    bucket_size = max(arr) / len(arr)
    buckets = [[] for i in range(len(arr))]
    out = []

    for i in range(len(arr)):
        j = int(arr[i]//bucket_size)
        if j != len(buckets):    
            buckets[j].append(arr[i])
        else:
            buckets[len(buckets)-1].append(arr[i])

    for b in buckets:
        out += insertion_sort(b)

    return out


class TestSorts(TestCase):

    cases = [
        [],
        [0, 0, 0],
        random.sample(range(1, 40), 5),
        random.sample(range(-50, 50), 5),
        random.sample(range(0, 2500), 5)
    ]

    def test_merge(self):
        for case in self.cases:
            self.assertEqual(merge_sort(case), sorted(case))

    def test_insertion(self):
        for case in self.cases:
            self.assertEqual(insertion_sort(case), sorted(case))

    def test_selection(self):
        for case in self.cases:
            self.assertEqual(selection_sort(case), sorted(case))

    def test_bubble(self):
        for case in self.cases:
            self.assertEqual(bubble_sort(case), sorted(case))
    
    def test_quicksort(self):
        for case in self.cases:
            quick_sort(case)
            self.assertEqual(case, sorted(case))

    def test_counting(self):
        for case in [self.cases[2], self.cases[4]]:
            self.assertEqual(counting_sort(case), sorted(case))


unittest.main()