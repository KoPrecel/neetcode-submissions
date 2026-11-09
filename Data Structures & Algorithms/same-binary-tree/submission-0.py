# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p = [4, 7], q = [4, None, 7]
        # p = 7, q = None
        if p is None and q is None:
            return True
        else:

            if p and q and (p.val == q.val):
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False

        

        