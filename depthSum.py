class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        if len(nestedList) == 0:
            return 0
        stack = []
        sum = 0
        for i in nestedList:
            stack.append((i,1))
        
        while stack:
            next, d = stack.pop(0)
            if next.isInteger():
                sum += d * next.getInteger()
            else:
                for i in next.getList():
                    stack.append((i,d+1))
        return sum    
