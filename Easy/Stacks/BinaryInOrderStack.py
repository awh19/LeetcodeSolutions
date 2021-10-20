class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        outputNodes = []
        current = root
        
        if root is None:
            return outputNodes
        
        while current is not None or len(stack):
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            outputNodes.append(current.val)
            current = current.right
            
        return outputNodes
        
    # Uses a stack to traverse the list linearly instead of recursively