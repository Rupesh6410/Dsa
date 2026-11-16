class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return False
        def issym(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val!=q.val:
                return False
            return issym(p.left,q.right) and issym(p.right,q.left)
        return issym(root.left,root.right)
