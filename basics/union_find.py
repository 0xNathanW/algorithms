# Array based union find.
import enum


class UnionFind:

    def __init__(self, objects):
        self.mapping = {obj: i for i, obj in enumerate(objects)}
        self.arr = [i for i in range(len(objects))]

        print(self.mapping)
        print(self.arr)
    
    def union(self, a, b):



UnionFind(["E", "F", "I", "D", "C", "A", "J", "L", "G", "K", "B", "H"])

