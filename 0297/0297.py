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
        if not root:
            return None
        
        nodes = []
        def helper(root):
            if not root:
                nodes.append('null')
                return 
            nodes.append(str(root.val))
            helper(root.left)
            helper(root.right)
            
        helper(root)
        return " ".join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        nodes = data.split(" ")
        def helper(nodes):
            if nodes:
                node = nodes.pop(0)
                if node == "null":
                    return None
                else:
                    new = TreeNode(int(node))
                    new.left = helper(nodes)
                    new.right = helper(nodes)
                    return new
        return helper(nodes)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
