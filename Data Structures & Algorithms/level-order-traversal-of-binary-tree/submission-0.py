# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        nodeQueue = []
        res = []

        if root:
            nodeQueue.append(root)

        while nodeQueue:
            curSize = len(nodeQueue)
            levelList = []

            for _ in range(curSize):
                node = nodeQueue.pop(0)

                levelList.append(node.val)
                
                if node.left:
                    nodeQueue.append(node.left)
                    
                if node.right:
                    nodeQueue.append(node.right)

            res.append(levelList)

        return res