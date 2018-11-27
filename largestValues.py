"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
#bfs

class Solution:
    """
    @param root: a root of integer
    @return: return a list of integer
    """
    def largestValues(self, root):
        self.ans = []
        self.helper(root,0)
        print '233'
        return self.ans
    
    def helper(self, node, level):
        if not node:
            return []
        if len(self.ans) == level:
            self.ans.append(node.val)
            print self.ans,level
        else:
            print'##', node.val,level
            self.ans[level] = max(self.ans[level], node.val)
        print 'aa',level
        self.helper(node.left, level + 1)
        print 'a', level
        self.helper(node.right, level +1)
        print 'b', level
    
    # def largestValues(self, root):
    #     ans = []
    #     if root is None:
    #         return ans
    #     queue = [root]
    #     while queue:
    #         ans.append(max(x.val for x in queue))
    #         new_queue = []
    #         for node in queue:
    #             if node.left:
    #                 new_queue.append(node.left)
    #             if node.right:
    #                 new_queue.append(node.right)
    #         queue = new_queue
    #     return ans
    # BFS
