from cgi import test
from cgitb import small


class MaxHeap:

    def __init__(self, arr: list) -> None:
        self.arr = arr
        self.build()
        
    def build(self):
        self.heap_size = len(self.arr)
        for i in range(self.heap_size//2, -1, -1):
            self.heapify(i)
    
    def parent(self, idx: int) -> int:
        return idx // 2
        
    def left(self, idx: int) -> int:
        return (idx * 2) 

    def right(self, idx: int) -> int:
        return (idx * 2) + 1 

    def heapify(self, i: int):
        l = self.left(i)
        r = self.right(i)
        largest = i
        
        if l < self.heap_size and self.arr[l] > self.arr[largest]:
            largest = l

        if r < self.heap_size and self.arr[r] > self.arr[largest]:
            largest = r

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(largest)

    def sort(self) -> list:
        for i in range(len(self.arr)-1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.heap_size -= 1
            self.heapify(0)
        return self.arr

    def max(self) -> int:
        if self.heap_size < 1:
            raise "Heap Underflow"
        return self.arr[0]

    def extract_max(self) -> int:
        max = self.max()
        self.arr[0] = self.arr[-1]
        self.heap_size -= 1
        self.heapify(0)
        return max


class MinHeap:

    def __init__(self, items):
        idx = len(items) // 2
        self.size = len(items)
        self.heap = [0] + items[:]
        while idx > 0:
            self.sift_down(idx)
            idx -= 1

    def parent(self, idx: int) -> int:
        return idx // 2
        
    def left(self, idx: int) -> int:
        return (idx * 2) 

    def right(self, idx: int) -> int:
        return (idx * 2) + 1 
        
    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.sift_up(self.size)

    def sift_up(self, idx):

        while self.parent(idx) > 0:
            if self.heap[idx] < self.heap[self.parent(idx)]:

                self.heap[idx], self.heap[self.parent(idx)] = \
                self.heap[self.parent(idx)], self.heap[idx]
            
            i = self.parent(idx)

    def sift_down(self, idx):

        while self.left(idx) <= self.size:

            m = self.min_child(idx)

            if self.heap[idx] > self.heap[m]:
                self.heap[idx], self.heap[m] = self.heap[m], self.heap[idx]
            
            idx = m
        
    def min_child(self, idx):
        
        l, r = self.left(idx), self.right(idx)

        if r > self.size:
            return l
        return l if self.heap[l] < self.heap[r] else r

    def extract_min(self):
        min = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sift_down(1)
        return min

        
testArr = MinHeap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
print(testArr.heap)
print(testArr.extract_min())
print(testArr.extract_min())
print(testArr.heap)
