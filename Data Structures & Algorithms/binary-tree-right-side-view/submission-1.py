# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        rightside =[]
        queue = [root]
        while queue:
            temp=[]
            n = len(queue)
            for i in range(n):
                node  = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            rightside.append(temp)
        ans =[]
        for i in range(len(rightside)):
            ans.append(rightside[i][-1])
        return ans


        