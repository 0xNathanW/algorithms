# For heaps with non-number elements.
# class Element:

#     def __init__(self, key, idx):
#         self.key = key
#         self.idx = idx

#     def parent(self):
#         return self.idx // 2
    
#     def left(self):
#         return self.idx * 2
    
#     def right(self):
#         return (self.idx * 2) + 1

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
        return (idx * 2) + 1

    def right(self, idx: int) -> int:
        return (idx * 2) + 2 

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


        
testArr = MaxHeap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
print(testArr.arr)
print(testArr.max())
print(testArr.arr)
print(testArr.extract_max())
print(testArr.arr)




