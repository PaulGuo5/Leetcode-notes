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
        def write(root, res):
            if not root:
                res.append("#")
            else:
                res.append(str(root.val))
                write(root.left, res)
                write(root.right, res)
        res = []
        write(root, res)
        return " ".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = collections.deque(data.split(" "))
        def read():
            val = data.popleft()
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = read()
            node.right = read()
            return node
        return read()
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
