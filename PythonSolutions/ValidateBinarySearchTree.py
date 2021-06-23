import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def solve(root, less, more):
            if not root:
                return True
            if not less<root.val<more:
                return False
            else:
                return solve(root.left, less, root.val) and solve(root.right, root.val, more)
        return solve(root, -math.inf, math.inf)