"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        def write(root):
            if not root:
                return
            res.append(str(root.val))
            for child in root.children:
                write(child)
            res.append("#")
        
        res = []
        write(root)
        return " ".join(res)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data: 
            return None
        data = collections.deque(data.split(" "))
        root = Node(int(data.popleft()), [])
        q = [root]
        while data:
            val = data.popleft()
            if val == "#":
                q.pop()
            else:
                new = Node(int(val), [])
                q[-1].children.append(new)
                q.append(new)
        return root
                
            
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
