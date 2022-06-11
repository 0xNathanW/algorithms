from collections import deque
from re import X

class Node:

    def __init__(self, key=None):

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
            self.inorder(x.l)
            print(x.key)
            self.inorder(x.r)

    def search_recurse(self, k, x="root"):
        if x=="root":
            x = self.root
        if x == None or k == x.key:
            return x
        
        return self.search(k, x.l) if k<x.key else self.search(k, x.r)

    def search(self, k):
        x = self.root
        while x is not None and k != x.key:
            x = x.l if k<x.key else x.r
        return x

    def insert(self, new):
        z = Node(new)
        x, y = self.root, None

        while x is not None:
            y=x
            x = x.l if z.key < x.key else x.r
        
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.l = z
        else:
            y.r = z

    def insert_list(self, new):
        for n in new:
            self.insert(n)

    def minimum(self, x="root"):
        
        if x == "root":
            x = self.root

        while x.l is not None:
            x = x.l
        return x

    def maximum(self, x="root"):
        
        if x == "root":
            x = self.root

        while x.r is not None:
            x = x.r
        return x

    def successor(self, x):
        if x.r is not None:
            return self.minimum(x.r)
        
        y = x.p
        while y is not None and x == y.r:
            x = y
            y = y.p
        return y

    def preccessor(self, x):
        if x.l is not None:
            return self.maximum(x.l)

        y = x.p
        while y is not None and x == y.l:
            x = y
            y = y.p
        return y

    def transplant(self, u, v):
        # Replaces subtree at node u with that rooted at node v.
        if u.p is None:
            self.root = v
        elif u == u.p.l:
            u.p.l = v
        else: 
            u.p.r = v
        if v is not None:
            v.p = u.p

    def delete(self, z):
        
        if z.l is None:
            self.transplant(z, z.r)
        elif z.r is None:
            self.transplant(z, z.l)
        else:
            y = self.minimum(z.r)
            if y != z.r:
                self.transplant(y, y.r)
                y.r = z.r
                y.r.p = y
            self.transplant(z, y)
            y.l = z.l
            y.l.p = y

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

tree = Tree(Node(6))
tree.insert_list([5, 7, 2, 5, 8, 1, 3, 4])
tree.print_tree()
tree.delete(tree.search(5))
print("="*20)
tree.print_tree()