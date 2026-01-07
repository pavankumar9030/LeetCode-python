# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root):
        self.total = 0
        self.max_prod = 0
        
        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            self.max_prod = max(self.max_prod, s * (self.total - s))
            return s
        
        self.total = dfs(root)
        dfs(root)
        return self.max_prod % (10**9 + 7)
