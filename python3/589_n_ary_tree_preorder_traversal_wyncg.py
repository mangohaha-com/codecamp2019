"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        """ iterative
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            temp = stack.pop()
            result.append(temp.val)
            stack.extend(temp.children[::-1])
            
            
        return result
        """
        
        #recursive
        if root is None:
            return []
        result = [root.val]
        for child in root.children:
            result.extend(self.preorder(child))
        return result