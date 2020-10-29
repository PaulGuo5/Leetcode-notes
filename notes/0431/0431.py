"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None
        new = TreeNode(root.val)
        if not root.children:
            return new
        
        new.left = self.encode(root.children[0]) # node's children
        node = new.left
        for child in root.children[1:]: # node's sibling
            node.right = self.encode(child)
            node = node.right
        return new
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return None
        new = Node(data.val, [])
        node = data.left
        while node:
            new.children.append(self.decode(node))
            node = node.right
        return new
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
