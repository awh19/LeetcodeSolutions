# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodeList = []
        self.traversalHelper(root,nodeList)
        return nodeList
        
        
    def traversalHelper(self, root: Optional[TreeNode], nodeList: List[int]):
        if root is not None:
            if root.left is not None:
                self.traversalHelper(root.left, nodeList)
            nodeList.append(root.val)
            if root.right is not None:   
                self.traversalHelper(root.right, nodeList)

    
        
    #Notes Learned:
    # - Always make sure to call the value and not the root itself
    # - Can also use a stack for this kind of problem.