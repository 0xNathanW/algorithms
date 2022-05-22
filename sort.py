from asyncio import create_subprocess_shell
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

unittest.main()