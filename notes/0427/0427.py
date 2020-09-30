"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(x, y, l):
            if l == 1:
                node = Node(grid[x][y], True, None, None, None, None)
            else:
                topL = dfs(x, y, l//2)
                topR = dfs(x, y+l//2, l//2)
                botL = dfs(x+l//2, y, l//2)
                botR = dfs(x+l//2, y+l//2, l//2)
                val = topL.val or topR.val or botL.val or botR.val
                if topL.isLeaf and topR.isLeaf and botL.isLeaf and botR.isLeaf and topL.val == topR.val == botL.val == botR.val:
                    node = Node(val, True, None, None, None, None)
                else:
                    node = Node(val, False, topL, topR, botL, botR)
            return node
        return grid and dfs(0, 0, len(grid)) or None
