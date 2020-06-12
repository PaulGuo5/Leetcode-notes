class Solution:
    def validTree1(self, n: int, edges: List[List[int]]) -> bool:
        if not edges and n == 1: return True
        if not edges and n > 1: return False
        def findRoot(x, tree):
            if tree[x] == -1: return x
            root = findRoot(tree[x], tree)
            tree[x] = root
            return root
        tree = [-1]*(n)
        for e in sorted(edges):
            x = findRoot(e[0], tree)
            y = findRoot(e[1], tree)
            if x == y:
                return False
            if x < y:
                tree[y] = x
            else:
                tree[x] = y
        return len(edges) == n-1
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(nums, i):
            if nums[i] == -1: return i
            return find(nums, nums[i])
        def union(nums, a, b):
            aa = find(nums, a)
            bb = find(nums, b)
            if aa == bb:
                return False
            nums[aa] = bb
            return True
        nums = [-1]*n
        for a, b in edges:
            if not union(nums, a, b):
                return False
        return len(edges) == n-1
        
