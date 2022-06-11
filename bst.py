from collections import deque

class Node:

    def __init__(self, key: int):

        self.key = key
        self.p = None
        self.l = None
        self.r = None
    
class Tree:

    def __init__(self, root: Node):
        self.root = root

    def inorder(self, x="root"):
        
        if x=="root":
            x = self.root

        if x != None:
            self.inorder(x.left)
            print(x.key)
            self.inorder(x.right)

    def search_recurse(self, k, x="root"):
        if x=="root":
            x = self.root
        if x == None or k == x.key:
            return x
        
        return self.search(k, x.left) if k<x.key else self.search(k, x.right)

    def search(self, k):
        x = self.root
        while x is not None and k != x.key:
            x = x.left if k<x.key else x.right
        return x

    def insert(self, new):
        z = Node(new)
        x, y = self.root, None

        while x != None:
            y=x
            if z.key < x.key:
                x = x.left

    def print_tree(self):
        root = self.root
        res = []
        q = deque([root])
        while q:
            row = []
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    row.append("#")
                    continue
                row.append(node.key)
                q.append(node.l)
                q.append(node.r)
            res.append(row)
        rows = len(res)
        base = 2**(rows)
        for r in range(rows):
            for v in res[r]:
                print("." * (base), end = "")
                print(v, end = "")
                print("." * (base - 1), end = "")
            print("|")
            base //= 2

test = Tree(Node(6))

