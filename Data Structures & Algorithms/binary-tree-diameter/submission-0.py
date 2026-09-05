# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #go all the way to the left
        #go all the way to the right
        #subtract

        maxx = [0]

        def height(root):
            if root is None:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            
            diameter = left + right
            maxx[0] = max(maxx[0], diameter)

            return 1 + max(left, right)

        height(root)
        return maxx[0]

