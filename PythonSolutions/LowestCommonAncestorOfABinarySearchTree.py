# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root != p and root != q:
            if p.val < root.val < q.val or p.val > root.val > q.val:
                return root
            if p.val < root.val:
                root = root.left
            else:
                root = root.right
        if root == p:
            return p
        if root == q:
            return q
