# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            curr = node == p or node == q

            if left + right + curr >= 2:
                self.ans = node

            if right or left or curr:
                return True

            return False

        dfs(root)
        return self.ans
