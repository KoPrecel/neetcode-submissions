# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            max_diameter = 0
            height = 0
            left_height = 0
            right_height = 0
            left_max = 0
            right_max = 0

            if not node:
                return (0, 0)
            
            if node.left:
                (left_height, left_max) = dfs(node.left)

            if node.right:
                (right_height, right_max) = dfs(node.right)

            height = max(left_height, right_height) + 1
            max_diameter = max(left_max, right_max)
            max_diameter = max(max_diameter, left_height + right_height)

            return (height, max_diameter)

        _, res = dfs(root)
        return res
