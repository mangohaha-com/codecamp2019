class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack = []
        result = 0
        #['dir', '\tsubdir1', '\t\tfile1.ext', '\t\tsubsubdir1', '\tsubdir2', '\t\tsubsubdir2', '\t\t\tfile2.ext']
        #['dir', '    file.txt']
        for current in input.split('\n'):
            current_length = len(current)
            pure_current_length = len(current.lstrip('\t'))
            level = (current_length - pure_current_length) / 2
            if len(stack) == 0:
                # init
                if '.' in current:
                    # check if file
                    result = max(result, pure_current_length)
                else:
                    stack.append([pure_current_length, level])
            else:
                previous_length = stack[-1][0]
                previous_level = stack[-1][1]
                if level > previous_level:
                    # check if deeper level
                    if '.' in current:
                        # check if file
                        result = max(result, previous_length + 1 + pure_current_length)
                    else:
                        stack.append([previous_length + 1 + pure_current_length, level])
                else:
                    while len(stack) != 0 and level <= previous_level:
                        stack.pop()
                        # check if root is not single
                        if len(stack) != 0:
                            previous_level = stack[-1][1]
                            previous_length = stack[-1][0]
                        else:
                            previous_level = 0
                            previous_length = 0
                    # if root, no plus 1 for '/'
                    new_result = previous_length + pure_current_length if level == 0 else previous_length + 1 + pure_current_length
                    if '.' in current:
                        # check if file
                        result = max(result, new_result)
                    else:
                        stack.append([new_result, level]) 
        return result
