# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        maxdiff=0
        def dfs(node):
            nonlocal maxdiff
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            maxdiff = max(maxdiff, abs(left-right))

            return 1 +max(left,right)
        dfs(root)
        if maxdiff >1:
            return False 
        else :
            return True 
            
        