# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def write(root):
            if not root:
                res.append("#")
            else:
                res.append(str(root.val))
                write(root.left)
                write(root.right)
        res = []
        write(root)
        print(res)
        return " ".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
#         def read():
#             val = next(vals)
#             if val == "#":
#                 return None
#             node = TreeNode(int(val))
#             node.left = read()
#             node.right = read()
#             return node
        
#         vals = iter(data.split())
#         return read()
    
        def read():
            val = vals.popleft()
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = read()
            node.right = read()
            return node
        
        vals = collections.deque(data.split(" "))
        return read()
                
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))