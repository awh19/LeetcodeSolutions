class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        charDict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        stack = []
        
        for c in s:
            if c in charDict:
                if stack and stack[-1] == charDict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False
        
# Notes Learned:
# - Python lists can be used as stacks
# - stack[-1] refers to the most recently added item due to negative indexes