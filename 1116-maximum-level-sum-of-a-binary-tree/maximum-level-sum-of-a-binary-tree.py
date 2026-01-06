# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxLevelSum(self, root):
        q = deque([root])
        level, maxLevel = 1, 1
        maxSum = root.val
        
        while q:
            size = len(q)
            s = 0
            for _ in range(size):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s > maxSum:
                maxSum = s
                maxLevel = level
            level += 1
        
        return maxLevel

        