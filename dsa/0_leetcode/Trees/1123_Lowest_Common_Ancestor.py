# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Naive Approach
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
            
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def lcaDeepestLeaves(self, root):
        left = self.maxDepth(root.left) if root.left else 0
        right = self.maxDepth(root.right) if root.right else 0
        
        if left == right:
            return root
        
        if left > right:
            return self.lcaDeepestLeaves(self.left)
        else:
            return self.lcaDeepestLeaves(self.right)


class Solution:
    def lcaDeepestLeaves(self, root):
        def dfs(node):
            if not node:
                return (0, None)
            
            ld, llca = dfs(node.left)
            rd, rlca = dfs(node.right)
            
            if ld == rd:
                return (ld, node)
            if ld > rd:
                return (ld+1,llca)
            else:
                return (rd+1, rlca)
            
        return dfs(root)[1]



