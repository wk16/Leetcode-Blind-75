# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = [root]
        level = []
        nextLevel = []
        while q:
            el = q.pop(0)
            level.append(el.val)
            if el.left:
                nextLevel.append(el.left)
            if el.right:
                nextLevel.append(el.right)

            if len(q) == 0:
                res.append(level)
                q = nextLevel
                level, nextLevel = [], []
        return res
