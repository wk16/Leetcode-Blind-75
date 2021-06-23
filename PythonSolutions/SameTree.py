class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(p, q):
            if p and q:
                if p.val != q.val:
                    return False
                else:
                    return dfs(p.right, q.right) and dfs(p.left, q.left)
            elif not p and not q:
                return True
            else:
                return False

        return dfs(p, q)
