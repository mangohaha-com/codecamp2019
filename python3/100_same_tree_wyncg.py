class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        """
        recursive
        def compare(pNode, qNode):
            #:type pNode: TreeNode
            #:type qNode: TreeNode
            #:rtype: bool
            if pNode == None and qNode == None:
                return True
            if pNode == None and qNode != None or pNode != None and qNode == None:
                return False
            return pNode.val == qNode.val
                
        pStack = [p]
        qStack = [q]
        while pStack and qStack:
            currentP = pStack.pop(0)
            currentQ = qStack.pop(0)
            if not compare(currentP, currentQ):
                return False
            if currentP: pStack.extend([currentP.left, currentP.right])
            if currentQ: qStack.extend([currentQ.left, currentQ.right])
            
        return True
        """

        #iterate
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == None and q == None