import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, maxi, mini):
            if not node:
                return True

            if not node.val < maxi or not node.val > mini:
                return False

            return dfs(node.left, node.val, mini) and dfs(
                node.right, maxi, node.val
            )

        return dfs(root, math.inf, -math.inf)
