# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, r, sr):
        if not r and not sr:
            return True
        elif not r or not sr:
            return False
        return r.val == sr.val and self.isSameTree(r.left, sr.left) and self.isSameTree(r.right, sr.right)

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if self.isSameTree(root, subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
